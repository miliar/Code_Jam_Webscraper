#include <cstdio>
#include <algorithm>
#include <cmath>
#define N 105
#define eps 1e-9
#define fi(a, b, c) for(int a = (b); a < (c); a++)
#define fd(a, b, c) for(int a = (b); a > (c); a--)
#define FI(a, b, c) for(int a = (b); a <= (c); a++)
#define FD(a, b, c) for(int a = (b); a >= (c); a--)
#define fe(a, b, c) for(int a = (b); a; a = c[a])
using namespace std;

int t, n;
double x, y, z, a[N], b[N], c[N], w[N], ans;

bool equal(double x, double y){
	return fabs(x - y) < eps;
}

void solve(int tt){
	scanf("%d %lf %lf", &n, &x, &y);
	z = x * y;
	fi(i, 0, n){
		scanf("%lf %lf", &a[i], &b[i]);
		c[i] = a[i] * b[i];
	}
	
	if(n > 1){
		if(equal(b[0], b[1])){
			if(equal(b[0], y)) ans = x / (a[0] + a[1]);
			else ans = -1;
		}else if(y > min(b[0], b[1]) - eps && y < max(b[0], b[1]) + eps){
			w[0] = (c[1] * x - a[1] * z) / (a[0] * c[1] - a[1] * c[0]);
			w[1] = (-c[0] * x + a[0] * z) / (a[0] * c[1] - a[1] * c[0]);
			ans = max(w[0], w[1]);
		}else ans = -1;
	}else{
		if(equal(b[0], y)) ans = x / a[0];
		else ans = -1;
	}
	
	printf("Case #%d: ", tt);
	if(ans < -eps) puts("IMPOSSIBLE");
	else printf("%.8lf\n", ans);
}

int main(){
	freopen("B-small-attempt6.in", "r", stdin);
	freopen("B-small-attempt6.out", "w+", stdout);
	scanf("%d", &t);
	FI(z, 1, t) solve(z);
	scanf("\n");
}
