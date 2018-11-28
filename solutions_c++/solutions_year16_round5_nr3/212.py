#include <cstdio>
#include <cstring>
#include <cmath>
using namespace std;
#define N 1111
int x[N], y[N], z[N], vx[N], vy[N], vz[N];
int n, S;
int f[N];

int sqr(int x){
	return x * x;
}

int getf(int x){
	return f[x] == x ? x : getf(f[x]);
}

int ok(int L){
	for (int i = 0; i < n; ++ i){
		f[i] = i;
	}
	for (int i = 0; i < n; ++ i){
		for (int j = i + 1; j < n; ++ j){
			if (sqr(x[i] - x[j]) + sqr(y[i] - y[j]) + sqr(z[i] - z[j]) <= L){
				int fx = getf(i), fy = getf(j);
				f[fx] = fy;
			}
		}
	}
	return getf(0) == getf(1);
}

int main(){
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);
	int _, __ = 0;
	scanf("%d", &_);
	while (_--){
		printf("Case #%d: ", ++ __);
		scanf("%d%d", &n, &S);
		for (int i = 0; i < n; ++ i){
			scanf("%d%d%d%d%d%d", &x[i], &y[i], &z[i], &vx[i], &vy[i], &vz[i]);
		}
		int l = 0, r = 3e6;
		while (l < r){
			int mid = (l + r) / 2;
			if (ok(mid)) r = mid; else l = mid + 1;
		}
		printf("%.8f\n", sqrt(l * 1.0));
	}
	return 0;
}