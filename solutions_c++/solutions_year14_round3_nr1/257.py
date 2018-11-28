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
using namespace std;

ll gcd(ll a, ll b){
  if(b > a) return gcd(b,a);
  if(b==0) return a;
  return gcd(b, a%b);
}

int T;
ll P,Q;
char c;

int main(){
  scanf(" %d", &T);
  For(t,T){
    scanf(" %lld%c%lld",&P,&c,&Q);
    ll g = gcd(P,Q);
    P /= g;
    Q /= g;
    
    ll gen = 0;
    while(Q > P){ P*=2LL; gen++; }
    
    while (Q%2LL == 0LL) Q/=2LL;
    
    if(Q != 1LL)
      printf("Case #%d: impossible\n",t+1);
    else
      printf("Case #%d: %lld\n", t+1, gen);
  }
  return 0;
}