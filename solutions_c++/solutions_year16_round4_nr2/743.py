#include <cstdio>
#include <cmath>
#include <algorithm>

using namespace std;

const int N = 210;

int n,k;
double x[N],y[N];

inline double solve () {
	scanf ("%d %d", &n, &k);
	for (int i = 0;i < n;i ++) {
		scanf ("%lf", &x[i]);
	}

	double ans = 0;
	for (int i = (1<<n)-1;i >= 0;i --) {
		int cnt = 0;
		for (int j = 0,_ = 0;j < n;j ++) {
			if ((i>>j)&1) {
				cnt ++;
				y[_ ++] = x[j];
			}
		}
		if (cnt != k) {
			continue;
		}

		double sum = 0;
		for (int j = (1<<k)-1;j >= 0;j --) {
			cnt = 0;
			double cal = 1;
			for (int l = 0;l < k;l ++) {
				if ((j>>l)&1) {
					cnt ++;
					cal *= y[l];
				} else {
					cal *= (1-y[l]);
				}
			}
			if (cnt != k/2) {
				continue;
			}
			sum += cal;
		}
		ans = max (ans, sum);
	}
	return ans;
}

int main () {
	int tt;
	scanf ("%d", &tt);

	for (int c = 1;c <= tt;c ++) {
		printf ("Case #%d: %lf\n", c, solve ());
	}
}