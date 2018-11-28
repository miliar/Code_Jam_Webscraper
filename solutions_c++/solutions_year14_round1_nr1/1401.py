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

int a[11][11];
int b[11][11];

void solve()
{
	int n, l;
	cin >> n >> l;
	for(int i = 1; i <= n; i++)
	{
		for(int j = 1; j <= l; j++)
			scanf("%1d", &a[i][j]);
	}

	for(int i = 1; i <= n; i++)
	{
		for(int j = 1; j <= l; j++)
			scanf("%1d", &b[i][j]);
	}

	/*for(int i = 1; i <= n; i++)
	{
		for(int j = 1; j <= l; j++)
			cout << a[i][j];
		cout << ' ';
	}
	cout << endl;

	for(int i = 1; i <= n; i++)
	{
		for(int j = 1; j <= l; j++)
			cout << b[i][j];
		cout << ' ';
	}
	cout << endl;*/

	int ans = INF;
	for(int mask = 0; mask < (1 << l); mask++)
	{
		int cntbit = 0;
		for(int i = 0; i < l; i++)
			if(mask & (1 << i))
			{
				cntbit++;
				for(int j = 1; j <= n; j++)
					a[j][l - i] = 1 - a[j][l - i];
			}

		bool ok = true;
		for(int i = 1; i <= n; i++)
		{
			bool can = false;
			for(int j = 1; j <= n; j++)
			{
				bool good = true;
				for(int k = 1; k <= l; k++)
					if(b[i][k] != a[j][k])
						good = false;
				if(good)
					can = true;
			}
			
			if(!can)
				ok = false;
		}

		if(ok)
			ans = min(ans, cntbit);

		for(int i = 0; i < l; i++)
			if(mask & (1 << i))
			{
				cntbit++;
				for(int j = 1; j <= n; j++)
					a[j][l - i] = 1 - a[j][l - i];
			}
	}

	if(ans == INF)
		cout << "NOT POSSIBLE" << endl;
	else
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