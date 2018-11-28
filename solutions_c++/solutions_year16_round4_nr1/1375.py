#include <fstream>
#include <string>

using namespace std;

ifstream fin("A-large.in");
ofstream fout("out.txt");

string ss[] = {"PRPSRS", "PRRSPS", "PSPRRS", "PSRSPR", "RSPRPS", "RSPSPR"};
string res = "";

bool check(int pos, int n, int r, int p, int s) {
	res = "";
	for (int i = 0; i < (1 << n); ++i) {
		if (ss[pos][i % 6] == 'P') {
			if (p > 0) {
			    --p;
			    res += 'P';
			} else {
				return false;
			}
		}
		if (ss[pos][i % 6] == 'R') {
			if (r > 0) {
			    --r;
			    res += 'R';
			} else {
				return false;
			}
		}
		if (ss[pos][i % 6] == 'S') {
			if (s > 0) {
			    --s;
			    res += 'S';
			} else {
				return false;
			}
		}
	}
	return true;
}

int comp(int p1, int p2, int n) {
	for (int i = 0; i < n; ++i) {
		if (res[p1 + i] > res[p2 + i]) {
			return -1;
		} else if (res[p1 + i] < res[p2 + i]) {
			return 1;
		}
	}

	return 0;
}

void optimize(int l, int r, int n) {
	if (n == 2) return;
	optimize(l, l + n / 2, n / 2);
	optimize(l + n / 2, r, n / 2);
	if (comp(l, l + n / 2, n / 2) == -1) {
		for (int i = l; i < l + n / 2; ++i) {
			swap(res[i], res[i + n / 2]);
		}
	}
}

int main() {
	int tests;
	fin >> tests;
	for (int test = 0; test < tests; ++test) {
		int n, r, p, s;
		fin >> n >> r >> p >> s;
		fout << "Case #" << test + 1 << ": ";
		if (check(0, n, r, p, s)) {
			optimize(0, (1 << n), 1 << n);
			fout << res << endl;
		} else
		if (check(1, n, r, p, s)) {
			optimize(0, (1 << n), 1 << n);
			fout << res << endl;
		} else
		if (check(2, n, r, p, s)) {
			optimize(0, (1 << n), 1 << n);
			fout << res << endl;
		} else
		if (check(3, n, r, p, s)) {
			optimize(0, (1 << n), 1 << n);
			fout << res << endl;
		} else
		if (check(4, n, r, p, s)) {
			optimize(0, (1 << n), 1 << n);
			fout << res << endl;
		} else
		if (check(5, n, r, p, s)) {
			optimize(0, (1 << n), 1 << n);
			fout << res << endl;
		} else {
			fout << "IMPOSSIBLE" << endl;
		}
	}

	return 0;
}
