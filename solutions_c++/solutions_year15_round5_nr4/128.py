#include <algorithm>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <set>
#include <map>
using namespace std;

#define mp(a,b) make_pair(a,b)

long long kInf = 1e15;


map<long long, long long> m;
long long v[10005];
long long s[10005];

void Solve(bool nothing = false) {
	long long p;
	cin >> p;
	if (nothing) {
		return;
	}
	long long n = 0;
	for (int i = 0; i < p; ++i) {
		cin >> v[i];
	}
	for (int i = 0; i < p; ++i) {
		cin >> s[i];
		n += s[i];
	}
	int deg = 0;
	while (n != 1) {
		++deg;
		n >>= 1;
	}
	m.clear();
	for (int i = 0; i < p; ++i) {
		m[v[i]] = s[i];
	}
	for (int i = 0; i < deg; ++i) {
		long long x = -kInf;
		for (int j = 0; j < p; ++j) {
			if (m.count(v[j]) == 0 || m[v[j]] == 0) {
				continue;
			}
			map<long long, long long> m1 = m;
			bool ok = true;
			if (v[j] == 0) {
				for (int k = 0; k < p; ++k) {
					if (m1.count(v[k]) == 0) {
						continue;
					}
					if (m1[v[k]] % 2 != 0) {
						ok = false;
						break;
					}
					m1[v[k]] = m1[v[k]] / 2;
				}
			} else {
				if (v[j] > 0) {
					for (auto it : m1) {
						if (it.second == 0) {
							continue;
						}
						if (m1.count(it.first) == 0 || v[j] > 0 && m1[it.first + v[j]] < it.second) {
							ok = true;
							break;
						}
						m1[it.first + v[j]] -= it.second;
					}
				} else {
					for (auto itt = m1.rbegin(); itt != m1.rend(); ++itt) {
						auto& it = *itt;
						if (it.second == 0) {
							continue;
						}
						if (m1.count(it.first) == 0 || v[j] < 0 && m1[it.first + v[j]] < it.second) {
							ok = true;
							break;
						}
						m1[it.first + v[j]] -= it.second;
					}
				}
			}
			if (ok) {
				m = m1;
				x = v[j];
				break;
			}
		}
		if (x == -kInf) {
			cerr << "Failed";
		} else {
			cout << x << " ";
		}
	}
	cout << "\n";
}


int main(int argc, char** argv) {
	freopen("d.in", "r", stdin);
	freopen("d.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int I = 0; I < T; ++I) {
		printf("Case #%d: ", I + 1);
		Solve();
	}
	return 0;
}