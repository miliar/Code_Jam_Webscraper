#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>
#include <deque>
#include <cstdlib>
#include <ctime>
#include <cmath>
#include <algorithm>
#include <map>
#include <set>

using namespace std;

const int MAXM = 1010;
const int MAXTN = 2020;
const long long MOD = 1000002013;

int T, M;
long long N;
long long o[MAXM], e[MAXM], p[MAXM];
int tn;
long long d[MAXTN], s[MAXTN];
long long newTotal, oriTotal;

int main() {
	cin >> T;
	for (int c = 0; c < T; ++c) {
		cin >> N >> M;
		tn = 0;
		for (int i = 0; i < M; ++i) {
			cin >> o[i] >> e[i] >> p[i];
			if (o[i] == e[i]) continue;
			bool foundo = false;
			bool founde = false;
			for (int j = 0; j < tn; ++j) {
				if (d[j] == o[i]) {
					s[j] += p[i];
					foundo = true;
				}
				if (d[j] == e[i]) {
					s[j] -=p[i];
					founde = true;
				}
			}
			if (!foundo) {
				++tn;
				d[tn - 1] = o[i];
				s[tn - 1] = p[i];
			}
			if (!founde) {
				++tn;
				d[tn - 1] = e[i];
				s[tn - 1] = -p[i];
			}
		}
		for (int i = 0; i < tn; ++i) {
			for (int j = tn - 1; j > i; --j) {
				if (d[j] < d[j-1]) {
					swap(d[j], d[j-1]);
					swap(s[j], s[j-1]);
				}
			}
		}
		newTotal = 0;
		for (int i = 0; i < tn; ++i) {
			if (s[i] >= 0) continue;
			for (int j = i - 1; j >= 0; --j) {
				if (s[j] > 0) {
					long long k = d[i] - d[j];
					long long tmp = (2 * N + 1 - k) * k / 2;
					tmp %= MOD;
					if (s[j] > -s[i]) {
						tmp = (tmp * (-s[i])) % MOD;
						newTotal += tmp;
						newTotal %= MOD;
						s[j] += s[i];
						s[i] = 0;
					} else {
						tmp = (tmp * s[j]) % MOD;
						newTotal += tmp;
						newTotal %= MOD;
						s[i] += s[j];
						s[j] = 0;
					}
				}
			}
		}
		oriTotal = 0;
		for (int i = 0; i < M; ++i) {
			long long k = e[i] - o[i];
			long long tmp = (2 * N + 1 - k) * k / 2;
			tmp %= MOD;
			oriTotal += (tmp * p[i]) % MOD;
			oriTotal %= MOD;
		}
		long long loss = (oriTotal + MOD - newTotal) % MOD;
		cout << "Case #" << c + 1 << ": " << loss << endl;
	}
	return 0;
}
