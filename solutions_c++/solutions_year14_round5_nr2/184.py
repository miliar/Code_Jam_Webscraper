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

int hp[105];

int needToShoot[105];
int towerShoot[105][2];

int dyn[105][505][505];
int n;

int gold[105];

int getDyn(int cur, int shd, int sht)
{
	if (cur >= n)
		return 0;
	int &cv = dyn[cur][shd][sht];

	if (cv != -1)
		return cv;

	int res = 0;
	{//skips
		int next = getDyn(cur + 1, shd, sht + towerShoot[cur][0]);
		res = next;
	}
	{//kills
		int dShoots = shd + needToShoot[cur];
		int tShoots = sht + towerShoot[cur][1];
		if (dShoots <= tShoots + 1)
		{
			int curVal = getDyn(cur + 1, dShoots, tShoots);
			curVal += gold[cur];
			res = max(res, curVal);
		}
	}
	cv = res;
	return cv;
}

void test(int ti)
{
	int p, q, n;
	scanf("%d%d%d", &p, &q, &n);
	//p = rand() % 19 + 1; q = rand() % 19 + 1; n = 100;
	printf("Case #%d: ", ti);
	::n = n;
	rep(i, 0, n)
	{
		scanf("%d%d", hp + i, gold + i);
		//hp[i] = 100 + rand() % 101;
		//gold[i] = rand();
		int chp = hp[i];
		needToShoot[i] = 0;
		while (1)
		{
			needToShoot[i]++;
			if ((chp - 1) % q < p)
			{
				towerShoot[i][1] = (chp - 1) / q;
				break;
			}
			chp -= p;
		}
		towerShoot[i][0] = (hp[i] + q - 1) / q;
	}

	memset(dyn, -1, sizeof(dyn));

	int res = getDyn(0, 0, 0);

	printf("%d\n", res);
}

void run()
{
	int tc;
	scanf("%d", &tc);

	rep(i, 0, tc)
	{
		fprintf(stderr, "TT %d\n", i);
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