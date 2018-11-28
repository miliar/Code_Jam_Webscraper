/*
	Author:USETC_elfness
*/
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cmath>
#include<vector>
#include<string>
#include<algorithm>
#include<iostream>
typedef long long LL;
const int V=1100000;
const int P=1000000007;
using namespace std;
int set[V], cnt[V];
int find(int x)
{
	if(x != set[x]) set[x] = find(set[x]);
	return set[x];
}
void U(int x, int y)
{
	int px = find(x);
	set[px] = y;
}
struct Node{int id, s;}q[V];
bool cmp(Node x, Node y)
{return x.s < y.s;}
int l[V], r[V], vis[V], p[V];
void dfs(int u)
{
	if(vis[u])return;
	vis[u] = 1;
	dfs(p[u]);
	l[u] = max(l[u], l[p[u]]);
	r[u] = min(r[u], r[p[u]]);
}
int n, D, S, A, C, R;
int s[V];
int main()
{
	freopen("A.in", "r", stdin);
	freopen("AL.out", "w", stdout);
	int _;
	scanf("%d", &_);
	for(int ca = 1; ca <= _; ++ca)
	{
		scanf("%d%d", &n, &D);
		scanf("%d%d%d%d", &S, &A, &C, &R);
		q[0].s = S;
		for(int i = 1; i < n; ++i)
		q[i].s = ((LL)q[i - 1].s * A + C) % R;
		for(int i = 0; i < n; ++i)q[i].id = i;
		scanf("%d%d%d%d", &S, &A, &C, &R);
		cerr <<ca <<endl;
		p[0] = S;
		for(int i = 1; i < n; ++i)
		p[i] = ((LL)p[i - 1] * A + C) % R;
		for(int i = 1; i < n; ++i) p[i] %= i;
		sort(q, q + n, cmp);
		int pos = 0;
		for(int i = 0; i < n; ++i)
		{
			l[q[i].id] = i;
			while(pos + 1 < n &&q[pos + 1].s - q[i].s<=D)
			pos++;
			r[q[i].id] = pos;
		}
		memset(vis,0,sizeof(vis));
		vis[0]=1;
		for(int i = 0; i < n; ++i)
		dfs(i);
		memset(s, 0, sizeof(s));
		for(int i = 0; i < n; ++i)
		if(r[i]>=l[i])s[l[i]]++, s[r[i] + 1]--;
		for(int i = 0; i <=n ;++i)
		s[i] += s[i - 1];
		int ret = 0;
		for(int i = 0; i <=n; ++i) ret = max(ret, s[i]);
		printf("Case #%d: %d\n", ca, ret);
	}
	return 0;
}
