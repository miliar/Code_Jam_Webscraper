#include <bits/stdc++.h>

#define LL long long
#define INF 0x3f3f3f3f
#define eps 1e-8

using namespace std;

bool vis[15];
int main(){
#ifndef ONLINE_JUDGE
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
#endif // ONLINE_JUDGE
    int T;
    scanf("%d", &T);
    int n;
    int cas = 0;
    while(T--){
        scanf("%d", &n);
        memset(vis, 0, sizeof(vis));
        int ans = -1;
        int cnt = 0;
        int m = n;
        int p = 0;
        while(true){
            int x = m;
            while(x > 0){
                int y = x % 10;
                if(!vis[y]){
                    ++cnt;
                    vis[y] = true;
                }
                x /= 10;
            }
            if(cnt >= 10){
                ans = m;
                break;
            }
            m += n;
            if(m <= 0) break;
            if(++p > 100000) break;
        }
        if(ans == -1){
            printf("Case #%d: INSOMNIA\n", ++cas);
        }
        else{
            printf("Case #%d: %d\n", ++cas, ans);
        }
    }
}
