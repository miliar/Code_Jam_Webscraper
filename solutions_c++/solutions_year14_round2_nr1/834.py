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

char s[100][1000];
int cnt[100],si[100],at[100];

int calc() {
  int ans=0;
  memset(at,0,sizeof(at));
  
  while(true) {
    int f = 0;
    REP(i,n) {
      if (at[i] == si[i]) {
        f++;
      }
    }
    if (f == n) {
      break;
    }
    char c = s[0][at[0]];
    int max = 0;
    REP(i,n) {
      cnt[i]=0;
      while(at[i] != si[i] && s[i][at[i]] == c) {
        at[i]++;
        cnt[i]++;
      }
      if (cnt[i]>max) {
        max = cnt[i];
      }
    }
    int mini = 10000;
    FOR(i,1,max+1) {
      int x = 0;
      REP(j,n) {
        x += abs(cnt[j]-i);
      }
      if (x<mini) {
        mini = x;
      }
    }
    ans += mini;
  }
  return ans;
}

int main() {

  si(t);
  REP(prob, t) {
    si(n);
    REP(i,n) {
      ss(s[i]);
    }
    REP(i,n) {
      si[i]=0;
      while(s[i][si[i]]!='\0') {
        si[i]++;
      }
    }
    memset(at,0,sizeof(at));
    int flag = 0;
    while(true) {
      int f = 0;
      REP(i,n) {
        if (at[i] == si[i]) {
          f++;
        }
      }
      if (f == n) {
        break;
      }
      if (f!=0) {
        flag=1;
        break;
      }
      FOR(i,1,n) {
        if (s[i][at[i]] != s[0][at[0]]) {
          flag = 1;
          break;
        }
      }
      if (flag) {
        break;
      }
      char c = s[0][at[0]];
      REP(i,n) {
        while(at[i] != si[i] && s[i][at[i]] == c) {
          at[i]++;
        }
      }
    }
    if (flag) {
      printf("Case #%d: Fegla Won\n", prob+1);
      continue;
    }
    printf("Case #%d: %d\n", prob+1, calc());
  }

  //system("pause");
  return 0;
}
