#include <iostream>
#include <cstring>
#include <cstdio>

using namespace std;

int t, n, m, c;
long long sum, tmp;
int cnt[10];

int main () {
	// freopen("a.in", "r", stdin);
	// freopen("a.out", "w", stdout);
	cin >> t;
	for (int tc = 1; tc <= t; ++tc) {
		cin >> n;
		cout << "Case #" << tc << ": ";
		if (!n) {
			cout << "INSOMNIA" << endl;
			continue;
		}
		memset(cnt, 0, sizeof cnt);
		for (sum = n, c = 0; c != 10; sum += n) {
			tmp = sum;
			while (tmp) {
				m = tmp % 10;
				if (!cnt[m])
					c++, cnt[m]++;
				tmp /= 10;
			}
		}
		cout << sum - n << endl;
	}
	return 0;
}