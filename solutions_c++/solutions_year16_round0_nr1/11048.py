#include <bits/stdc++.h>
using namespace std;

int n, cnt;
long long x, z;
bool vis[15];

int main()
{
   freopen("r.txt","r",stdin);
   freopen("pr.txt","w",stdout);
   scanf("%d", &n);
   for(int i=0;i<n;i++){
        scanf("%lld",&x);
        printf("Case #%d: ", i+1);
        cnt=0, memset(vis,0, sizeof vis);
        for(int j=1;j<50000;j++){
            z=x*j;
            while(z){
                if(vis[z%10]==0)
                    cnt++;
                vis[z%10]=1, z/=10;
            }
            if(cnt==10){
                printf("%lld\n", j*x);
                break;
            }
        }
        if(cnt!=10)
            printf("INSOMNIA\n");
   }

    return 0;
}
