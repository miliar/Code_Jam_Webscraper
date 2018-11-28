#include <bits/stdc++.h>

using namespace std;

typedef long long LL;

const int N = 1100;
char s[N];

int main() {
    int T;
    scanf("%d", &T);
    for (int _ = 1; _ <= T; _++) {
        int k;
        scanf("%s%d", s, &k);
        int n = strlen(s);
        int cnt = 0;
        for (int i = 0; i <= n - k; i++) {
            if (s[i] == '-') {
                cnt++;
                for (int j = i; j < i + k; j++) s[j] = s[j] == '-' ? '+' : '-'; 
            }
        }
        bool flag = 1;
        for (int i = 0; i < n; i++) if (s[i] != '+') flag = 0;
        printf("Case #%d: ", _);
        if (flag) printf("%d\n", cnt);
        else puts("IMPOSSIBLE");
    }
    return 0;
}
