#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <vector>

using namespace std;
const int N = 300;
double a[N], b[N];
int n, k;
double ans;
double c[20][20];

void init() {
	c[0][0] = 1;
	for (int i = 1; i <= 17; i++) {
		c[i][0] = 1;
		for (int j = 1; j <= i; j++)
			c[i][j] = c[i - 1][j] + c[i - 1][j - 1];
	}
}

double cal(double b[], int n) {
	double res = 0;
	//cout<<n<<endl;
	//for (int i = 1; i <= n; i++)
	//	cout<<b[i]<<endl;
	for (int i = 0; i < (1<<n); i++) {
		int m = 0;
		double t = 1;
		for (int j = 1; j <= n; j++)
			if (i & (1<<(j-1))) {
				m++;
				t *= b[j];
			}
		if (m >= n/2) {
			t *= c[m][n/2];
			if ((m - n / 2) % 2 == 0)
				res += t;
			else
				res -= t;
		}
	}
	//cout<<res<<endl;
	return res;
}

void dfs(int now, int t, int k) {
	if (t == k) {
		double s = cal(b, k);
		if (s > ans)
			ans = s;
		return;
	}
	if (now > n)
		return;
	b[t + 1] = a[now];
	dfs(now + 1, t + 1, k);
	dfs(now + 1, t, k);
}

int main() {
	init();
	int o, cas = 0;
	scanf("%d", &o);
	while (o--) {
		scanf("%d %d", &n, &k);
		for (int i = 1; i <= n; i++)
			scanf("%lf", &a[i]);
		ans = 0;
		dfs(1, 0, k);
		printf("Case #%d: %.7lf\n", ++cas, ans);
	}
}