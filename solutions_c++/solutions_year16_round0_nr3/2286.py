#include <cstring>
#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <map>

using namespace std;

map<long long int, int> M;

long long int isPrime(long long int N) {
	if (M.find(N) != M.end()) {
		return M[N];
	}

	if (N == 2) {
		M[2] = -1;
		return -1;
	}

	if (N % 2 == 0) {
		return 2;
	}

	for (long long int i = 3; i * i <= N; i += 2) {
		if (N % i == 0) {
			M[N] = i;
			return i;
		}
	}

	M[N] = -1;
	return -1;
}

long long int check(vector<int> s, int base) {
	long long int p = 1;
	long long int n = 0;

	for (int i = 0; i < s.size(); i++) {
		n += p * s[i];
		p = (p * base);
	}
	return isPrime(n);
}

void solve() {
	int count = 0;
	int no = (1 << 15) + 1;
	vector<long long int> V(11);
	while (count < 50) {
		bool o = false;
		vector<int> s(16);
		for (int i = 0; i < 16; i++) {
			s[i] = 1 & (no >> i);
		}

		for (int i = 2; i <= 10; i++) {
			long long int tmp = check(s, i);
			if (tmp != -1) {
				V[i] = tmp;
			} else {
				o = true;
				break;
			}
		}

		if (!o) {
			count++;
			for (int i = 15; i >= 0; --i) {
				cout << s[i];
			}
			
			cout << ' ';

			for (int i = 2; i <= 10; i++) {
				cout << V[i] << ' ';
			}
			cout << '\n';
		} 
		no += 2;
	}
}


int main() {
	ios::sync_with_stdio(false);
	cout << "Case #1:\n";
	solve();
	return 0;
}