#include<iostream>
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

int t,n;

/*
bool myfunction(data i,data j)    //use it to sort vectors
{
    if( i.x < j.x ) return true;
    if( j.x < i.x ) return false;
    return j.y > i.y;
}
*/

int a[17];

int main() {

  si(t);
  int ans, ai, x;
  REP(prob, t) {
    memset(a,0,sizeof(a));
    si(x);
    x--;
    REP(i,4) {
      REP(j,4) {
        if (x == i) {
          si(n);
          a[n] = 1;
        } else {
          si(n);
        }
      }
    }
    si(x);
    x--;
    ai=0;
    REP(i,4) {
      REP(j,4) {
        if (i == x) {
          si(n);
          if (a[n]) {
            ai++;
            ans = n;
          }
        } else {
          si(n);
        }
      }
    }
    if (ai == 0) {
      printf("Case #%d: Volunteer cheated!\n", prob+1);
    } else if (ai > 1) {
      printf("Case #%d: Bad magician!\n", prob+1);
    } else {
      printf("Case #%d: %d\n", prob+1, ans);
    }
  }

  //system("pause");
  return 0;
}
