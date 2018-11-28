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

const int maxn = 1e4 + 5;

int n, sz;
int a[maxn];
bool mark[maxn];

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tests;
	scanf("%d", &tests);
	fore(test, 1, tests)
	{
		printf("Case #%d: ", test);
		scanf("%d%d", &n, &sz);
		forn(j, n)
			scanf("%d", &a[j]);
		sort(a, a + n);
		int answer = 0;
		forn(j, n)
			mark[j] = false;
		for (int cur = n - 1; cur >= 0; cur--)
		{
			if (mark[cur])
				continue;
			answer++;
			for (int an = cur - 1; an >= 0; an--)
			{
				if (!mark[an] && a[an] + a[cur] <= sz)
				{
					mark[an] = true;
					break;
				}
			}
		}
		printf("%d\n", answer);
		fprintf(stderr, "test %d done\n", test);
	}

	return 0;
}