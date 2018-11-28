#include<cstdio>
#include<cstring>

int T, N;
bool vis[10];

int main() {
    scanf("%d", &T);
    for(int cas = 1; cas <= T; cas++) {
        scanf("%d", &N);
        printf("Case #%d: ", cas);
        if(N == 0) {
            printf("INSOMNIA\n");
        }
        else {
            int ans = N, left = 10;
            memset(vis, 0, sizeof(vis));
            while(true) {
                int tmp = ans;
                while(tmp) {
                    int x = tmp % 10;
                    tmp /= 10;
                    if(vis[x] == false) {
                        vis[x] = true;
                        left--;
                    }
                }
                if(left == 0) {
                    break;
                }
                ans += N;
            }
            printf("%d\n", ans);
        }
    }
    return 0;
}