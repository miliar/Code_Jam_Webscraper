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
int main()
{
   int t; cin>>t;
   int a[107][107];
   FORC(u, 1, t)
   {
      int m, n; cin>>m>>n;
      FOR(i, 0, m) FOR(j, 0, n) cin>>a[i][j];
      bool yes = true;
      FOR(i, 0, m) FOR(j, 0, n)
      {
	 bool check1 = true;
	 FOR(k, 0, m) if(a[k][j] > a[i][j]) check1 = false;
	 bool check2 = true;
	 FOR(k, 0, n) if(a[i][k] > a[i][j]) check2 = false;
	 if(!check1 and !check2) yes = false;
      }
      if(yes) printf("Case #%d: YES\n", u);
      else printf("Case #%d: NO\n", u);
   }
}