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

void test(int TC)
{
	printf("Case #%d: ", TC);
	
	double c, f, x;
	scanf("%lf%lf%lf", &c, &f, &x);

	double curProd = 2;
	double curCook = 0;
	double timePassed = 0;

	double res = 0.0;
	if (c > x)
		res = x / curProd;
	else
	{
		while (1)
		{
			double timeNeed = c / curProd;
			res += timeNeed;
			double time1 = (x - c) / curProd;
			double time2 = x / (curProd + f);
			if (time1 < time2)
			{
				res += time1;
				break;
			}
			else
			{
				curProd += f;
			}
		}
	}

	printf("%.9lf\n", res);
}

void run()
{
	int tc;
	scanf("%d", &tc);

	rep(i, 1, tc + 1)
	{
		test(i);
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