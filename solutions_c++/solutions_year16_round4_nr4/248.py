#include <bits/stdc++.h>
using namespace std;
const int MAXN = 15;
string adj[MAXN];
bool vis[MAXN];
vector <int> G[MAXN];
int pairs[MAXN];
bool kuhn(int v)
{
	if(vis[v])
		return false;
	vis[v] = true;
	for (int i = 0; i < G[v].size(); ++i)
	{
		int to = G[v][i];
		if(pairs[to] == -1 || kuhn(pairs[to]))
		{
			pairs[to] = v;
			return true;
		}
	}
	return false;
}
bool is_ok(int mask, int n)
{
	vector < vector <int> > A(n, vector <int> (n,0));
	for (int i = 0; i < n*n; ++i)
		if(mask & (1<<i))
			A[i/n][i%n] = 1;
	// cout<<mask<<":\n";
	for (int j = 0; j < n; ++j)
	{
		bool found = false;
		for (int i = 0; i < n; ++i)
		{
			if(A[i][j])
				found = true;
		}
		if(!found)
			return false;
	}
	// for (int i = 0; i < n; ++i)
	// {
	// 	for (int j = 0; j < n; ++j)
	// 		cout<<A[i][j]<<" ";
	// 	cout<<"\n";
	// }
	for (int i = 0; i < n; ++i)
	{
		// cleanup
		for (int j = 0; j < n; ++j)
			G[j].clear();
		// check if i is ok
		// cout<<"check "<<i<<"\n";
		for (int j = 0; j < n; ++j)
		{
			if(j == i)
				continue;
			for (int k = 0; k < n; ++k)
			{
				if(A[i][k] && A[j][k])
					G[j].push_back(k);
			}
		}
		// for (int j = 0; j < n; ++j)
		// {
		// 	cout<<j<<": ";
		// 	for (int k = 0; k < G[j].size(); ++k)
		// 	{
		// 		cout<<G[j][k]<<" ";
		// 	}
		// 	cout<<"\n";
		// }
		memset(pairs, -1, sizeof pairs);
		for (int j = 0; j < n; ++j)
		{
			memset(vis, false, sizeof vis);
			kuhn(j);
		}
		int match = 0, ctr = 0;
		for (int j = 0; j < n; ++j)
		{
			if(pairs[j] != -1)
				match++;
			if(A[i][j])
				ctr++;
		}
		// cout<<match<<" "<<ctr<<"\n";
		assert(match <= ctr);
		if(match == ctr)
			return false;
	}
	return true;
}
int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	int t;
	cin>>t;
	for (int tc = 1; tc <= t; ++tc)
	{
		int n;
		cin>>n;
		for (int i = 0; i < n; ++i)
			cin>>adj[i];
		int curr = 0, ans = (1<<(n*n))-1;
		for (int i = 0; i < n; ++i)
			for (int j = 0; j < n; ++j)
				if(adj[i][j] == '1')
					curr|=(1<<(n*i + j));
		for (int mask = 0; mask < (1<<(n*n)); ++mask)
		{
			if(	(mask & curr) == curr
				&& __builtin_popcount(mask) < __builtin_popcount(ans)
				&& is_ok(mask,n))
					ans = mask;
		}
		cout<<"Case #"<<tc<<": "<<__builtin_popcount(ans) - __builtin_popcount(curr)<<"\n";
	}
	return 0;
}