#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <set>
#include <queue>
#include <deque>
#include <map>
#include <stack>
#include <string>
#include <ctime>

using namespace std;

#define rep(x, y, z) for(int x = (y), end##x = (z); x < end##x; x++)
#define all(x) (x).begin(),(x).end()

#ifdef LOCAL_DEBUG

#define DebugPrint(...) fprintf(stderr, __VA_ARGS__);

#else

#define DebugPrint(...)

#endif

typedef long long ll;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef pair<pll, ll> plll;

void test(int testNum);
void init();

int main()
{
	//
#ifdef LOCAL_DEBUG

	freopen("test.in", "r", stdin);
	freopen("test.out", "w", stdout);

#else

	//freopen("test.in", "r", stdin);
	//freopen("test.out", "w", stdout);

#endif

	clock_t cl = clock();

	init();

	int tc;
	scanf("%d", &tc);

	rep(i, 0, tc)
		test(i+1);

#ifdef LOCAL_DEBUG

	fprintf(stderr, "\nTime used: %lf\n", (clock() - cl) / (double)CLOCKS_PER_SEC);

#endif

	return 0;
}

void init()
{

}

int N;

ll getVal(ll e, ll o)
{
	int n = N;
	ll t = o - e;
	ll cs = (n + n - t + 1) * t / 2;
	return cs;
}

void test(int testNum)
{
	printf("Case #%d: ", testNum);
	vector<plll> entries;

	stack<pll> cards;

	int n, m;

	scanf("%d%d", &n, &m);

	N = n;

	ll normSum = 0, badSum = 0;

	rep (i, 0, m)
	{
		int e, o, p;
		scanf("%d%d%d", &e, &o, &p);

		normSum += getVal(e, o) * p;

		entries.push_back(plll(pll(e, 0), p));
		entries.push_back(plll(pll(o, 1), p));
	}

	sort(all(entries));

	rep(i, 0, 2*m)
	{
		if (entries[i].first.second == 0)
		{
			cards.push(pll(entries[i].first.first, entries[i].second));
		}
		else
		{
			ll left = entries[i].second;
			while (left > 0)
			{
				pll last = cards.top();
				cards.pop();
				ll cur = min(last.second, left);
				last.second -= cur;
				left -= cur;
				if (last.second > 0)
					cards.push(last);

				ll curAdd = getVal(last.first, entries[i].first.first);
				curAdd *= cur;

				badSum += curAdd;
			}
		}
	}

	ll diff = normSum - badSum;
	printf("%lld\n", diff);
}