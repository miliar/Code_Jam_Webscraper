/*Santiago Zubieta*/
#include <iostream>
#include <numeric>
#include <fstream>
#include <climits>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <queue>
#include <list>
#include <map>
#include <set>
#include <stack>
#include <deque>
#include <vector>
#include <string>
#include <cstdlib>
#include <cassert>
#include <sstream>
#include <iterator>
#include <algorithm>

#define ull unsigned long long
using namespace std;

// 0:  1, 1:  i, 2:  j, 3:  k
// 4: -1, 5: -i, 6: -j, 7: -k

int neg(int quat) {
    return (quat + 4) % 8;
}

int mult(int quat1, int quat2) {
    // First, the basic * 1 or * -1 operations.
    if(quat2 == 0) return quat1;
    // X * 1 == X
    if(quat1 == 0) return quat2;
    // 1 * Y == Y
    if(quat2 > 3) return neg(mult(quat1, neg(quat2)));
    // If the second value is negative, make it positive and neg the result.
    if(quat1 > 3) return neg(mult(neg(quat1), quat2));
    // If the first value is negative, make it positive and neg the result.

    // From here on, we ideally want to deal only with positive things, if some-
    // thing negative was received, the previous conditions will change their
    // sign and then revert the sign change.

    if(quat1 == quat2) return 4;
    // Equal quaternions will result in a -1.

    if((quat1 + 1) % 3 != quat2 % 3) {
    // We need the first one to be lesser in the order i -> j -> k
        return neg(mult(quat2, quat1));
    }

    int res = quat1 + quat2;
    if(res == 3) return 3;
    // 1(i) + 2(j) == 3(k)
    if(res == 5) return 1;
    // 2(j) + 3(k) == 5(i)
    if(res == 4) return 2;
    // 3(k) + 1(i) == 4(j)
}

int convert(char quatChar) {
    switch(quatChar) {
        case 'i' : return 1;
        // 'i' is binded to 2
        case 'j' : return 2;
        // 'j' is binded to 3
        case 'k' : return 3;
        // 'k' is binded to 4
    }
}

bool validateQuaternion(ull start, string quat, char current) {
    int lookFor = convert(current);
    int value = 0;
    // Initially have a 1 to start multiplying values.
    for(ull z = start; z < quat.length(); z++) {
        int res = mult(value, convert(quat[z]));
        value = res; 

        // Multiply the previous value with the current position, this is the
        // reduction of quaternion symbols into less quaternion symbols.
        if(value == lookFor) {
        // If what we're currently looking is the current reduction:
            bool subRes = false;
            if(current == 'i') {
            // If we reduced an 'i', lets start looking for a 'j' reduction
            // starting from the next symbol.
                return validateQuaternion(z + 1, quat, 'j');
            }
            if(current == 'j') {
            // If we reduced a 'j', lets start looking for a 'k' reduction
            // starting from the next symbol.
                return validateQuaternion(z + 1, quat, 'k');
            }
            if(current == 'k') {
            // If we reduced a 'k', we need it to be at the end of the chain
            // of quaternion symbols, otherwise we haven't fully reduced the
            // chain of symbols.
                if(z + 1 == quat.length()) {
                    return true;
                }
                else {
                    continue;
                }
            }
        }
    }
    // If it finishes traversing the string, and no reduction was possible to
    // the aforementioned 'ijk' chain, or it exceeded the bounds while trying
    // to reduce a symbol, then it will return false.
    return false;
}

int main() {
    int T;

    scanf("%d", &T);

    for(int z = 0; z < T; z++){
        string quaternion;
        ull chars, repeats;
        cin >> chars >> repeats;
        cin >> quaternion;
        string quat = "";
        for(ull k = 0; k < repeats; k++) {
            quat += quaternion;
        }

        bool result = validateQuaternion(0, quat, 'i');
        printf("Case #%d: %s", z + 1, (result)? "YES" : "NO");
        if(z + 1 < T){
            puts("");
        }
    }
}

/*
    Start traversing the string, multiplying quaternions
    
    1. if an i is reduced, start from the next symbol reducing a j, if you
       can't reduce a j, or the result of 2. is false, then keep reducing 
       until finding another i.

    2. if a j is reduced, start from the next symbol reducing a k, if you
       can't reduce a k, or the result of 3. is false, then keep reducing
       until finding another j.

    3. if a k is reduced, and you've consumed the whole string, then return
       true, if there's still parts of the string left to consume, keep
       reducing it until finding another k.
*/