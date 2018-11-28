#include <bits/stdc++.h>
using namespace std;
const int MAXN = 1005;
int x[MAXN], y[MAXN], z[MAXN], vx[MAXN], vy[MAXN], vz[MAXN], par[MAXN];
bool adj[MAXN][MAXN];
inline long double get_dist(int i, int j)
{
	return sqrtl(powl(x[i]-x[j],2) + powl(y[i]-y[j],2) + powl(z[i]-z[j],2));
}
void make_adj(int n, long double max_edge)
{
	for (int i = 0; i < n; ++i)
	{
		adj[i][i] = false;
		for (int j = i+1; j < n; ++j)
		{
			if(get_dist(i,j) <= max_edge)
			{
				adj[i][j] = adj[j][i] = true;
			}
			else
			{
				adj[i][j] = adj[j][i] = false;
			}
		}
	}
}
int parent(int pos)
{
	if(par[pos] != pos)
		par[pos] = parent(par[pos]);
	return par[pos];
}
int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	cout.precision(9);
	int t;
	cin>>t;
	for (int tc = 1; tc <= t; ++tc)
	{
		int n,s;
		cin>>n>>s;
		for (int i = 0; i < n; ++i)
		{
			cin>>x[i]>>y[i]>>z[i]>>vx[i]>>vy[i]>>vz[i];
		}
		long double lo = 0.0, hi = get_dist(0,1);
		for (int ii = 0; ii < 200; ++ii)
		{
			long double mid = (lo + hi)/2.0;
			make_adj(n,mid);
			for (int i = 0; i < n; ++i)
				par[i] = i;
			for (int i = 0; i < n; ++i)
			{
				for (int j = 0; j < n; ++j)
				{
					if(adj[i][j])
					{
						int u = parent(i), v = parent(j);
						par[u] = v;
					}
				}
			}
			if(parent(0) == parent(1))
				hi = mid;
			else
				lo = mid;
		}
		double ans = (lo + hi)/2.0;
		cout<<"Case #"<<tc<<": "<<fixed<<ans<<"\n";
	}
	return 0;
}