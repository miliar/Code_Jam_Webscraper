#include <algorithm>
#include <iostream>
#include <cstdlib>
#include <cassert>
#include <string>
#include <vector>
#include <cstdio>
#include <set>
#include <map>
#include <queue>
#include <memory.h>
#include <cmath>

using namespace std;

#define forn(i, n) for (int i = 0; i < (int)n; i++)
#define fore(i, b, e) for (int i = (int)b; i <= (int)e; i++)
#define all(x) (x).begin(), (x).end()
#define se second
#define fi first
#define mp make_pair
#define pb push_back
#define op operator
typedef vector <int> vi;
typedef pair<int, int> pii;
typedef long long i64;

int edges[1000][26];
string s[10];
int best, counter, n, m;
int a[10];

void go(int step)
{
	if (step == n)
	{
		int nnew = 0;
		bool fail = false;
		forn(server, m)
		{
			int cnt = 1;
			forn(j, 26)
				edges[0][j] = 0;
			if (a[0] == 0 && a[1] == 1 && a[2] == 2 && a[3] == 3)
			{
				int hhh = 0;
			}
			forn(j, n)
				if (a[j] == server)
				{
					int cur = 0;
					forn(pos, s[j].length())
					{
						int tmp = s[j][pos] - 'A';
						if (edges[cur][tmp] != 0)
						{
							cur = edges[cur][tmp];
						}
						else
						{
							cnt++;
							forn(h, 26)
								edges[cnt][h] = 0;
							edges[cur][tmp] = cnt;
							cur = cnt;
						}
					}
				}
			nnew += cnt;
			if (cnt == 1)
			{
				fail = true;
				break;
			}
		}
		if (fail)
			return;
		if (best == nnew)
			counter++;
		else if (nnew > best)
		{
			best = nnew;
			counter = 1;
		}
		return;
	}
	forn(t, m)
	{
		a[step] = t;
		go(step + 1);
	}
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tests;
	scanf("%d", &tests);
	fore(test, 1, tests)
	{
		printf("Case #%d: ", test);
		scanf("%d%d", &n, &m);
		forn(j, n)
			cin >> s[j];
		best = -1;
		counter = 0;
		go(0);
		printf("%d %d\n", best, counter);
		fprintf(stderr, "test %d done\n", test);
	}

	return 0;
}