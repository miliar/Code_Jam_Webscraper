#include <iostream>
#include <iomanip>
#include <cstdio>
#include <bitset>
#include <memory>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <list>
#include <string>
#include <cstring>
#include <fstream>
#include <functional>
#include <stack>
#include <complex>
#include <wchar.h>
#include <wctype.h>
#include <cmath>
#include <queue>
#include <ctime>
#include <numeric>

using namespace std;

template<typename T> T mabs(const T &a){ return a<0 ? -a : a; }
#define rep(x,y,z) for(int x=(y),e##x=(z);x<e##x;x++)
#define SQR(x) ((x)*(x))
#define all(c) (c).begin(), (c).end()

typedef long long ll;
typedef long double ld;
typedef unsigned long long ull;
typedef unsigned int ui;
typedef short int si;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef pair<ll, int> pli;
typedef pair<int, ll> pil;

ll arr[1000005];

ll sums[1000005];

ll getSum(int l, int r)
{
	return sums[r] - sums[l - 1];
}

void test(int ti)
{
	printf("Case #%d: ", ti);

	int n;
	ll p, q, r, s;
	scanf("%d%lld%lld%lld%lld", &n, &p, &q, &r, &s);

	ll total = 0;
	rep(i, 0, n)
	{
		arr[i] = ((i * p + q) % r + s);
		total += arr[i];
	}

	sums[0] = 0;

	//rep(i, 0, n)
	//{
	//	sums[i + 1] = sums[i] + arr[i + 1];
	//}

	ll minRes = 0, maxRes = total + 1;

	ll bestRes = 0;

	while (minRes <= maxRes)
	{
		ll mid = (maxRes + minRes) / 2;

		ll lSum = 0, lBnd = 0, rSum = 0, rBnd = n - 1;

		while (lBnd < n)
		{
			if (lSum + arr[lBnd] <= mid)
			{
				lSum += arr[lBnd];
				lBnd++;
			}
			else
				break;
		}

		while (rBnd >= lBnd)
		{
			if (rSum + arr[rBnd] <= mid)
			{
				rSum += arr[rBnd];
				rBnd--;
			}
			else
				break;
		}
		ll midSum = 0;
		rep(i, lBnd, rBnd + 1)
		{
			midSum += arr[i];
		}

		if (midSum > mid)
		{
			minRes = mid + 1;
		}
		else
		{
			bestRes = mid;
			maxRes = mid - 1;
		}
	}

	ll arnar = total - bestRes;

	double res = arnar / double(total);

	printf("%.10lf\n", res);
}

void run()
{
	int tc;
	scanf("%d", &tc);

	rep(i, 0, tc)
	{
		test(i + 1);
	}
}

//#define prob "fence"

int main()
{
#ifdef LOCAL_DEBUG
	freopen("test.in", "r", stdin);
	freopen("test.out", "w", stdout);
	time_t st = clock();
#else 
#ifdef prob
	freopen(prob".in", "r", stdin);
	freopen(prob".out", "w", stdout);
#endif
#endif

	run();

#ifdef LOCAL_DEBUG
	fprintf(stderr, "\n=============\n");
	fprintf(stderr, "Time: %.2lf sec\n", (clock() - st) / double(CLOCKS_PER_SEC));
#endif

	return 0;
}