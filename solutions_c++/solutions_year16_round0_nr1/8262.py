#include <bits/stdc++.h>
#define PB push_back
#define FT first
#define SD second
#define MP make_pair
#define INF 0x3f3f3f3f
using namespace std;
typedef long long LL;
typedef unsigned long long ULL;
typedef pair<int,int>  P;
const int N = 2333,MOD = 7+1e9;
bool vis[10];
bool work(int x)
{
    while(x) {
        vis[x % 10] = 1;
        x /= 10;
    }
    for(int i = 0;i < 10;i ++) if(!vis[i]) return 0;
    return 1;
}
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int T, ca = 0;
    scanf("%d", &T);
    while(T --) {
        int n;
        scanf("%d", &n);
        memset(vis, 0, sizeof vis);
        printf("Case #%d: ", ++ ca);
        if(n == 0) {
            puts("INSOMNIA");
            continue;
        }
        int ans = 1;
        while(1) {
            if(work(ans * n)) {
                break;
            }  
            ans ++;
        } 
        printf("%d\n", ans * n);
    }
    return 0;
}