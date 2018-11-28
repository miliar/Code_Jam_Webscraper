#include<iostream>
#include<vector>
#include<algorithm>
#define rep(x,n) for (int x = 0; x < n; x++)
#define pb push_back
#define H 2
#define MH -1
using namespace std;
 vector < vector < int > > V;
 vector < int > MaxCols, MaxRows;
 int n,m;
 bool Check()
 {
  rep(x,n)
  {
    rep(y,m)
    {
     if (V[x][y] < MaxCols[y] && V[x][y] < MaxRows[x]) return false;
    }
  }
  return true;
 }
int main()
{
 int t; cin >> t; int a;

 rep(x,t)
 {
  V.clear(); MaxCols.clear(); MaxRows.clear();
  cin >> n >> m; V.resize(n); MaxCols.resize(m,MH); MaxRows.resize(n,MH);
  rep(y,n)
  {
   rep(z,m)
   {
    cin >> a; V[y].pb(a);
    MaxCols[z] = max(MaxCols[z],a);
    MaxRows[y] = max(MaxRows[y],a);
   }
  }
  cout << "Case #" << x+1 << ": ";
  if (Check()) cout << "YES\n"; else cout << "NO\n";
 }
 return 0;
}
