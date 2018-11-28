// @author kelvin
// #includes {{{
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cassert>
#include <cmath>
#include <iostream>
#include <sstream>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <string>
#include <algorithm>
#include <functional>
using namespace std;
// }}}
// #defines {{{
#define RI(x) scanf("%d",&(x))
#define RII(x,y) scanf("%d %d",&(x),&(y))
#define RF(x) scanf("%lf",&(x))
#define RS(x) scanf("%s",x)
#define PRI(x) printf("%d\n",x);
#define PR printf
#define MP(x,y) make_pair(x,y)
#define PB(x) push_back(x)
#define POP() pop_back()
#define F first
#define S second
typedef pair<int,int> pii;
// }}}
// #functions {{{
pii operator+(const pii &a,const pii &b) { return MP(a.F+b.F,a.S+b.S); }
pii operator-(const pii &a,const pii &b) { return MP(a.F-b.F,a.S-b.S); }
pii& operator+=(pii &a,const pii &b) { a.F+=b.F; a.S+=b.S; return a; }
pii& operator-=(pii &a,const pii &b) { a.F-=b.F; a.S-=b.S; return a; }
template <class T,class U>
bool cmp_second(const pair<T,U> &a,const pair<T,U> &b) { return a.second<b.second; }
template <class T>
T gcd(T a,T b) { a=abs(a); b=abs(b); while(b) { T t=b; b=a%b; a=t; } return a; }
template <class T>
pair<T,T> ext_gcd(T a,T b) {
   T a0=1,a1=0,b0=0,b1=1;
   if(a<0) { a=-a; a0=-1; }
   if(b<0) { b=-b; b1=-1; }
   while(b) {
      T t,q=a/b;
      t=b; b=a-b*q; a=t;
      t=b0; b0=a0-b0*q; a0=t;
      t=b1; b1=a1-b1*q; a1=t;
   }
   return MP(a0,a1);
}
inline int sg(int x) { return x?(x>0?1:-1):0; }
// }}}

#define MAXN 2050

int n;
int lis[MAXN],lds[MAXN];
int pi[MAXN],pd[MAXN];
int s[MAXN];

pii pt[MAXN];
int deg[MAXN];
bool vis[MAXN];

inline bool lt(pii a,pii b) {
   return a.F<=b.F&&a.S<=b.S;
}

int ii[MAXN],dd[MAXN];
bool check() {
   /*for(int i=0;i<n;i++)
      fprintf(stderr," %d",s[i]); fputs("\n",stderr);*/
   for(int i=0;i<n;i++) {
      if(s[i]<0||s[i]>n) return 0;
      for(int j=i+1;j<n;j++)
         if(s[i]==s[j]) return 0;
   }
   for(int i=0;i<n;i++) {
      int ma=0;
      for(int j=0;j<i;j++)
         if(s[j]<s[i]) ma=max(ma,ii[j]);
      ii[i]=ma+1;
   }
   for(int i=n-1;i>=0;i--) {
      int ma=0;
      for(int j=n-1;j>i;j--)
         if(s[j]<s[i]) ma=max(ma,dd[j]);
      dd[i]=ma+1;
   }
   /*fprintf(stderr,"checking lis & lds\n");
   for(int i=0;i<n;i++)
      if(ii[i]!=lis[i]||dd[i]!=lds[i]) return 0;
   fprintf(stderr,"done\n");*/
   return 1;
}

void solve() {
   //vector<int>a arr;
   //arr.PB(1);
   //memset(s,-1,sizeof(s));
   memset(deg,0,sizeof(deg));
   memset(vis,0,sizeof(vis));
   for(int i=0;i<n;i++)
      pt[i]=MP(lis[i],lds[i]);
   for(int i=0;i<n;i++)
      for(int j=0;j<n;j++)
         if(i!=j&&lt(pt[i],pt[j])) deg[j]++;
   for(int x=1;x<=n;x++) {
      pi[0]=0;
      for(int j=0;j<=n;j++) {
         if(vis[j]) pi[j+1]=max(pi[j],lis[j]);
         else pi[j+1]=pi[j];
      }
      pd[n]=0;
      for(int j=n-1;j>=0;j--) {
         if(vis[j]) pd[j]=max(pd[j+1],lds[j]);
         else pd[j]=pd[j+1];
      }
      for(int i=0;i<n;i++) {
         if(vis[i]||deg[i]) continue;
         if(pi[i]+1!=lis[i]||pd[i]+1!=lds[i]) continue;
         vis[i]=1;
         s[i]=x;
         for(int j=0;j<n;j++)
            if(i!=j&&lt(pt[i],pt[j])) deg[j]--;
         break;
      }
   }
   assert(check());
   /*fprintf(stderr,"(%d)\n",(int)arr.size());
   assert(arr.size()==n);
   for(int i=0;i<n;i++)
      s[arr[i]]=i+1;*/
   for(int i=0;i<n;i++)
      printf(" %d",s[i]); puts("");
}

int main(void) {
   int t,cas=1;
   RI(t);
   while(t--) {
      RI(n);
      for(int i=0;i<n;i++)
         RI(lis[i]);
      for(int i=0;i<n;i++)
         RI(lds[i]);
      printf("Case #%d:",cas++);
      solve();
   }
   return 0;
}

// vim: fdm=marker:commentstring=//\ %s:nowrap:autoread

