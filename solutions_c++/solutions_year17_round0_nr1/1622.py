#include <bits/stdc++.h>

#define LL long long

using namespace std;

const int maxn = 1005;

char s[maxn];

int K, a[maxn];

int main(){
    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; cas++){
        scanf("%s", s);
        scanf("%d", &K);
        int len = strlen(s), ans = 0;
        for (int i = 0; i < len; i++){
            if (s[i] == '+') a[i] = 1; else a[i] = 0;
        }
        for (int i = 0; i + K <= len; i++){
            if (a[i] == 1) continue;
            ans += 1;
            for (int j = 0; j < K; j++)
                a[i + j] = 1 - a[i + j];
        }
        for (int i = 0; i < len; i++){
            if (a[i] == 0){
                ans = -1;
                break;
            }
        }
        if (ans == -1)
            printf("Case #%d: IMPOSSIBLE\n", cas);
        else
            printf("Case #%d: %d\n", cas, ans);
    }
    return 0;
}
