#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
#include <vector>
#include <set>
#include <queue>
#include <map>
#include <stack>
#include <cstdlib>
#include <algorithm>
#include <list>
#include <cassert>
#include <ctime>
#include <sstream>
#include <cmath>
#include <unordered_map>
#include <unordered_set>
#include <iomanip>
using namespace std;

#define sc(x) scanf("%d", &x)
#define sc2(x, y) scanf("%d%d", &x, &y)
#define sc_str(s) scanf("%s", s)
#define pr(x) printf("%d ", x)
#define nl() printf("\n")
#define mp(x, y) make_pair(x, y)
#define forn(i, a, b) for(int i=a; i<b; ++i)
#define ford(i, a, b) for(int i=b-1; i>=a; --i)
#define pb(x) push_back(x)
#define sz(x) (int)x.size()
#define X first
#define Y second

typedef long long ll;
typedef long double ld;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef vector<int> vi;
typedef vector<vector<int> > vvi;
typedef vector<bool> vb;
typedef vector<vector<bool> > vvb;

double ans = 0;

int n, k;

void solve()
{
	int t;
	sc(t);
	forn(tt, 0, t)
	{
		sc2(n, k);
		vector<double> p(n + 1);
		forn(i, 0, n)
			cin >> p[i];
		ans = 0;
		for (int mask = 0; mask < (1 << n); ++mask)
		{
			vector<int> v;
			for (int i = 0; i < n; ++i)
				if (mask & (1 << i))
					v.push_back(i);
			if(v.size()==k)
			{
				double total = 0;
				for (int mask2 = 0; mask2 < (1 << k); ++mask2)
				{
					double prob=1, cnt1 = 0, cnt2 = 0;
					for (int i = 0; i < k; ++i)
					{
						if (mask2 & (1 << i))
						{
							cnt1++;
							prob *= p[v[i]];
						}
						else
						{
							cnt2++;
							prob *= (1 - p[v[i]]);
						}
					}
					if (cnt1 == cnt2)
						total += prob;
				}
				ans = max(ans, total);
			}
		}

		
		printf("Case #%d: %.10f\n", tt + 1, ans);
	}
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	solve();
#ifdef _DEBUG
	fprintf(stderr, "Time: %.2lf\n", (double)clock() / CLOCKS_PER_SEC);
#endif

	return 0;
}