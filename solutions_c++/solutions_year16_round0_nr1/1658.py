#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;

void fastInOut();

int vis[10], ID = 0;

int eval(int n) {
	int cnt = 0;
	while (n != 0) {
		if (vis[n % 10] != ID)
			vis[n % 10] = ID, ++cnt;
		n /= 10;
	}
	return cnt;
}

int lst(int n) {
	if (n == 0)
		return -1;
	int tot = n, cnt = 0;
	++ID;
	while (1) {
		cnt += eval(tot);
		if (cnt == 10)
			return tot;
		tot += n;
	}
	return -1;
}

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	fastInOut();
	int t, n;
	cin >> t;
	for (int tst = 1; tst <= t; ++tst) {
		cin >> n;
		int ret = lst(n);
		cout << "Case #" << tst << ": ";
		if (ret == -1)
			cout << "INSOMNIA\n";
		else
			cout << ret << "\n";
	}
	return 0;
}

void fastInOut() {
	ios_base::sync_with_stdio(0);
	cin.tie(NULL), cout.tie(NULL);
}
