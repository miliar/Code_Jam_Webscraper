#include<iostream>
#include <assert.h>
#include<cmath>
#include<algorithm>
#include<limits>
#include<vector>
#include<bitset>
#include<cstdlib>
#include<cstdio>
#include<cstring>
#include<map>

using namespace std;

#define REP(i,n) for(int i=0;i<n;i++)
#define FOR(i,FROM,n) for(int i=FROM;i<n;i++)
#define FORR(i,n) for(int i=n;i>=0;i--)
#define ll long long int
#define llu long long unsigned int
#define si(n) scanf("%d",&n)
#define sl(n) scanf("%lld",&n)
#define slu(n) scanf("%llu",&n)
#define sf(n) scanf("%f",&n)
#define sd(n) scanf("%lf",&n)
#define ss(n) scanf("%s",n)
#define sss(n, size) fgets(n, size, stdin)
#define PI pair<int,int>
#define F first
#define S second
#define MP make_pair
#define PB push_back
#define V(x) vector<x>

ll gcd(ll r0, ll r1)
{
    if(r0==0 || r1==0)
    return 1;

    if(r0<r1)
    return gcd(r1,r0);

    if(r0%r1==0)
    return r1;

    return gcd(r1,r0%r1);
}
ll findInverse(ll a, ll b)
{
    ll x[3];
    ll y[3];
    ll quotient  = a / b;
    ll remainder = a % b;
    x[0] = 0;
    y[0] = 1;
    x[1] = 1;
    y[1] = quotient * -1;

    ll i = 2;
    for (; (b % (a%b)) != 0; i++)
    {
        a = b;
        b = remainder;
        quotient = a / b;
        remainder = a % b;
        x[i % 3] = (quotient * -1 * x[(i - 1) % 3]) + x[(i - 2) % 3];
        y[i % 3] = (quotient * -1 * y[(i - 1) % 3]) + y[(i - 2) % 3];
    }
    //x[i — 1 % 3] is inverse of a
    //y[i — 1 % 3] is inverse of b
    return x[(i - 1) % 3];
}

int t,n,m,k;

/*
bool myfunction(data i,data j)    //use it to sort vectors
{
    if( i.x < j.x ) return true;
    if( j.x < i.x ) return false;
    return j.y > i.y;
}
*/
int a[100000];
ll fact[20];

int get() {
  int ret = 0, at = 0;
  REP(i, n) {
    REP(j, m) {
      if (a[at] == 0) {
        at++;
        continue;
      }
      if (j < m-1) {
        if (a[at+1] == 1) {
          ret++;
        }
      }
      if (i < n-1) {
        if (a[at+m] == 1) {
          ret++;
        }
      }
      at++;
    }
  }
  return ret;
}

int main() {

  fact[0] = 1;
  FOR(i, 1, 20) {
    fact[i] = fact[i-1]*i;
  }

  si(t);
  REP(prob, t) {
    si(n);
    si(m);
    si(k);
    int l = n*m;
    REP(i, l) {
      a[i] = 0;
    }
    REP(i, k) {
      a[i] = 1;
    }
    ll cnt = fact[l]/fact[k]/fact[l-k];
    int ans = 10000000;
    while(cnt) {
      cnt--;
      ans = min(ans, get());
      next_permutation(a, a+l);
    }
    printf("Case #%d: %d\n", prob+1, ans);
  }

  //system("pause");
  return 0;
}
