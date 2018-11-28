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

bool isPal(ll n) {
  int a[20];
  int sz=0;
  while(n!=0){
    a[sz++] = n % 10;
    n /= 10;
  }
  REP(i,sz) if (a[i] != a[sz-i-1]) return false;
  return true;
}

vector<ll> adm;

int main(){
  for (ll i = 1; i*i<=1000000000000000LL; i++)
    if (isPal(i) && isPal(i*i)) adm.push_back(i*i);
  int _cases; scanf("%d",&_cases);
  for(int _case=1;_case<=_cases;_case++){
    printf("Case #%d:",_case);
    ll a,b;scanf("%lld%lld",&a,&b);
    int res=0;
    REP(i,(int)adm.size())
      if(adm[i] >= a && adm[i] <= b) res++;
    printf(" %d\n", res);
  }
  return 0;
}
