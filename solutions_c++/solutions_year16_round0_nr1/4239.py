#include<bits/stdc++.h>
using namespace std;

typedef __int64 ll;

int n;

int main() {
    freopen("A-large.in","r",stdin);
    freopen("text.txt","w",stdout);
    int T;
    scanf("%d",&T);
    for(int ca=1;ca<=T;ca++) {
        scanf("%d",&n);
       // printf("FF %d\n",n);
        bool vis[11]={0};
        int num=0;
        printf("Case #%d: ",ca);
        for(int i=1;i<1000000;i++) {
            ll t=1ll*i*n;
            while(t) {
                int tmp=t%10;
                if(!vis[tmp]) vis[tmp]=1,num++;
                t/=10;
            }
            if(num==10) {
                printf("%I64d\n",1ll*i*n);
                break;
            }
        }
        if(num!=10) puts("INSOMNIA");
    }
    return 0;
}
