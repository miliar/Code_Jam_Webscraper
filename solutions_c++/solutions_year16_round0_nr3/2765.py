#include "template.h"



int n, j;

string makeStr(long long l) {
	string ret;
	for (int i = 0; i < n; ++i) {
		ret.push_back(l % 2 + '0');
		l /= 2;
	}
	ret.push_back('1');
	reverse(ret.begin(), ret.end());
	ret.push_back('1');
	return ret;
}

long long isPrime(long long n) {
	if (n <= 1)
		return false;

	for (long long i = 2; i * i <= n; i++)
		if (n % i == 0)
			return i;

	return 0;
}
vector<long long> isCoinJam(const string& s) {
	vector<long long> ret;
	for (int ary = 2; ary <= 10; ++ary) {
		long long num = 0;
		for (int i = 0; i < s.size(); ++i) {
			num += (s[i] - '0');
			if (i < s.size() - 1) {
				num *= ary;
			}
		}
		long long isP = isPrime(num);
		if (isP == 0) {
			return vector<long long>();
		}
		ret.push_back(isP);
	}
	return ret;
}
int main() {
	freopen("C_output.txt", "w", stdout);
	int TC; cin >> TC;
	for (int tc = 1; tc <= TC; ++tc) {
		cin >> n >> j;
		n -= 2;

		const long long l = (1ll<<n);
		
		cout << "Case #1: " << endl;
		for (long long i = 0; i < l && (j > 0); ++i) {
			string s = makeStr(i);
			if (i % 100 == 0) {
				cerr << "its " << i << endl;
				//cerr << s << endl;
			}
			auto vll = isCoinJam(s);
			if (vll.size() == 0) {
				continue;
			}
			else {
				cout << s << ' ';
				for (auto& k : vll) {
					cout << k << ' ';
				}
				cout << endl;
				j--;
			}
		}
		
	}
	return 0;
}