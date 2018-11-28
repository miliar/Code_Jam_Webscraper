#include<cstdio>
#include<iostream>
#include<cmath>
#include<cstring>
#include<string>
#include<map>
#include<set>
#include<algorithm>
#define CLR(x) memset(x,0,sizeof(x))
#define REP(i,l,r) for(int i=l;i<=r;i++)
#define rep(i,l,r) for(int i=l;i<r;i++)
#define RREP(i,l,r) for(int i=l;i>=r;i--)
#define rrep(i,l,r) for(int i=l;i>r;i--)
#define _s(x) scanf("%d",&x)
#define _sc(x) scanf("%c",&x)
#define _ss(x) scanf(" %s",x)
#define _sl(x) scanf("%I64d",&x)
#define _sd(x) scanf("%lf",&x)
#define _pt(x) printf("%d",x)
#define _ps(x) printf("%s",x)
#define _pc(x) printf("%c",x)
#define _pd(x) printf("%f",x);
#define _pl(x) printf("%I64d",x)
#define _pn printf("\n");
#define _p printf(" ");
#define gch getchar()
#define debug(x) printf("%d\n",x)
#define ll long long

using namespace std;

int t,n,a[10];

bool check(){
   REP(i,0,9){
     if(!a[i]) return 1;
   }
   return 0;
}

int main(){
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    _s(t);

    int cnt=0;
    REP(i,1,t){
        _s(n);
        printf("Case #%d: ",i);
        ll ans=0;
        int num=0;
        if(n==0){
           _ps("INSOMNIA\n");
           continue;
        }
        CLR(a);
        while(check()){
            ans+=n;
            ll t=ans;
            while(t){
               if(!a[t%10]) a[t%10]=1;
               t/=10;
            }
        }
        _pt(ans);_pn;
    }
}
