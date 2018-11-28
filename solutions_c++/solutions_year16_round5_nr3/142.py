#include <bits/stdc++.h>

using namespace std;

typedef pair<int,int> pii;

struct Point {
	int x, y, z;

	Point() {}
	Point(int _x, int _y, int _z):x(_x), y(_y), z(_z) {}
	Point operator+(const Point& b) const { return Point(x+b.x, y+b.y, z+b.z); }
	Point operator-(const Point& b) const { return Point(x-b.x, y-b.y, z-b.z); }

	double hypot() const { return sqrt(x*x + y*y + z*z); }
};

Point ast[1111];
int ufs[1111];
int ufs_find(int x) { return ufs[x] == x ? x : ufs[x] = ufs_find(ufs[x]); }
bool verify(int N, double dist)
{
	for(int i = 0;i < N;i++) ufs[i] = i;
	for(int i = 0;i < N;i++) {
		for(int j = 0;j < N;j++) {
			if (i == j) continue;
			if ((ast[i] - ast[j]).hypot() <= dist) {
				int fx = ufs_find(i);
				int fy = ufs_find(j);
				if (fx != fy) ufs[fx] = fy;
			}
		}
	}
	return ufs_find(0) == ufs_find(1);
}

int main(void)
{
	int TK = 0;
	int T = 0;
	scanf("%d", &T);
	while (T--) {
		printf("Case #%d: ", ++TK);

		int N = 0;
		scanf("%d %*s", &N);

		for (int i = 0;i < N;i++) {
			scanf("%d %d %d %*d %*d %*d", &ast[i].x, &ast[i].y, &ast[i].z);
		}

		double l = 0;
		double r = 1e20;
		for (int _ = 0;_ < 233;_++) {
			double mid = (l + r) / 2;
			if (verify(N, mid)) {
				r = mid;
			} else {
				l = mid;
			}
		}
		printf("%.9g\n", l);
	}
	return 0;
}
