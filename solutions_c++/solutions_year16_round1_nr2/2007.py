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
int n;
int a[200][200];
map<int,int> Mp;
set<int> St;

int main(){
   freopen("B-large.in","r",stdin);
   freopen("B-large.out","w",stdout);
   _s(t);
   REP(cas,1,t){
     _s(n);
     Mp.clear();St.clear();
     REP(i,1,2*n-1){
        REP(j,1,n){
           _s(a[i][j]);
           Mp[a[i][j]]++;
        }
     }
     map<int,int>::iterator it=Mp.begin();
     for(;it!=Mp.end();it++){
        if(it->second%2==1){
            St.insert(it->first);
        }
     }
     printf("Case #%d: ",cas);
     set<int>::iterator it1=St.begin();
     for(;it1!=St.end();it1++){
         _pt(*it1);_p;
     }
     _pn;
   }
}
