#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <cmath>
#include <vector>
#include <cstdlib>
#include <utility>
#include <memory.h>
#include <cassert>
#include <iterator>
#include <bitset>
#include <iomanip>
#include <complex>
#include <queue>
#include <ctime>
#include <deque>
#include <stack>
#include <set>
#include <map>
 
using namespace std;
 
#define pb push_back
#define mp make_pair
#define F first
#define S second

const int N = 222;

int n, k;
long double f[N][N];
long double p[N], q[N];

double solve(int m1, int mm) {
	double pr = 1.0;
	for (int i = 0; i < n; i++) {
		if ((mm & (1 << i)) == 0) continue;
		if ((m1 & (1 << i)) != 0) pr *= q[i]; else pr *= p[i]; 
	}
	return pr;
}

double solve(vector<int> &v) {
	for (int i = 0; i < N; i++) for (int j = 0; j <= N / 2; j++) f[i][j] = 0.0;
	f[0][0] = 1.0;
	for (int i = 0; i < k; i++) {
		for (int j = 0; j <= k / 2; j++) {
			f[i + 1][j] += (f[i][j] * p[v[i]]);
			if (j + 1 <= k / 2) {
				f[i + 1][j + 1] += (f[i][j] * q[v[i]]);
			}
		}
	}
	double ans = f[k][k / 2];
	return ans;
}

void solve(int test) {
	printf("Case #%d: ", test);
	cin >> n >> k;
	for (int i = 0; i < n; i++) {
		cin >> p[i];
	}
	sort(p, p + n);
	for (int i = 0; i < n; i++) {
		q[i] = 1.0 - p[i];
	}
	vector<int> v;
	for (int i = 0; i < k / 2; i++) v.pb(i);
	int taken = 0;
	for (int i = n - 1; i >= 0; --i) {
		v.pb(i);
		++taken;
		if (taken == k / 2) break;
	}
	long double ans = solve(v);
	v.clear();
	for (int i = 0; i < k; i++) v.pb(i);
	ans = max(ans, solve(v));
	for (int i = 0; i <= k; i++) {
		int need = k - i;
		v.clear();
		for (int j = 0; j < i; j++) v.pb(j);
		for (int j = n - 1; j >= 0; --j) {
			if (need == 0) break;
			v.pb(j);
			--need;
		}
		ans = max(ans, solve(v));
	}
	cout << fixed << setprecision(20) << ans << endl;
}
              
int main() {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	srand(time(NULL));
	int tc;
	scanf("%d", &tc);
	for (int i = 1; i <= tc; i++) {
		solve(i);
		cerr << i << "!" << endl;
	}
	return 0;
}
