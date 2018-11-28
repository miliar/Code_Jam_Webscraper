#include <bits/stdc++.h>

using namespace std;

long long get_divisor(long long x) {
	for (long long i = 2; i * i <= x; ++i) {
		if (x % i == 0) {
			return i;
		}
	}
	return -1;
}

long long to_system(long long x, int base) {
	long long cbase = 1, res = 0;
	for (long long i = 1; i <= x; i *= 2LL) {
		if (x & i) {
			res += cbase;
		}
		cbase *= base;
	}
	return res;			
}

string to_binray_view(long long x) {
	string res = "";
	for (long long j = 1; j <= x; j *= 2LL) {
		if (x & j) {
			res.append("1");
		} else {
			res.append("0");
		}
	}	
	reverse(res.begin(), res.end());	
	return res;
}

void solve() {
	long long n, q; cin >> n >> q;
	vector < vector <long long> > res;
	for (long long mask = 0; mask < (1LL << n) && (int)res.size() < q; ++mask) {
		if ((mask & 1) && (mask & (1LL << (n - 1)))) {
			vector <long long> cur = {mask};
			for (int j = 2; j <= 10; ++j) {
				long long res = get_divisor(to_system(mask, j));
				if (res == -1) {
					break;
				} else {
					cur.push_back(res);
				}
			}	
			if (cur.size() == 10) {
				res.push_back(cur);
			}	
		}	
	}
	for (int i = 0; i < q; ++i) {
		cout << to_binray_view(res[i][0]) << " ";
		for (int j = 1; j < (int)res[i].size(); ++j) {
			cout << res[i][j] << " ";
		}
		/*cout << endl;
		cout << "Checking: " << endl;
		for (int j = 2; j <= 10; ++j) {
			cout << to_system(res[i][0], j) << " " << get_divisor(to_system(res[i][0], j)) << endl;
		}*/
		cout << endl;
	} 
}

int main() {
#ifdef ALEXEY
	freopen("input", "r", stdin);
	freopen("output", "w", stdout);
#endif
	int test_count;
	cin >> test_count;
	cout << "Case #1:\n";
	solve();
	return 0;
}
