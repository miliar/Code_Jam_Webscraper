#include<iostream>
#include<algorithm>
#include<iomanip>
#include<map>
#include<set>
#include<vector>
#include<queue>
#include<deque>
#include<cctype>
#include<cstdio>
#include<cstring>
#include<cmath>
#include<stack>
#include<sstream>
using namespace std;
#define FOR(i, a, b) for(int i=a; i<b; ++i)
#define FORC(i, a, b) for(int i=a; i<=b; ++i)
#define FORD(i, a, b) for(int i=a-1; i>=b; --i)
#define FORDC(i, a, b) for(int i=a; i>=b; --i)
#define endl '\n'
#define pb push_back
#define size(v) (int)((v).size())
#define all(v) (v).begin(), (v).end()
#define DREP(v) sort(all(v)); v.erase(unique(all(v)), (v).end())
#define F first
#define S second
#define mp make_pair
#define VI vector<int>
#define index(a, val) (lower_bound(all(a), val)-(a).begin())
#define iter(i, c) for(typeof((c).begin()) i=(c).begin(); i!=(c).end(); ++i)
#define PII pair<int, int>
#define ll long long
#define ini(arr, val) memset(arr, val, sizeof(arr))
#define debug(a) cerr<<"DEBUG: "<<#a<<" = "<<a<<endl
#define deb debug("gauss")
bool palin(ll n)
{
   stringstream s; s<<n;
   string a = s.str();
   int sz = size(a);
   FOR(i, 0, sz) if(a[i] != a[sz-i-1]) return false;
   return true;
}
ll concat(ll u)
{
   ll copy = u;
   while(copy)
   {
      u *= 10;
      u += copy%10;
      copy /= 10;
   }
   return u;
}
ll concat2(ll u, ll dig)
{
   ll copy = u;
   u *= 10; u += dig;
   while(copy)
   {
      u *= 10;
      u += copy%10;
      copy /= 10;
   }
   return u;
}
int main()
{
   vector<ll> v; v.reserve(100000);
   v.pb(1); v.pb(4); v.pb(9);
   for(long long i = 1; i<100000; ++i)
   {
      ll b = concat(i);
      if(b>10000000) break;
      if(palin(b*b)) v.pb(b*b);
      for(ll j = 0; j<10; ++j)
      {
	 b = concat2(i, j);
	 if(palin(b*b)) v.pb(b*b);
      }
   }
   sort(all(v));
   int t; cin>>t;
   FORC(u, 1, t)
   {
      ll a, b; cin>>a>>b;
      int yes1 = index(v, a), yes2 = index(v, b);
      int ans = yes2 - yes1 + ((v[yes2] == b)?(1):(0));
      printf("Case #%d: %d\n", u, ans);
   }
}