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
#include <unordered_map>
#include <unordered_set>

using namespace std;

template<typename T> T mabs(const T &a) { return a<0 ? -a : a; }
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
typedef pair<double, double> pdd;

const double EPS = 1e-8;

void init() {

}

void test() {
	int n;
	double v, x;
	scanf("%d %lf %lf", &n, &v, &x);

	double ri[150], ti[150];
	vector<pdd> h, c;
	double totalRate = 0.0;
	rep(i, 0, n) {
		scanf("%lf %lf", ri + i, ti + i);
		if (mabs(ti[i] - x) < EPS) {
			totalRate += ri[i];
		}
		else if (ti[i] < x) {
			c.push_back({ x - ti[i], ri[i] });
		}
		else {
			h.push_back({ ti[i] - x, ri[i] });
		}
	}

	sort(all(h));
	sort(all(c));
	//reverse(all(h));
	//reverse(all(c));
	int curH = 0, curC = 0;
	double curHUsed = 0, curCUsed = 0;

	while (1) {
		if (curH >= h.size() || curC >= c.size())
			break;
		double curHLeft = h[curH].second - curHUsed, curCLeft = c[curC].second - curCUsed;
		double hTemp = h[curH].first, cTemp = c[curC].first;
		double prop = cTemp / hTemp;
		if (curHLeft > prop * curCLeft) {
			curHLeft -= prop * curCLeft;
			totalRate += curCLeft * (prop + 1);
			curC++;
			curCUsed = 0;
		}
		else {
			curCLeft -= curHLeft / prop;
			totalRate += curHLeft + curHLeft / prop;
			curH++;
			curHUsed = 0;
		}
	}

	if (totalRate < EPS) {
		printf("IMPOSSIBLE\n");
	}
	else {
		double res = v / totalRate;
		printf("%.12lf\n", res);
	}
}

void run()
{
	init();
	int tc;
	scanf("%d", &tc);
	rep(i, 0, tc) {
		printf("Case #%d: ", i + 1);
		test();
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