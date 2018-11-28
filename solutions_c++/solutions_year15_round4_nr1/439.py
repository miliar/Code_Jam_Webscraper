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

void init() {

}

int dy[] = { -1, 0, 1, 0 };
int dx[] = { 0, -1, 0, 1 };
char arr[] = { '<', '^', '>', 'v' };

int arrToD(char let) {
	rep(i, 0, 4) {
		if (arr[i] == let)
			return i;
	}
	return -1;
}

char bd[500][500];
int w, h;
bool hasArr(int x, int y, int dir) {
	x += dx[dir], y += dy[dir];
	while (1) {
		if (x < 0 || y < 0 || x >= h || y >= w)
			return false;
		if (bd[x][y] != '.')
			return true;
		x += dx[dir], y += dy[dir];
	}
}

void test() {
	scanf("%d%d", &h, &w);
	rep(i, 0, h) {
		scanf("%s", bd[i]);
	}

	int cnt = 0;
	rep(i, 0, h) {
		rep(j, 0, w) {
			int ad = arrToD(bd[i][j]);
			if (ad == -1)
				continue;
			if (hasArr(i, j, ad))
				continue;
			bool good = false;
			rep(k, 0, 4) {
				if (hasArr(i, j, k)) {
					good = true;
					break;
				}
			}
			if (!good) {
				cnt = -1;
				break;
			}
			cnt++;
		}
		if (cnt == -1)
			break;
	}
	if (cnt == -1) {
		printf("IMPOSSIBLE\n");
	}
	else {
		printf("%d\n", cnt);
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