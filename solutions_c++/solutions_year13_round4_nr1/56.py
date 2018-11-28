#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <vector>
#include <map>
#include <queue>
#include <utility>
#include <set>
#include <algorithm>
#include <iostream>
#include <sstream>

using namespace std;

#define CLEAR(X) memset(X,0,sizeof(X))
#define REP(i,n) for(int i=0;i<(n);i++) 
template <class T> vector<T>parse(string s,const char d=' '){
  vector<T> v; string p; s+=d; int i=0; 
  while(i<(int)s.size())
    if (s[i] == d){stringstream u; u<<p; T t; u>>t; v.push_back(t); p=""; while(i<(int)s.size() && s[i]==d)i++;} else p+=s[i++];   
  return v;
} 

typedef long long ll;
typedef long double ld;

struct E{
  ll pos, plus;
  bool start;
};

ll MOD = 1000002013;

bool cmp(const E &a, const E &b){
  if (a.pos != b.pos) return a.pos < b.pos;
  return a.start > b.start;
}

int main(){
  int _cases; scanf("%d",&_cases);
  for(int _case=1;_case<=_cases;_case++){
    printf("Case #%d:",_case);
    ll n,m;scanf("%lld%lld",&n,&m);
    ll normal=0;
    vector<E> e;
    REP(i,m){
      ll from,to,c;
      scanf("%lld%lld%lld",&from,&to,&c);
      ll k = to - from;
      normal += (c * ((k * n - (k*(k-1))/2)%MOD))%MOD;
      normal %= MOD;
      normal += MOD;
      normal %= MOD;
      E a;a.pos = from; a.plus = c; a.start = true; e.push_back(a);      
      E b;b.pos = to; b.plus = c; b.start = false; e.push_back(b);
    } 
    sort(e.begin(),e.end(),cmp);
    ll stack[2010];
    ll stackp[2010];
    int top = 0;
    ll cost = 0;
    REP(i,(int)e.size()) {
      if (e[i].start) {
        stack[top] = e[i].plus;
        stackp[top] = e[i].pos;
        top++;
      } else {
        ll rem = e[i].plus;
        while (rem > 0) {
//          printf("%d %d %lld %lld\n",top,i,n,m);fflush(stdout);
          ll k = e[i].pos - stackp[top-1], p;
          if (stack[top-1] > rem) {
            p = rem;            
            stack[top-1] -= rem;
            rem = 0;
          } else {
            p = stack[top-1];
            rem -= stack[--top];
          }
          cost += (p * ((k * n - (k*(k-1))/2) % MOD))%MOD;  
          cost %= MOD;
          cost += MOD;
          cost %= MOD;
        }
      }
    }
    ll dif = (normal-cost)%MOD;
    dif+=MOD;
    dif%=MOD;
    printf(" %lld\n", dif);
  }  
  return 0;
}
