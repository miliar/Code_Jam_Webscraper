#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

long long primes[10000000];
int sz_primes = 0;
bool notPrime[100000010] = {1, 1};

long long decode(int n, int base) {
	if (base == 2) {
		return n;
	}
	long long m = 1;
	long long ret = 0;
	while (n) {
		ret += m * (n&1);
		m *= base;
		n >>= 1;
	}
	return ret;
}

vector<long long> solve(int n) {
	bool ok = true;
	//for (int b = 2; b <= 10; b++) {
	//	long long v = decode(n, b);
	//	ok &= !binary_search(primes, primes+sz_primes, v);
	//}
	vector<long long> ret;
	//if (ok) {
		for (int b = 2; b <= 10; b++) {
			long long v = decode(n, b);
			for (int i = 0; i < sz_primes; i++) {
				if (v % primes[i] == 0) {
					ret.push_back(primes[i]);
					break;
				}
			}
		}
	//}
	return ret;
}

int main() {
	for (int i = 2; i < 10000; i++) {
		if (!notPrime[i]) {
			for (int j = i+i; j < 10000; j += i) {
				notPrime[j] = true;
			}
			primes[sz_primes++] = i;
		}
	}
	int T; cin >> T;
	for (int No = 1; No <= T; No++) {
		int N, J; cin >> N >> J;
		cout << "Case #" << No << ":" << endl;
		int cnt = 0;
		for (int i = (1<<(N-1))+1; i < (1<<N) && cnt < J; i+=2) {
			vector<long long> ans = solve(i);
			if (ans.size() == 9) {
				cout << decode(i, 10);
				for (int i = 0; i < ans.size(); i++) {
					cout << " " << ans[i];
				}
				cout << endl;
				cnt++;
			}
		}
	}
	return 0;
}
