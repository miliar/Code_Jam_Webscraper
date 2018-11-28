#include <iostream>
#include <string>
#include <vector>
using namespace std;

typedef long long Uint;

Uint toKBase(Uint x, int base, int N) {
	Uint ans = 0;
	for (int i = 0; i < N; ++i) {
		ans *= base;
		ans += (x & (1u << (N-i-1))) > 0;
	}

	return ans;
}

int isPrime(Uint x) {
	if (x == 2 || x == 3 || x == 5 || x == 7)
		return 0;
	if (x % 2 == 0)
		return 2;
	if (x % 3 == 0)
		return 3;
	if (x % 5 == 0)
		return 5;
	if (x % 7 == 0)
		return 7;
	for (Uint i = 11; i*i <= x; i+=2)
		if (x % i == 0)
			return i;
	return 0;
}

string toBinary(Uint x, int N) {
	string ans(N, ' ');
	for (int i = 0; i < N; ++i)
		ans[i] = ((x & (1u << (N-i-1))) > 0) ? '1' : '0';
	return ans;
}

int main() {
	int T, N, J;
	cin >> T >> N >> J;

	Uint beg = (1u << (N-1)) | (1u), end = 0;
	for (int i = 0; i < N; ++i)
		end |= (1u << i);

	vector<int> divisor(11);
	vector<pair<Uint, vector<int> > > ans;
	for (Uint i = beg; i <= end; i+=2) {
		bool allIsNotPrime = true;
		for (int base = 2; base <= 10; ++base) {
			divisor[base] = isPrime(toKBase(i, base, N));
			if (divisor[base] == 0) {
				allIsNotPrime = false;
				break;
			}
		}

		if (allIsNotPrime) {
			// cout << "haha " << i << endl;
			ans.push_back(make_pair(i, divisor));
			if (ans.size() >= J) {
				cout << "Case #1: " << endl;
				for (int x = 0; x < J; ++x) {
					cout << toBinary(ans[x].first, N) << ' ';
					for (int xx = 2; xx < ans[x].second.size(); ++xx)
						cout << ans[x].second[xx] << ' ';
					cout << endl;
					// for (int base = 2; base <= 10; ++base)
					// 	cout << toKBase(ans[x].first, base, N) << ' ';
					// cout << endl;
				}
				break;
			}
		}
	}

	return 0;
}