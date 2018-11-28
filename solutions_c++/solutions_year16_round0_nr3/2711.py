#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <fstream>
#include <map>
#include <set>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>
#include <utility>
#include <cstring>
#include <list>
#include <stack>
#include <vector>
using namespace std;


typedef long long LL;

LL bases[11][50];
vector<LL> primes;

void InitPrimes() {
	for (LL i = 2; i <= (1 << 16); ++i) {
		bool isPrime = true;
		for (int j = 0; j < primes.size() && i / primes[j] >= primes[j]; ++j) {
			if (i % primes[j] == 0) {
				isPrime = false;
				break;
			}
		}
		if (isPrime) {
			primes.push_back(i);
		}
	}
}

int main(){
	freopen("input.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	InitPrimes();

	for (int i = 2; i < 11; ++i) {
		LL k = 1;
		for (int j = 0; j < 32; ++j) {
			bases[i][j] = k;
			k *= i;
		}
	}
	int T;
	cin >> T;
	for (int caseID = 1; caseID <= T; ++caseID) {
		printf("Case #%d:\n", caseID);
		int N, J;
		cin >> N >> J;
		int x[50];
		x[0] = x[N - 1] = 1;
		int cnt = 0;
		for (int i = 0; i < (1 << (N - 2)); ++i) {
			for (int j = 0; j < N - 2; ++j) {
				x[j + 1] = (i >> j) & 1;
			}
			vector<LL> divisors;
			for (int j = 2; j < 11; ++j) {
				LL s = 0;
				for (int k = 0; k < N; ++k) {
					s += (x[N - 1 - k] ? bases[j][k] : 0);
				}
				for (int k = 0; k < primes.size() && s / primes[k] >= primes[k]; ++k) {
					if (s % primes[k] == 0) {
						divisors.push_back(primes[k]);
						break;
					}
				}
			}
			if (divisors.size() == 9) {
				for (int j = 0; j < N; ++j) cout << x[j];
				for (int j = 0; j < 9; ++j) cout << " " << divisors[j];
				cout << endl;
				++cnt;
				if (cnt == J) break;
			}
		}
	}
}