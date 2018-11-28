#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
using namespace std;

#define LL long long
int target;

struct poi {
	LL x, y;
	poi () {x = y = 0;}
	poi (LL _x, LL _y) {x = _x; y = _y;}
}p[4096];

int quad(poi a) {
	if (a.x > 0 && a.y >= 0) return 1;
	if (a.y > 0 && a.x <= 0) return 2;
	if (a.x < 0 && a.y <= 0) return 3;
	if (a.y < 0 && a.x >= 0) return 4;
	return 0;
}

poi operator + (poi a, poi b) {
	return poi(a.x + b.x, a.y + b.y);
}

poi operator - (poi a, poi b) {
	return poi(a.x - b.x, a.y - b.y);
}

LL dot (poi a, poi b) {
	return a.x * b.x + a.y * b.y;
}

LL cross (poi a, poi b) {
	return a.x * b.y - a.y * b.x;
}

int T;
int n;
int id[8192];

bool cmp(int a, int b) {
	int ta = quad(p[a] - p[target]);
	int tb = quad(p[b] - p[target]);
	if (ta != tb) return ta < tb;
	return cross(p[a] - p[target], p[b] - p[target]) > 0;
}

int main() {
	scanf("%d", &T);
	for (int test = 1; test <= T; ++test) {
		printf("Case #%d:\n", test);
		scanf("%d", &n);
		for (int i = 0; i < n; ++i) {
			scanf("%lld %lld", &p[i].x, &p[i].y);
		}
		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < n - 1; j++)
				if (j < i) id[j] = j;
				else id[j] = j + 1;
			target = i;
			sort(id, id + n - 1, cmp);
			for (int j = n - 1; j < n * 2 - 2; ++j)
				id[j] = id[j - n + 1];
			int now = 0;
			int ans = 1;
			for (int j = 0; j < n - 1; ++j) {
				while (now < j + n - 2 && cross(p[id[j]] - p[i], p[id[now + 1]] - p[i]) >= 0)
					now ++;
				if ((now - j + 2) > ans) ans = now - j + 2;
			}
			printf("%d\n", n - ans);
		}
	}
	return 0;
}