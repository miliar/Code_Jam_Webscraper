#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

char s[105];

int main() {
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int cases;
    scanf ("%d", &cases);
    for (int cas = 1; cas <= cases; cas ++) {
        cin >> s;
        int len = strlen(s);
        int i = len - 1;
        int ans = 0;
        while (i >= 0 && s[i] == '+') {
            i--;
        }
        char pre, cur;
        if (i >= 0) {
            pre = s[i];
            i--;
            ans ++;
        }
        for (;i >= 0; i--) {
            cur = s[i];
            if (cur == pre) continue;
            else {
                pre = cur;
                ans ++;
            }
        }
        printf ("Case #%d: %d\n", cas, ans);

    }


    return 0;
}

