#include <stdio.h>
#include <cstring>
using namespace std;

bool vis[20];

int main(){
        freopen("a.in", "r", stdin);
        freopen("a.out", "w", stdout);

        int tt, ca = 0;
        scanf("%d", &tt);
        while (tt--) {
                printf("Case #%d: ", ++ca);
                int n;
                scanf("%d", &n);
                if (n == 0) { printf("INSOMNIA\n"); continue;}
                
                memset(vis, 0, sizeof(vis));
                int cnt = 0;
                long long i;
                for (i = n; cnt < 10; i += n){
                        long long t = i;
                        while (t){
                                int dig = t % 10;
                                if (!vis[dig]) {vis[dig] = true; cnt ++;}
                                t /= 10;
                        }
                        if (cnt >= 10) break;
                }
                printf("%lld\n", i);
        }
}
