//ITNOG
#include<bits/stdc++.h>

using namespace std;

//#define int long long
#define rep(i, s, e) for(int i = s; i < e; i ++)
typedef long double ld;

const int maxN = 100+5;
const int mod = 1000*1000*1000 + 7;

vector<pair<int,int> > v;
char a[maxN][maxN];
int px, py;
int dis[100*100][100*100];


void solve()
{
    int n,m; cin >> n >> m;
    rep(i,0,n) rep(j,0,m) cin >> a[i][j];
    
    int te = 0;
    rep(i,0,n) rep(j,0,m)
    {
	  if(a[i][j] == '.') continue;
	  int bes = -1;
	  rep(k,0,n) if(k != i && a[k][j] != '.')
	  {
		if(k < i && a[i][j] == '^') { bes = 1; break; }
		if(k > i && a[i][j] == 'v') { bes = 1; break; }
		bes = 0;
	  }
	  
	  rep(k,0,m) if(k != j && a[i][k] != '.')
	  {
		if(bes == 1) break;
		if(k < j && a[i][j] == '<') { bes = 1; break; }
		if(k > j && a[i][j] == '>') { bes = 1; break; }
		bes = 0;
	  }
	  if(bes == -1) { cout << "IMPOSSIBLE" << endl; return; }
	  if(bes == 0) te ++;
    }
    cout << te << endl;
}


main()
{
//    ios::sync_with_stdio(0); cin.tie();
    int T; cin >> T;
    rep(i,1,T+1)
    {
	  printf("Case #%d: ", i);
	  solve();
    }
    return 0;
}
