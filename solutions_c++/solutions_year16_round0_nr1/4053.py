#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

typedef long long ll;
int vis[10];

int main(){
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int T,t = 0;
    scanf("%d",&T);
    while(T--){
        int cnt = 0;
        ll x,n;
        memset(vis,0,sizeof(vis));
        scanf("%lld",&n);
        if(n == 0){
            printf("Case #%d: INSOMNIA\n",++t);
            continue;
        }
        for(int i = 1; ; ++i){
            x = i*n;
            while(x){
                if(!vis[x%10]){
                    cnt++;
                    vis[x%10] = 1;
                }
                x /= 10;
            }
            if(cnt == 10){
                printf("Case #%d: %lld\n",++t,i*n);
                break;
            }
        }
    }
    return 0;
}
