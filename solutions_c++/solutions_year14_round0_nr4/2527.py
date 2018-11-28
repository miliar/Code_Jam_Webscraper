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

const int maxn = 1005;
const double eps = 1.0e-8;

double a[maxn];
double b[maxn];
int n;
bool used[maxn];

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tests;
	scanf("%d", &tests);
	fore(test, 1, tests)
	{
		scanf("%d", &n);
		forn(i, n)
			scanf("%lf", &b[i]);
		sort(b, b + n);
		forn(i, n)
			scanf("%lf", &a[i]);
		sort(a, a + n);
		int not_opt = 0;
		memset(used, 0, sizeof(used));
		forn(cur, n)
		{
			int lesser = -1;
			int more = -1;
			forn(choice, n) if (!used[choice])
				if (b[cur] - a[choice] > eps)
				{
					lesser = choice;
					break;
				}
			forn(choice, n) if (!used[choice])
				if (a[choice] - b[cur] > eps)
				{
					more = choice;
					break;
				}
			if (more != -1)
			{
				used[more] = true;
			}
			else
			{
				assert(lesser != -1);
				used[lesser] = true;
				not_opt++;
			}
		}
		int p = n - 1;
		int opt = 0;
		for (int cur = n - 1; cur >= 0; cur--)
		{
			while(p != -1 &&  a[p] - b[cur] > eps)
				p--;
			if (p != -1)
			{
				opt++;
				p--;
			}
		}
		assert(opt >= not_opt);
		printf("Case #%d: %d %d\n", test, opt, not_opt);
	}

	return 0;
}