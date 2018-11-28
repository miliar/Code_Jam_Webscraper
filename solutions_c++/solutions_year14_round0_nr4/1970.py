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

int a[1000],b[1000],p[5]={1,10,100,1000,10000},ai[1000],bi[1000];

int get() {
  char s[10];
  ss(s);
  int ans = 0;
  int cnt = 0;
  for(int i=2;s[i]!='\0';i++) {
    ans*=10;
    ans+=(s[i]-'0');
    cnt++;
  }
  ans *=p[5-cnt];
  return ans;
}

int main() {

  si(t);
  REP(prob, t) {
    si(n);
    REP(i,n) {
      a[i] = get();
    }
    REP(i,n) {
      b[i] = get();
    }
    sort(a,a+n);
    sort(b,b+n);
    int ans2=0, ans1=0;
    REP(i,n) {
      bi[i]=0;
    }
    REP(i,n) {
      int done = 0;
      REP(j,n) {
        if (bi[j] == 0 && b[j]>a[i]) {
          done = 1;
          bi[j] = 1;
          break;
        }
      }
      if (!done) {
        ans2++;
      }
    }
    int l1=0,l2=0;
    while(n--) {
      if(a[l1]>b[l2]) {
        l1++;
        l2++;
        ans1++;
      } else {
        l1++;
      }
    }
    printf("Case #%d: %d %d\n", prob+1, ans1, ans2);
  }

  //system("pause");
  return 0;
}
