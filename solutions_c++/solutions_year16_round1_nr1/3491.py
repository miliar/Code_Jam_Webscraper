#include <cstdio>
#include <cstdlib>
#include <stdint.h>
#include <iostream>
#include <sstream>
#include <vector>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <algorithm>

using namespace std;

int main()
{
    int T; string S;
    cin >> T;
    for (int i = 1; i <= T; ++i) {
        cin >> S;
        int len = S.length();
        string res = S;
        // count pos
        int count = 0;
        int curr = 0;
        for (int i = 1; i < len; ++i) {
            if (S[i] >= S[curr]) {
                ++count; curr = i;
            }
        }
        res[count] = S[0]; curr = count + 1;
        for (int i = 1; i < len; ++i) {
            if (S[i] >= res[count]) {
                res[--count] = S[i];
            }
            else {
                res[curr++] = S[i];
            }
        }

        cout << "Case #" << i << ": " << res << endl;
    }
    return 0;
}
