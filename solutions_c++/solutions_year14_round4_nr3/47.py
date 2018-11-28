#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <cassert>
#include <cstdlib>
#include <ctime>

using namespace std;
typedef long long int64;
#ifdef HOME
	#define E(c) cerr<<#c
	#define Eo(x) cerr<<#x<<" = "<<(x)<<endl
	#define Ef(...) fprintf(stderr, __VA_ARGS__)
#else
	#define E(c) ((void)0)
	#define Eo(x) ((void)0)
	#define Ef(...) ((void)0)
#endif

const int SIZE = 1024;

int IntervDist(int l1, int r1, int l2, int r2) {
	if (r1 <= l2)
		return l2 - r1;
	if (r2 <= l1)
		return l1 - r2;
	return 0;
}
int Distance(int *a, int *b) {
	int dx = IntervDist(a[0], a[2], b[0], b[2]);
	int dy = IntervDist(a[1], a[3], b[1], b[3]);
	return max(dx, dy);
}

int w, h, b;
int rect[SIZE][4];
int n;

int64 dist[SIZE];
bool used[SIZE];

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tests;
	scanf("%d", &tests);
	for (int tt = 1; tt<=tests; tt++) {
		scanf("%d%d%d", &w, &h, &b);
		for (int i = 0; i<b; i++) {
			for (int j = 0; j<4; j++)
				scanf("%d", &rect[i][j]);
			rect[i][2]++;
			rect[i][3]++;
		}

		rect[b][0] = rect[b][2] = 0;
		rect[b][1] = 0;
		rect[b][3] = h;
		rect[b+1][0] = rect[b+1][2] = w;
		rect[b+1][1] = 0;
		rect[b+1][3] = h;
		n = b + 2;

		memset(dist, 63, sizeof(dist));
		memset(used, false, sizeof(used));
		dist[b] = 0;
		while (1) {
			int best = -1;
			int64 minDist = 1000000000;
			for (int i = 0; i < n; i++) if (!used[i])
				if (minDist > dist[i]) {
					minDist = dist[i];
					best = i;
				}

			if (best < 0)
				break;
			used[best] = true;

			for (int i = 0; i<n; i++) {
				int64 nd = dist[best] + Distance(rect[best], rect[i]);
				if (nd < dist[i])
					dist[i] = nd;
			}
		}

		int ans = dist[b+1];

		printf("Case #%d: %d\n", tt, ans);
		fflush(stdout);
	}
	return 0;
}
