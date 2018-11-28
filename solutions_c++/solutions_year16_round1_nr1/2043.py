#include<cstdio>
#include<iostream>
#include<cmath>
#include<cstring>
#include<string>
#include<vector>
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
#define pb push_back
#define ll long long

using namespace std;

int t;
char a[1010];
int b[3010];


int main(){
   freopen("A-large.in","r",stdin);
   freopen("A-large.out","w",stdout);
   _s(t);
   REP(cas,1,t){
     _ss(a);
     int k=strlen(a);
     int l=1500,r=1500;
     b[l]=0;
     rep(i,1,k){
       if(a[i]>=a[b[l]]){
          b[--l]=i;
       }else{
          b[++r]=i;
       }
     }
     printf("Case #%d: ",cas);
     REP(i,l,r){
        _pc(a[b[i]]);
     }
     _pn;
   }

}
