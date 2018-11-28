#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cassert>
#include <cstdio>

#define REP(i,n) for(int i=0; i<(n); ++i)
#define FOR(i,p,k) for(int i=(p); i<=(k); ++i)

typedef long long LL;

std::vector<LL> A;

bool go(LL s)
{
  int l = 0, h = A.size()-1;
  while(l<h)
  {
    int m = (l+h+1)/2;
    if(A[m]>s) h = m-1; else l = m;
  }
  if(A[l]>s) return 0;
  int ll = l; h = A.size()-1;
  while(ll<h)
  {
    int m = (ll+h+1)/2;
    if(A[m]>s+A[l]) h = m-1; else ll = m;
  }
  //printf("s=%lld l1=%d l2=%d\n",s,l,ll);
  return A.back()<=s+A[ll];
}

int main()
{
  int t; std::cin >> t;
  FOR(_,1,t)
  {
    int n,p,q,r,s; scanf("%d%d%d%d%d",&n,&p,&q,&r,&s);
    A.resize(n);
    REP(i,n){ A[i] = (LL(i)*p+q)%r+s; if(i) A[i] += A[i-1]; }
    //if(n<100) REP(i,n) printf("%lld ",A[i]); puts("");
    LL l = 0, h = A.back();
    while(l<h)
    {
      LL m = (l+h)/2;
      if(go(m)) h = m; else l = m+1;
    }
    printf("Case #%d: %.11lf\n",_,double(A.back()-l)/A.back());
  }
  return 0;
}
