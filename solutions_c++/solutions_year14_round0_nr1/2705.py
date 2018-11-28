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

const int maxn = 4;

int a[maxn][maxn];
int b[maxn][maxn];

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tests;
	scanf("%d", &tests);
	fore(test, 1, tests)
	{
		int first, second;
		scanf("%d", &first);
		first--;
		forn(i, 4)
			forn(j, 4)
				scanf("%d", &a[i][j]);
		scanf("%d", &second);
		second--;
		forn(i, 4)
			forn(j, 4)
				scanf("%d", &b[i][j]);
		int cnt = 0;
		int ans;
		forn(choice, 4)
		{
			bool f = false;
			forn(an, 4)
				if (b[second][an] == a[first][choice])
				{
					f = true;
					break;
				}
			if (f)
			{
				cnt++;
				ans = a[first][choice];
			}
		}
		printf("Case #%d: ", test);
		if (cnt == 0)
			printf("Volunteer cheated!\n");
		else if (cnt > 1)
			printf("Bad magician!\n");
		else printf("%d\n", ans);
	}
	return 0;
}