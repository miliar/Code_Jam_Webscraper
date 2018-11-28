#include<stdio.h>
#include<algorithm>
#include<string.h>
#include<map>
#include<set>
#include<vector>
#include<iostream>
#include<iomanip>
#define REP(i,n) for(int i=0; i<n; i++)
#define FOR(i,n) for(int i=1; i<=n; i++)

typedef long long LL;
using namespace std;

#define N 110
int n;
long double V,C;
struct A{
  long double v,c;
  const bool operator<(const A &rhs)const{
    return c>rhs.c;
  }
}a[N];
bool check(long double t){
  long double tot=0;
  FOR(i,n)tot+=a[i].v*t;
  if(tot<V)return false;
  
  tot=0;
  long double rem=V;
  for(int i=1; i<=n && rem>1e-10; i++){
    tot+=min(rem,a[i].v*t)*a[i].c;
    rem-=min(rem,a[i].v*t);
  }
  if(C-tot/V>1e-10)return false;
  
  rem=V;
  tot=0;
  for(int i=n; i>=1 && rem>1e-10; i--){
    tot+=min(rem,a[i].v*t)*a[i].c;
    rem-=min(rem,a[i].v*t);
  }
  if(tot/V-C>1e-10)return false;
  
  return true;
}
int main(){
#ifdef QWERTIER
  freopen("b.in","r",stdin);
  freopen("b.out","w",stdout);
#endif 
  int T;
  scanf("%d",&T);
  
  FOR(kase,T){
    printf("Case #%d: ",kase);
    cin>>n>>V>>C;
    FOR(i,n){
      cin>>a[i].v>>a[i].c;
    }
    sort(a+1,a+n+1);
    long double lo=0,hi=1e9;
    while(hi-lo>1e-10){
      long double mi=(lo+hi)/2;
      if(check(mi))hi=mi;
      else lo=mi;
    }
    if(lo>1e8)
      puts("IMPOSSIBLE");
    else{
      double ans=lo;
      cout<<fixed<<setprecision(10)<<ans<<endl;
    }
  }
  return 0;
}
