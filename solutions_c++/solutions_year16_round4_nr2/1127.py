#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <vector>
#include <queue>
#include <cmath>
#include <string>
#include <algorithm>
#include <iomanip>
using namespace std;

const int N = 17;

double a[N];
int k, n;
int b[N];
double ans[1 << N];
int p2[N];

void dfs(int p, int u, int v)
{
	if(u == 0 && v == 0) {
		double res = 1;
		int t = 0;
		for(int i = 1; i < p; ++i) {
			if(b[i] == 1) {
				res *= a[i];
				t += p2[i-1];
			}
			else if(b[i] == -1) {
				res *= 1 - a[i];
				t += p2[i-1];
			}
		}
		ans[t] += res;
		return;
	}
	if(n-p+1 < u+v) {
		return;
	}
	if(n-p >= u+v) {
		b[p] = 0;
		dfs(p+1, u, v);
	}
	if(u) {
		b[p] = 1;
		dfs(p+1, u-1, v);
	}
	if(v) {
		b[p] = -1;
		dfs(p+1, u, v-1);
	}
}

void work()
{
	double ma = 0;
	cin >> n >> k;
	for(int i = 1; i < (1 << n); ++i) {
		ans[i] = 0;
	}
	for(int i = 1; i <= n; ++i) {
		cin >> a[i];
	}
	dfs(1, k/2, k/2);
	for(int i = 1; i < (1 << n); ++i) {
		ma = max(ma, ans[i]);
	}
	cout << fixed << setprecision(9) << ma << endl;
}

void pre()
{
	p2[0] = 1;
	for(int i = 1; i <= 16; ++i) {
		p2[i] = p2[i-1]*2;
	}
}

int main()
{
	#define LOCAL
	#ifdef LOCAL

	freopen("0.in", "r", stdin);
	freopen("0.out", "w", stdout);

	#endif // LOCAL

	pre();
	int n;
	cin >> n;
	for(int i = 1; i <= n; ++i) {
		cout << "Case #" << i << ": ";
		work();
	}
	return 0;
}
