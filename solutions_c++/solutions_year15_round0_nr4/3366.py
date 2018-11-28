#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstring>
#include <vector>
#include <string>

using namespace std;

#define MAXN 1000

int T, n, a, b, c;

string solve() {
    string GB = "GABRIEL";
    string RC = "RICHARD";
    if (a == 1) return GB;
    if (a == 2) {
        if ((b * c)% 2 == 0) return GB;
        else return RC;
    }

    if(a == 3) {
        if ((b * c) % 3 == 0) {
            if (b == 1 || c == 1) return RC;
            else return GB;
        }
        else return RC;
    }
    if(a == 4) {
        if ((b * c) % 4 == 0) {
            if (b == 1 || c == 1) {
                return RC;
            }
            else if(b == 2 || c == 2) return RC;
            else if(b == 3 || c == 3) return GB;
            else return GB;
        }
        else return RC;
    }
}

int main () {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    //preCal();
    scanf("%d", &T);
    for(int i = 1; i <= T; i++) {
        scanf("%d %d %d", &a, &b, &c);
        printf("Case #%d: ", i);
        cout << solve() << endl;
    }
    return 0;
}
