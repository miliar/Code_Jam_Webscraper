#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <vector>
#include <map>
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

int f(ll k) {
  if (k == 0) return 0;
  if (k % 2 == 1) return 1 + f (k/2);
  return 1 + f ((k-1)/2);  
}

ll pos(int n, ll k){
  ll x = f(k);
  ll res = 0;
  REP(i,n){
    res *= 2;
    if (i < x) res++;
  }
  return res;
}

ll pos2(int n, ll k){
  ll x = f(k);
  ll res = 0;
  REP(i,n){
    res *= 2;
    if (i >= x) res++;
  }
  return res;
}


int main(){
  int _cases; scanf("%d",&_cases);
  for(int _case=1;_case<=_cases;_case++){
    printf("Case #%d:",_case);
    ll n, p; scanf("%lld%lld",&n,&p);
    ll mn = (1LL<<n)-1LL;

    ll left = 0, right = mn+1;
    while (left != right) {
      ll mid =(left+right)/2;
      if (pos(n,mid) < p) left = mid + 1;
      else right = mid;
    }
    printf(" %lld", left-1);
    left = 0; right = mn+1;
    while (left != right) {
      ll mid =(left+right)/2;
      if (pos2(n,mn-mid) < p) left = mid + 1;
      else right = mid;
    }
    printf(" %lld\n", left-1);
  }
  return 0;
}
