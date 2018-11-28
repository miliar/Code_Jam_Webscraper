#include <bits/stdc++.h>

using namespace std;

int t,tt,ans,e,i;
long long x,n;
int main(){
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d",&t);
    for(int tt=1;tt<=t;tt++){
        scanf("%lld",&n);ans=-1;e=0;
        for(int i=1;i<=1000000000;i++){
            x=n*i;
            while(x){
                e|=(1<<(x%10));
                x/=10;
            }
            if(e==1023){ans=i;break;}
        }
        printf("Case #%d: ",tt);
        if(ans==-1)puts("INSOMNIA");else printf("%lld\n",n*ans);
    }
    return 0;
}