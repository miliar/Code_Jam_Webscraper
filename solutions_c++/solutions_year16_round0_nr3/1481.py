#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <iomanip>
#include <string>
#include <tuple>
#include <queue>
#include <utility>
#include <stack>
#include <set>
#include <map>
#include <deque>
#include <limits>
#include <new>
#include <functional>
#include <unordered_map>
#include <unordered_set>

using namespace std;

long long transform(int mask, long long base, int n) {
	long long val = 0;
	long long fact = 1;
	for (int i = 0; i < n; i++) {
		val += fact * (long long)(mask & 1);
		mask = mask >> 1;
		fact *= base;
	}
	return val;
}

string makebinary(int val, int n) {
	string res;
	for (int i = 0; i < n; i++) {
		res += to_string(val & 1);
		val = val >> 1;
	}
	string realres;
	for (int i = res.size() - 1; i >= 0; i--) {
		realres += res[i];
		if (i == res.size() - 1) realres += "0000000000000000";
	}
	return realres;
}

int main(void) {
	cin.tie(nullptr);
	cin.sync_with_stdio(false);

	int t;
	cin >> t;
	for (int i = 1; i <= t; i++) {
		int n, j;
		cin >> n >> j;
		cout << "Case #" << i << ": " << '\n';
		vector<bool> p(100000102, true);
		vector<long long> prime;
		p[0] = p[1] = false;
		for (long long k = 2; k < 100000102LL; k++) {
			if (p[k]) {
				prime.push_back(k);
				if (k < 20000) {
					for (long long l = k * k; l < 100000102LL; l += k) {
						if (k == 46349) {
							cout << l << endl;
						}
						p[l] = false;
					}
				}
			}
		}
		int cnt = 0;
		for (int mask = (1 << n - 1) + 1; mask < 1 << n; mask += 2) {
			vector<long long> divs;
			for (int base = 2; base <= 10; base++) {
				long long val = transform(mask, base, n);
				for (int it = 0; prime[it] * prime[it] <= val; it++) {
					if (val % prime[it] == 0) {
						divs.push_back(prime[it]);
						break;
					}
				}
			}
			if (divs.size() == 9 && divs[0] == 3 && divs[1] == 2 && divs[2] == 3 && divs[3] == 2 && divs[4] == 7 && divs[5] == 2 && divs[6] == 3 && divs[7] == 2 && divs[8] == 3) {
				cnt++;
				cout << makebinary(mask, n) << ' ';
				for (int it = 0; it < 9; it ++) {
					cout << divs[it] << (it != 8 ? ' ' : '\n');
				}
			}
			if (cnt == j) break;
		}

	}

	return 0;
}