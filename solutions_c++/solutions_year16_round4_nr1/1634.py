#include <iostream>
#include <vector>
#include <string>
using namespace std;

bool ok(const string& in) {
	string v = in;
	size_t n = v.size();
	while (n > 1) {
		for (int i = 0; i < n / 2; ++i) {
			if (v[2*i] == v[2*i + 1]) {
				return false;
			} else if ((v[2*i] == 'P' && v[2*i + 1] == 'R') || (v[2*i] == 'R' && v[2*i + 1] == 'P')) {
				v[i] = 'P';
			} else if ((v[2*i] == 'P' && v[2*i + 1] == 'S') || (v[2*i] == 'S' && v[2*i + 1] == 'P')) {
				v[i] = 'S';
			} else {
				v[i] = 'R';
			}
		}
		n /= 2;
	}
	return true;
}

int main() {
	int tests;
	cin >> tests;
	for (int test = 1; test <= tests; ++test) {
		int n, r, p, s;
		cin >> n >> r >> p >> s;

		cout << "Case #" << test << ": ";
		int cnt = 1 << n;
		if (r > cnt / 2 || p > cnt / 2 || s > cnt / 2) {
			cout << "IMPOSSIBLE" << endl;
			continue;
		}

		int rs = cnt / 2 - p;
		int ps = s - rs;
		int pr = r - rs;

		vector<int> gen(cnt / 2, 0);
		int npr = 0, nps = 0, nrs = 0;
		int pos = 0;
		while (pos >= 0) {
			if (pos >= cnt / 2) {
				string v;
				v.reserve(cnt);
				for (int i = 0; i < cnt / 2; ++i) {
					if (gen[i] == 1) {
						v += "PR";
					} else if (gen[i] == 2) {
						v += "PS";
					} else {
						v += "RS";
					}
				}
				if (ok(v)) {
					cout << v << endl;
					break;
				}
				--pos;
				continue;
			}

			if (gen[pos] == 1) {
				--npr;
			} else if (gen[pos] == 2) {
				--nps;
			} else if (gen[pos] == 3) {
				--nrs;
			}

			if (gen[pos] < 1 && npr < pr) {
				++npr;
				gen[pos++] = 1;
				gen[pos] = 0;
			} else if (gen[pos] < 2 && nps < ps) {
				++nps;
				gen[pos++] = 2;
				gen[pos] = 0;
			} else if (gen[pos] < 3 && nrs < rs) {
				++nrs;
				gen[pos++] = 3;
				gen[pos] = 0;
			} else {
				--pos;
			}
		}

		if (pos < 0) {
			cout << "IMPOSSIBLE" << endl;
		}
	}
}
