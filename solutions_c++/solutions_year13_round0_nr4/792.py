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

int n, k;

int st[205];
int cur[205];
int lock[205];
int chest[205][205];

int used[2000000];
int q[2000000], qs, qe;

bool solve()
{
	printf("Case #%d: ", ++testNumber);

	_(q, 0); qs = 0; qe = 0;

	for (int i = 0; i < 2000000; i++)
		used[i] = -1;

	_(st, 0);
	_(lock, 0);
	_(chest, 0);

	scanf("%d%d", &k, &n);
	for (int i = 0; i < k; i++)
	{
		int a;
		scanf("%d", &a);
		a--;
		st[a]++;
	}

	for (int i = 0; i < n; i++)
	{
		scanf("%d", &lock[i]); lock[i]--;
		int k;
		scanf("%d", &k);
		for (int j = 0; j < k; j++)
		{
			int a;
			scanf("%d", &a);
			a--;
			chest[i][a]++;
		}
	}
	
	used[0] = 0;
	q[qe++] = 0;
	while (qs != qe)
	{
		int x = q[qs++];

		memcpy(cur, st, sizeof(st));
		int xx = x, xi = 0;
		while (xx)
		{
			if (xx & 1)
			{
				cur[lock[xi]]--;
				for (int i = 0; i < 200; i++)
					cur[i] += chest[xi][i];
			}

			xx >>= 1;
			xi++;
		}

		xx = x;
		for (xi = 0; xi < n; xi++)
		{
			if ((xx & 1) == 0 && cur[lock[xi]])
			{
				int ni = x | (1 << xi);
				if (used[ni] == -1)
				{
					used[ni] = xi;
					q[qe++] = ni;
				}
			}

			xx >>= 1;
		}
	}

	if (used[(1 << n) - 1] == -1)
	{
		printf("IMPOSSIBLE\n");
	}
	else
	{
		vector<int> ans;

		int mask = (1 << n) - 1;
		while (mask != 0)
		{
			int x = used[mask];
			ans.pb(x + 1);
			mask ^= (1 << x);
		}

		reverse(ans.begin(), ans.end());
		for (int i = 0; i < ans.size(); i++)
			printf("%d ", ans[i]);

		printf("\n");
	}

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