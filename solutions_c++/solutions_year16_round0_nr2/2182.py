#include <bits/stdc++.h>

using namespace std;

int T, cas; char ch[105];

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    cin >> T;
    while (T --) {
        scanf(" %s", ch);
        printf("Case #%d: ", ++ cas);
        int n = strlen(ch) - 1;
        while (n >= 0 && ch[n] == '+')
            n --;
        if (n < 0) {
            puts("0");
            continue;
        }
        int cnt = 0;
        for (int i = 1; i <= n; i ++) {
            if (ch[i] != ch[i - 1]) cnt ++;
        }
        printf("%d\n", cnt + 1);
    }
}
