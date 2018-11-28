#include<bits/stdc++.h>

using namespace std;
#define For(i,l,r) for (int i = l; i <= r; ++i)
#define Cor(i,l,r) for (int i = l; i >= r; --i)
#define UPD(a,b) { a = (a + (b)) % MD; }

struct Point {
	double x, y, z;
	Point(double x = 0, double y = 0, double z = 0) : x(x), y(y), z(z) {}
	Point operator - (const Point &b) const { return Point(x - b.x, y - b.y, z - b.z); }
	double len() {
		return sqrt(x * x + y * y + z * z); 
	}
}A[1111], velo[1111];

int n;
double s;
int vis[1111], q[1111];
bool check(double r) {
	memset(vis, 0, sizeof vis);
	int hd = 0, tl = 1;
	vis[q[1] = 1] = true;
	while (hd < tl) {
		int x = q[++hd];
		For(i,1,n) if ((A[i] - A[x]).len() <= r && !vis[i]) {
			//printf("%d %d %.12f\n", i, x, (A[i] - A[x]).len());
			vis[q[++tl] = i] = true;
		}
	}
	return vis[2];
}

int main() {
	int T; cin >> T;
	For(TK,1,T) {
		cin >> n >> s;
		For(i,1,n) {
			scanf("%lf%lf%lf", &A[i].x, &A[i].y, &A[i].z);
			scanf("%lf%lf%lf", &velo[i].x, &velo[i].y, &velo[i].z);
		}
		double l = 0, r = 100000000;
		For(TIME,1,50) {
			double mid = (l + r) / 2.0;
			if (check(mid)) r = mid; else l = mid;
		}
		printf("Case #%d: %.12f\n", TK, l);
	}
	return 0;
}
