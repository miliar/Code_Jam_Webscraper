#include<stdio.h>
#include<math.h>
#include<algorithm>
using namespace std;

typedef struct Point {
	long long x, y;
	double rad;
	Point() {}
	Point(long long _x, long long _y):x(_x), y(_y) {
		rad = atan2(y, x);
	}
	bool operator<(const struct Point &a) const {
		return rad < a.rad;
	}
	Point operator-(const struct Point &a) const {
		return Point(x-a.x, y-a.y);
	}
} Point;

int nCase;
int N, ans[4096];
double PI = acos(-1);
Point P[4096], pp[8192];

inline long long cross(Point &a, Point &b) {
	return a.x*b.y - a.y*b.x;
}

inline int halfplane(Point *pp, int n) {
	if(n <= 2) return 0;
	sort(pp, pp+n);
	for(int i = 0; i < n; ++i) {
		pp[n+i] = pp[i];
	}
	int mn = n;
	for(int i = 0, j = 1; i < n; ++i) {
		while(j == i || cross(pp[i], pp[j]) > 0) ++j;
		if(j-i-1 < mn) mn = j-i-1;
	}
	return mn;
}

int main() {
	scanf("%d", &nCase);
	for(int casei = 1; casei <= nCase; ++casei) {
		scanf("%d", &N);
		for(int i = 0; i < N; ++i) {
			scanf("%lld %lld", &P[i].x, &P[i].y);
			P[i].rad = atan2(P[i].y, P[i].x);
		}
		printf("Case #%d:\n", casei);
		for(int i = 0; i < N; ++i) {
			for(int j = 0, k = 0; j < N; ++j) if(j != i) pp[k++] = P[j]-P[i];
			printf("%d\n", halfplane(pp, N-1));
		}
	}
}

