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

	set<double> nao, ken;
	
	int n;
	scanf("%d", &n);

	rep(i, 0, n)
	{
		double cur;
		scanf("%lf", &cur);
		nao.insert(cur);
	}

	rep(i, 0, n)
	{
		double cur;
		scanf("%lf", &cur);
		ken.insert(cur);
	}

	set<double> k2 = ken;

	int res1 = 0, res2 = 0;

	for (auto it = nao.begin(), itEnd = nao.end(); it != itEnd; it++)
	{
		double cv = *it;
		auto kit = ken.lower_bound(cv);

		if (kit == ken.end())
			res2++;
		else
			ken.erase(kit);
	}

	ken = k2;
	for (auto it = nao.begin(), itEnd = nao.end(), kit = ken.begin(); it != itEnd; it++)
	{
		double cv = *it;
		double kv = *kit;
		if (cv > kv)
		{
			res1++;
			kit++;
		}
	}

	//printf("\n");
	//for (auto it = nao.begin(), itEnd = nao.end(), kit = --ken.end(); it != itEnd; it++, kit--)
	//{
	//	printf("%lf ", *it);
	//}
	//printf("\n");
	//for (auto it = ken.begin(), itEnd = ken.end(), kit = --ken.end(); it != itEnd; it++, kit--)
	//{
	//	printf("%lf ", *it);
	//}
	//printf("\n");

	printf("%d %d\n", res1, res2);
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