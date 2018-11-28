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

int t;
ll n;

/*
bool myfunction(data i,data j)    //use it to sort vectors
{
    if( i.x < j.x ) return true;
    if( j.x < i.x ) return false;
    return j.y > i.y;
}
*/

int a[1000001], d[100];

ll rev(ll x) {
  ll ret = 0;
  while(x) {
    int rem = x%10;
    x/=10;
    ret *= 10;
    ret += rem;
  }
  return ret;
}

int dig(ll x) {
  int at = 0;
  while(x) {
    d[at] = x%10;
    x/=10;
    at++;
  }
  return at;
}

int MAX = 10000;
int sub[] = {0, 1, 10, 100, 100, 1000, 1000, 10000, 10000, 100000, 100000, 1000000, 1000000, 10000000, 10000000};

int main() {

  a[0] = 1;
  a[1] = 1;
  FOR(i, 2, MAX) {
    a[i] = a[i-1];
    int r = rev(i);
    if (r < i && i%10 != 0 && a[i] > a[r]) {
      a[i] = a[r];
    }
    a[i]++;
  }

  si(t);
  REP(prob, t) {
    sl(n);
    int l = dig(n);
    ll ans = 0;
    if (n < MAX) {
       printf("Case #%d: %d\n", prob+1, a[n]);
       continue;
    }
    if (l == 15) {
      ans++;
      n--;
      l = dig(n);
    }
    ll at = n;
    dig(at);
    while(at >= MAX) {
      ll start = at % sub[l];
      ans += start;
      ll next = at-start+1;
      ll r = rev(next);
      if (next > at && next != r) {
        r = at-sub[l]+1;
        ans += (sub[l]-1);
      } else if (next == r) {
        ans--;
        r -= sub[l-1];
        ans += sub[l-1];
      }
      at = r;
      l = dig(at);
    }
    ans += a[at];
    printf("Case #%d: %lld\n", prob+1, ans);
  }

  //system("pause");
  return 0;
}
