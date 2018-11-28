#pragma comment(linker, "/STACK:167177216")

#include <stdio.h>
#include <stack>
#include <math.h>
#include <iostream>
#include <algorithm>
#include <string.h>
#include <string>
#include <memory.h>
#include <vector>
#include <map>
#include <queue>
#include <set>
#include <time.h>
#include <cassert>
using namespace std;

#define mp make_pair
#define pb push_back
#define pii pair<int, int>
#define forn(i, n) for(int i = 0; i < (int)(n); i++)
#define x first
#define y second

typedef long long li;
typedef long double ld;
typedef unsigned long long uli;

const int INF = 1e9;
const ld eps = 1e-9;
const li mod = INF + 7;
const li INF64 = (li)(INF) * (li)(INF);

const int ddx[] = {-1, 1, 1, -1};
const int ddy[] = {1, 1, -1, -1};
const int dx[] = {-1, -1, 0, 1, 1, 1, 0, -1};
const int dy[] = {0, 1, 1, 1, 0, -1, -1, -1};
const int dx4[] = {-1, 0, 1, 0};
const int dy4[] = {0, 1, 0, -1};
const int dxh[] = {-1, -1, -1, 1, 1, 1, 1, -1};
const int dyh[] = {1, -1, -1, -1, -1, 1, 1, 1};
const string dirs[] = {"RIGHT", "UP", "LEFT", "DOWN"};

vector<int> g[16];
bool used[16];

void solve()
{
	int n;
	cin >> n;
	for(int i = 1; i <= n; i++)
		g[i].clear(), used[i] = false;
	for(int i = 1; i < n; i++)
	{
		int a, b;
		cin >> a >> b;
		g[a].pb(b);
		g[b].pb(a);
	}

	int ans = INF;
	for(int mask = 0; mask < (1 << n); mask++)
	{
		for(int i = 1; i <= n; i++)
			used[i] = false;
		int cntbit = 0;
		forn(i, n)
			if(mask & (1 << i))
				cntbit++, used[n - i] = true;
		queue<int> q;
		int idx = 0;
		forn(i, n)
			if(!(mask & (1 << i)))
			{
				used[n - i] = true;
				q.push(n - i);
				idx = i;
				//cout << "idx == " << i << endl;
				break;
			}

		while(!q.empty())
		{
			int v = q.front();
			q.pop();
			forn(i, g[v].size())
			{
				int to = g[v][i];
				if(!used[to])
				{
					q.push(to);
					used[to] = true;
				}
			}
		}

		//cout << "WTF666" << endl;
		bool good = true;
		for(int i = 1; i <= n; i++)
			if(!used[i])
			{
				//cout <<"del == " << i << endl;
				good = false;
			}
		if(!good)
			continue;

		forn(i, n)
			if(mask & (1 << i))
				used[n - i] = true;
			else
				used[n - i] = false;

		//cout << "WTF" << endl;
		bool ok = false;
		for(int root = 1; root <= n; root++)
			if(!used[root])
			{
				bool u[16];
				for(int i = 1; i <= n; i++)
					u[i] = used[i];
				queue<int> Q;
				Q.push(root);
				u[root] = true;
				bool can = true;
				while(!Q.empty())
				{
					int v = Q.front();
					Q.pop();
					int cnt = 0;
					forn(i, g[v].size())
					{
						int to = g[v][i];
						if(!u[to])
						{
							cnt++;
							u[to] = true;
							Q.push(to);
						}
					}

					if(cnt != 0 && cnt != 2)
					{
						can = false;
						break;
					}
				}

				if(can)
				{
					ok = true;
					break;
				}
			}

			if(ok)
				ans = min(ans, cntbit);
	}

	cout << ans << endl;
}

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    //ios_base::sync_with_stdio(false);
	int tests;
	cin >> tests;
	forn(test, tests)
	{
		cout << "Case #" << test + 1 << ": ";
		solve();
	}
    return 0;
}