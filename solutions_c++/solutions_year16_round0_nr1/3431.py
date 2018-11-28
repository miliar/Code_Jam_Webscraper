#include <bits/stdc++.h>
using namespace std;
#define LL long long
int dig[10];

int main()
{
    freopen("out.txt","w",stdout);
    LL t;
    scanf("%lld",&t);
    for(int cs=1;cs<=t;cs++){
        LL n;
        scanf("%lld",&n);
        memset(dig,0,sizeof(dig));
        int cnt=0;
        int i;
        for(i=1;i<=1e5;i++){
            LL tmp=n*i;
            while(tmp!=0){
                if(dig[tmp%10]==0){
                    dig[tmp%10]=1;
                    cnt++;
                }
                tmp/=10;
            }
            if(cnt==10) break;
        }
        if(cnt==10) printf("Case #%d: %lld\n",cs,n*i);
        else printf("Case #%d: INSOMNIA\n",cs);
    }
    return 0;
}
