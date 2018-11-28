#include <cmath>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <map>
#include <set>
#include <string>
#include <queue>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

#define foreach(e,x) for(__typeof(x.begin()) e=x.begin(); e!=x.end(); ++e)

const int N = 100 + 10;
const int M = 1000 + 10;

int n;
int p, q;
int h[N], g[N];
int c[N];
int d[N], u[N];
int f[N][M];

void solve(int test)
{
	printf("Case #%d: ", test);
	cin >> p >> q >> n;
	for(int i = 0; i < n; ++ i) {
		cin >> h[i] >> g[i];
		c[i] = 0;
		for(int tmp = h[i]; tmp > 0; tmp -= q) {
			++ c[i];
		}
		d[i] = -1;
		for(int x = 0; x * p <= h[i]; ++ x) {
			for(int y = 0; y * q <= h[i]; ++ y) {
				if (x * p + y * q < h[i] && x * p + p + y * q >= h[i]) {
					d[i] = x;
					u[i] = y;
				}
			}
			if (d[i] >= 0) break;
		}
	}

	memset(f, -1, sizeof f);
	f[0][1] = 0;
	for(int i = 0; i < n; ++ i) {
		for(int j = 0; j < M; ++ j) {
			if (f[i][j] < 0) continue;
			//not kill
			f[i + 1][j + c[i]] = max(f[i + 1][j + c[i]], f[i][j]);
			//kill
			if (d[i] - u[i] + 1 <= j) {
				f[i + 1][j + u[i] - d[i] - 1] = max(f[i + 1][j + u[i] - d[i] - 1], f[i][j] + g[i]);
			}
		}
	}
	int ret = 0;
	for(int i = 0; i <= n; ++ i) {
		for(int j = 0; j < M; ++ j) {
			ret = max(ret, f[i][j]);
		}
	}
	cout << ret << endl;
}

int main()
{
	//freopen("B-small-attempt0.in", "r", stdin); freopen("B-small-attempt0.out1", "w", stdout);
	//freopen("B-small-attempt1.in", "r", stdin); freopen("B-small-attempt1.out", "w", stdout);
	freopen("B-large.in", "r", stdin); freopen("B-large.out", "w", stdout);
	int testcase;
	scanf("%d", &testcase);
	for(int i = 1; i <= testcase; ++ i) 
		solve(i);
	fclose(stdout);
	return 0;
}
