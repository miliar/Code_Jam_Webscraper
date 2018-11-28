#include <bits/stdc++.h>
using namespace std;

long long convert(vector<int> v, int n, long long dec) {
	long long mul = 1;
	long long res = 0;
	for (int j = n - 1; j >= 0; j--) {
		res += v[j] * mul;
		mul *= dec;
	}
	return res;
}

int is_prime(long long n) {
	for (long long i = 2; i * i <= n; i++) {
		if (n % i == 0) {
			return i;
		}
	}
	return -1;
}

void solve(){
	int n, cnt;
	cin >> n >> cnt;

	for (int mask = 0; mask < (1 << n) && cnt > 0; mask++) {
		vector<int> v;
		for (int j = 0; j < n; j++) {
			if (mask & (1 << j)) {
				v.push_back(1);
			}
			else {
				v.push_back(0);
			}
		}
		if (v[0] == 0 || v[n - 1] == 0) {
			continue;
		}
		bool prime = false;
		vector<int> t;
		for (int i = 2; i <= 10; i++) {
			t.push_back(is_prime(convert(v, n, i)));
			if (t.back() == -1) {
				prime = true;
			}
		}
		if (!prime) {
			for (int i = 0; i < n; i++) {
				cout << v[i];
			}
			for (int i = 0; i < t.size(); i++) {
				cout << " " << t[i];
			}
			cout << endl;
			cnt--;
		}
	}
}

int main(){
#ifdef HELTHAZAR
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif

	int test;
	cin >> test;
	for (int t = 1; t <= test; t++) {
		//printf("Case #%d: ", t);
		cout << "Case #" << t << ": " << endl;
		solve();
		//printf("\n");
	}
}
