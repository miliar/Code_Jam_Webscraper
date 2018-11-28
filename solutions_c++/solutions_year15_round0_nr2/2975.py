#include <cstdio>
#include <iostream>
#include <cmath>
#include <string>
#include <cstring>
#include <cctype>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <stack>
#include <queue>
#include <map>
#include <set>
#define For(i,N) for(int i=0; i<N; i++)
#define Fore(i,C) for(__typeof((C).begin()) i =(C).begin(); i != (C).end(); ++i)
#define FOR(i,j,k) for(int i=j; i<k; i++)
#define Fors(i,s) for(int i=0; s[i]; i++)
#define pb push_back
#define mp make_pair
#define ff first
#define ss second

typedef long long ll;
typedef long double ld;
using namespace std;

int n;
vector<int> v;

int cas(int cas_jedenia){
  int poc=0;
  For(i,n) if(v[i] > cas_jedenia) poc += (v[i] / cas_jedenia) - (v[i]%cas_jedenia==0);
  //printf("%d %d\n", cas_jedenia, poc+cas_jedenia);
  return poc+cas_jedenia;
}

void spocitaj(){
  scanf(" %d", &n);
  v.clear(); v.resize(n);
  For(i,n) scanf(" %d", &v[i]);
  sort(v.begin(), v.end());
  int res = v.back();
  
  FOR(i,1,v.back()) res = min(res, cas(i));
 
  printf("%d\n",res);
}

int main(){
  int T;
  scanf(" %d", &T);
  For(t,T){
    printf("Case #%d: ",t+1);
    spocitaj();
  }
  return 0;
}