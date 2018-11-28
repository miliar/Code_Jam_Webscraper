/// Google Code Jam
/// Author   : Rajdip Saha
/// Language : C++

#include <bits/stdc++.h>

#define MAX 100005
#define INF 111111111111111111

typedef long long ll;
typedef unsigned long long llu;

using namespace std;

bool digit[15];

int main()
{
    //freopen("A-large.in","r",stdin);
    //freopen("out.txt","w",stdout);
    ll t,n;
    scanf("%lld",&t);
    for(ll i=1;i<=t;i++){
        scanf("%lld",&n);
        if(!n){
            printf("Case #%lld: INSOMNIA\n",i);
            continue;
        }
        memset(digit,false,sizeof(digit));
        ll cnt=0;
        ll num,res;
        for(ll j=1;;j++){
            if(cnt==10)break;
            num=res=n*j;
            for(ll d=num;d>0;d/=10){
                ll m=d%10;
                if(!digit[m])digit[m]=true,cnt++;
            }
        }
        printf("Case #%lld: %lld\n",i,res);
    }
    return 0;
}
