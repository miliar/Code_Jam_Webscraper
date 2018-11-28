#include<bits/stdc++.h>
#include <iostream>
#include <fstream>
using namespace std;

#define MAX(a,b) ((a)>(b)?(a):(b))
#define MIN(a,b) ((a)<(b)?(a):(b))

#define REP(i,a,b) for(i=a;i<b;i++)
#define rep(i,b) for(i=0;i<b;i++)
#define rep1(i,b) for(i=1;i<=b;i++)

#define plln(n) printf("%lld\n",n)

#define s3ll(n1,n2,n3) scanf("%lld%lld%lld",&n1,&n2,&n3)
#define s2ll(n1,n2) scanf("%lld%lld",&n1,&n2)
#define sll(n) scanf("%lld",&n)

typedef long long LL;

#define MOD 1000000007
#define mx 1000000

int main()
{
    LL t,n,c,s,ans,p=1,i;
    freopen("largeinp.in", "r", stdin);
    freopen("largeout.out", "w", stdout);
    sll(t);
    while(t--)
    {
        s=c=ans=0;
        sll(n);
        string str;
        cin>>str;
        rep(i,n+1){
            c++;
            s+=(str[i]-'0');
            if(s<c){
                ans+=(c-s);
                s+=(c-s);
            }
        }
        printf("Case #%lld: ",p);
        printf("%lld\n",ans);
         p++;
    }
    return 0;
}
