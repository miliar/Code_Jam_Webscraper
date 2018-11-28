#include <bits/stdc++.h>
using namespace std;
bool isPrime(long long n) {
	if (n <= 1) return false;
	if (n <= 3) return true;
	if (n % 2 == 0 || n % 3 == 0) return false;
	for (long long i = 5; i * i <= n; i += 6)
		if (n % i == 0 || n % (i + 2) == 0) return false;
	return true;
}
long long firstDivisor(long long n) {
	if (n % 2 == 0) return 2;
	if (n % 3 == 0) return 3;
	for (long long i = 5; i * i <= n; i += 6) {
		if (n % i == 0) return i;
		if (n % (i + 2) == 0) return i + 2;
	}
}
long long convertTo(string s, long long base) {
	long long x = 0, cur = 1;
	for (int i = s.size() - 1; i >= 0; --i) {
		if (s[i] == '1')
			x += cur;
		cur *= base;
	}
	return x;
}
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t, n, j;
	cin >> t >> n >> j;
	int start = 1, x = n - 1;
	while (x) {
		start *= 2;
		x--;
	}
	int end = start * 2;
	start++;
	end--;
	vector< pair<string, int> > ok;
	vector< vector<long long> > bases(200005);
	for (int i = start; i <= end; i += 2) {
		string b;
		for (int k = 16; k >= 0; --k) {
			int two = (1 << k);
			if (two > i)
				continue;
			b += i & two ? '1' : '0';
		}
		vector<long long> all(11);
		bool p = isPrime(i);
		if (!p) {
			for (int base = 3; base <= 10; ++base) {
				long long converted = convertTo(b, base);
				p = isPrime(converted);
				if (p)
					break;
				all[base] = converted;
			}
		}
		if (!p) {
			ok.push_back(make_pair(b, i));
			for (int base = 3; base <= 10; ++base) {
				bases[i].push_back(all[base]);
			}
		}
		if (ok.size() == j)
			break;
	}
	cout << "Case #1:\n";
	for (int i = 0; i < ok.size(); ++i) {
		cout << ok[i].first;
		int dec = ok[i].second;
		cout << ' ' << firstDivisor(dec);
		for (int base = 0; base <= 7; ++base) {
			cout << ' ' << firstDivisor(bases[dec][base]);
		}
		cout << '\n';
	}
	return 0;
}
