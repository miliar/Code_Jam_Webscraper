#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

const int N = 1e6 + 5;
long long n, p, q, r, s, sum;
long long a[N], b[N];

long long calc(int j, int i) {
	long long t1 = b[i] - b[j - 1];
	long long t2 = b[j - 1];
	long long t3 = sum - t1 - t2;
	return sum - max(max(t1, t2), t3);
}

void solve() {
	cin >> n >> p >> q >> r >> s;
	b[0] = 0;
	for (int i = 0; i < n; i++) {
		a[i + 1] = (i * (long long) p + q) % r + s;
		b[i + 1] = b[i] + a[i + 1];
	}
	sum = b[n];
	long long ans = 0;
	int j = 1;
	for (int i = 1; i <= n; i++) {
		while (j < i && calc(j, i) < calc(j + 1, i)) j++;
		ans = max(ans, calc(j, i));
	}
	double p = ans / (double) sum;
	printf("%.10f", p);
}

int main() {
	//ios::sync_with_stdio(false);
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		cout << "Case #" << t << ": ";
		solve();
		cout << endl;
	}
}