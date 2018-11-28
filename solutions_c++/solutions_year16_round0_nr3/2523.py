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

int t,n;

/*
bool myfunction(data i,data j)    //use it to sort vectors
{
    if( i.x < j.x ) return true;
    if( j.x < i.x ) return false;
    return j.y > i.y;
}
*/

const int till = 33333333;
int a[33333333], d[20], p[3000000], pi = 0;
int ai = 0;

struct Ans {
  char dig[20];
  int div[11];
};

Ans ans[100];

int check(ll at) {
  int sr = sqrt(at);
  REP(i, pi) {
    if (p[i] > sr) {
      break;
    }
    if (at % p[i] == 0) {
      return p[i];
    }
  }
  return 0;
}

int main() {

  si(t);
  memset(a, 1, sizeof(a));
  FOR(i, 2, till) {
    if (a[i] != 0) {
      p[pi] = i;
      pi++;
      ll at = i;
      at *= at;
      while (at < till) {
         a[at] = 0;
         at += i;
      }
    }
  }
  //cout<<pi<<endl;

  int j;
  REP(prob, t) {
    si(n);
    si(j);
    int dig = n-2;
    int tries = 1<<(dig);
    int at = 0;
    while(ai < j && at < tries) {
      int x = at;
      REP(i, dig) {
        d[i] = x%2;
        x /= 2;
      }
      at++;
      ll num = 1;
      int flag = 1;
      Ans temp;
      FOR(base, 2, 11) {
        num = 1;
        REP(i,dig) {
          num *= base;
          num += d[i];
        }
        num *= base;
        num += 1;
        int div = check(num);
        if (div == 0) {
          flag = 0;
          break;
        }
        temp.div[base] = div;
      }
      if (flag) {
        temp.dig[0] = '1';
        REP(i, dig) {
          temp.dig[i+1] = d[i] + '0';
        }
        temp.dig[n-1] = '1';
        temp.dig[n] = '\0';
        ans[ai] = temp;
        ai++;
      }
    }
    printf("Case #%d:\n", prob+1);
    REP(i, j) {
      printf("%s ", ans[i].dig);
      FOR (base, 2, 11) {
        printf("%d ", ans[i].div[base]);
      }
      printf("\n");
    }
  }

  //system("pause");
  return 0;
}
