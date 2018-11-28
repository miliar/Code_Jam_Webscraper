#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include<vector>
#include<string>
#include<algorithm>
#include<cstdio>
#include<numeric>
#include<cstring>
#include<ctime>
#include<cstdlib>
#include<set>
#include<map>
#include<unordered_map>
#include<unordered_set>
#include<list>
#include<cmath>
#include<bitset>
#include<cassert>
#include<queue>
#include<stack>
#include<deque>
#include<cassert>
using namespace std;
typedef long long ll;
typedef long double ld;
int x[5007], y[5007], z[5007];
double d[5007];
bool used[5007];
double dist(int u, int v)
{
	double dx = x[u] - x[v], dy = y[u] - y[v], dz = z[u] - z[v];
	return sqrt(dx*dx + dy*dy + dz*dz);
}
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int tt = 1; tt <= t; tt++)
	{
		int n, s;
		scanf("%d %d", &n, &s);
		for (int i = 0; i <= n; i++)
		{
			d[i] = (ld)1e10;
			used[i] = false;
		}
		for (int i = 0; i < n; i++)
		{
			int vx, vy, vz;
			scanf("%d %d %d %d %d %d", &x[i], &y[i], &z[i], &vx, &vy, &vz);
		}
		d[0] = 0;
		for (int i = 0; i < n; i++)
		{
			int bestPos = -1;
			for (int j = 0; j < n; j++)
			{
				if (!used[j] && (bestPos == -1 || d[j] < d[bestPos]))
				{
					bestPos = j;
				}
			}
			int v = bestPos;
			used[v] = true;
			for (int j = 0; j < n; j++)
			{
				d[j] = min(d[j], max(d[v], dist(v, j)));
			}
		}
		printf("Case #%d: %.10lf\n", tt, d[1]);
	}
}