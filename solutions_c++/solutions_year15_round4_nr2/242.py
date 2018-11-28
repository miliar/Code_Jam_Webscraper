#include<cstring>
#include<cstdio>
#include<cmath>
#include<vector>
#include<algorithm>
using namespace std;
long double eps(1e-12);
const int N(111);
long double r[N], c[N];
__inline long double sign(const long double & x) {
	return (x > eps) - (x + eps < 0);
}
struct Point {
	double x, y;
	Point(const long double & x, const long double & y) : x(x), y(y) {
	}
};
__inline long double operator * (const Point & a, const Point & b) {
	return a.x * b.y - a.y * b.x;
}
__inline Point operator + (const Point & a, const Point & b) {
	return Point(a.x + b.x, a.y + b.y);
}
__inline bool operator < (const Point & a, const Point & b) {
	return a.y < b.y;
}
int main() {
	int tst;
	scanf("%d", &tst);
	for(int qq(1); qq <= tst; qq++) {
		int n;
		long double v, x;
		double v1, x1;
		scanf("%d%lf%lf", &n, &v1, &x1);
		v = v1; x = x1;
		for(int i(0); i < n; i++) {
			double rr, cc;
			scanf("%lf%lf", &rr, &cc);
			r[i] = rr; c[i] = cc;
		}
	//	printf("%d %f %f\n", n, v, x);
	//	for(int i(0); i < n; i++) {
	//		printf("%f %f\n", r[i], c[i]);
	//	}
		long double le(0), ri(1e10);
		for(int i(0); i < 300; i++) {
			long double mid((le + ri) / 2);
			static vector<Point> vec;
			vec.clear();
			for(int j(0); j < n; j++) {
				vec.push_back(Point(r[j], c[j]));
			}
			sort(vec.begin(), vec.end());
			long double low(0), high(0);
			long double cap(0);
			bool flag1(false);
			for(int j(0); j < n && sign(cap - v) < 0; j++) {
				long double tmp(min(v - cap, mid * vec[j].x));
				low = (low * cap + tmp * vec[j].y) / (cap + tmp);
				cap += tmp;
			}
			flag1 = sign(v - cap) == 0;
			cap = 0;
			bool flag2(false);
			reverse(vec.begin(), vec.end());
			for(int j(0); j < n && sign(cap - v) < 0; j++) {
				long double tmp(min(v - cap, mid * vec[j].x));
				high = (high * cap + tmp * vec[j].y) / (cap + tmp);
				cap += tmp;
			}
			flag2 = sign(v - cap) == 0;
			//printf("%d %d %f %f %f %f %f %f\n", flag1, flag2, low, x, high, le, mid, ri);
			if(flag1 && flag2 && sign(low - x) <= 0 && sign(high - x) >= 0) {
				ri = mid;
			}else {
				le = mid;
			}
		}
		printf("Case #%d: ", qq);
		if(le > 9e9) {
			printf("IMPOSSIBLE\n");
		}else {
			printf("%.10f\n", (double)(le + ri) / 2);
		}
	}
}
