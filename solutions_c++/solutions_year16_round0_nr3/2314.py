#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <cmath>
#include <ctime>
#include <cstdlib>
#include <queue>

#define LL long long
#define mp(x, y) make_pair(x, y)
#define pb(x) push_back(x)
#define PII pair<int, int>
#define PID pair<int, double>

#define BIGINT LL

using namespace std;

const int j = 50;
int n, m;
string ans[j];
BIGINT fac[j][11];
bool one[32];

BIGINT is_prime(const BIGINT &val) {
	for (BIGINT x = 2; x * x <= val; ++x) {
		if (val % x == 0) return x;
	}
	return 0;
}

void search(int x) {
	if (m == j) return;
	if (x == n - 1) {
		bool flag = true;
		for (int b = 2; b <= 10; ++b) {
			BIGINT s = 0, e = 1;
			for (int i = 0; i < n; ++i) {
				if (one[i]) s += e;
				e = e * b;
			}
			BIGINT f = is_prime(s);
			if (!f) {
				flag = false;
				break;
			}
			fac[m][b] = f;
		}
		if (flag) {
			for (int i = n - 1; i >= 0; --i)
				ans[m] += one[i] ? '1' : '0';
			++m;
		}

	} else {
		one[x] = false;
		search(x + 1);
		one[x] = true;
		search(x + 1);
	}
}

int main(){
	n = 16;
	one[0] = one[n - 1] = 1;
	search(1);
	for (int i = 0; i < m; ++i) {
		cout << ans[i];
		for (int k = 2; k <= 10; ++k)
			cout << ' ' << fac[i][k];
		cout << endl;
	}
}
