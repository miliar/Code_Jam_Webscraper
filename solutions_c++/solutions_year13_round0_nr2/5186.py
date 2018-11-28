#include <stdio.h>
#include <vector>
#include <map>
#include <string>
#include <algorithm>
#include <memory.h>
#include <cassert>
#include <set>
#include <queue>
#include <deque>
#include <iostream>
#include <math.h>

using namespace std;

#define mp make_pair
#define pb push_back
#define _(a, b) memset(a, b, sizeof(a))

typedef long long lint;
typedef unsigned long long ull;

const int INF = 1000000000;
const lint LINF = 4000000000000000000ll;

void prepare()
{
#ifdef LOLWUT
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#else
#endif
}

int testNumber = 0;

int n, m;
int field[105][105];
bool canv[2][105], canh[2][105];

set< pair< int, pair<int, int> > > ds;
vector< pair<int, int> > pos;

bool solve()
{
	ds.clear();

	scanf("%d%d", &n, &m);
	for (int i = 0; i < n; i++)
		for (int j = 0; j < m; j++)
		{
			scanf("%d", &field[i][j]);
			ds.insert( mp(-field[i][j], mp(i, j)) );
		}

	printf("Case #%d: ", ++testNumber);

	int cur = 0, next = 1;
	_(canv, 1);
	_(canh, 1);

	while (!ds.empty())
	{
		int h = ds.begin()->first;
		pos.clear();

		while (ds.begin()->first == h)
		{
			pos.pb(ds.begin()->second);
			ds.erase(ds.begin());
		}
		
		for (int k = 0; k < pos.size(); k++)
		{
			if (!canv[cur][pos[k].second] && !canh[cur][pos[k].first])
			{
				printf("NO\n");
				return false;
			}

			canv[next][pos[k].second] = false;
			canh[next][pos[k].first] = false;
		}

		swap(cur, next);
	}

	printf("YES\n");
	return false;
}

int main()
{
	prepare();
	int tn;
	for (scanf("%d", &tn); tn; tn--)
	{
		solve();
	}
	return 0;
}