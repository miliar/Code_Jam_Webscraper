//Template
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <climits>
#include <cmath>
#include <utility>
#include <set>
#include <map>
#include <queue>
#include <ios>
#include <iomanip>
#include <ctime>
#include <numeric>
#include <functional>
#include <fstream>
#include <string>
#include <vector>
#include <bitset>
#include <cstdarg>
#include <complex>
using namespace std;

typedef long long ll;
typedef unsigned int uint;
typedef unsigned long long ull;
typedef long double ld;
#define pair(x, y) make_pair(x, y)
#define runtime() ((double)clock() / CLOCKS_PER_SEC)

inline int read() {
	static int r, sign;
	static char c;
	r = 0, sign = 1;
	do c = getchar(); while (c != '-' && (c < '0' || c > '9'));
	if (c == '-') sign = -1, c = getchar();
	while (c >= '0' && c <= '9') r = r * 10 + (int)(c - '0'), c = getchar();
	return sign * r;
}

template <typename T>
inline void print(T *a, int n) {
	for (int i = 1; i < n; ++i) cout << a[i] << " ";
	cout << a[n] << endl;
}
#define PRINT(_l, _r, _s, _t) { cout << #_l #_s "~" #_t #_r ": "; for (int _i = _s; _i != _t; ++_i) cout << _l _i _r << " "; cout << endl; }

#define N 12
int n, r, p, s, T;
string seq[N + 1][100];
int cnt[N + 1][100][3];
char *str = "RSP";

int main(int argc, char *argv[]) {
#ifdef KANARI
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	
	int Case = 0;
	cin >> T;
	seq[0]['R'] = "R";
	seq[0]['S'] = "S";
	seq[0]['P'] = "P";
	for (int i = 1; i <= N; ++i) {
		if (seq[i - 1]['R'] < seq[i - 1]['P']) {
			seq[i]['P'] = seq[i - 1]['R'] + seq[i - 1]['P'];
		} else {
			seq[i]['P'] = seq[i - 1]['P'] + seq[i - 1]['R'];
		}
		if (seq[i - 1]['S'] < seq[i - 1]['R']) {
			seq[i]['R'] = seq[i - 1]['S'] + seq[i - 1]['R'];
		} else {
			seq[i]['R'] = seq[i - 1]['R'] + seq[i - 1]['S'];
		}
		if (seq[i - 1]['P'] < seq[i - 1]['S']) {
			seq[i]['S'] = seq[i - 1]['P'] + seq[i - 1]['S'];
		} else {
			seq[i]['S'] = seq[i - 1]['S'] + seq[i - 1]['P'];
		}
	}
	for (int i = 0; i <= N; ++i) {
		for (int j = 0; j < 3; ++j) {
			for (int x = 0; x < seq[i][str[j]].length(); ++x) {
				for (int k = 0; k < 3; ++k)
					if (seq[i][str[j]][x] == str[k])
						++cnt[i][str[j]][k];
			}
		}
	}
	while (T--) {
		cin >> n >> r >> p >> s;
		string ans = "";
		for (int i = 0; i < 3; ++i) {
			if (cnt[n][str[i]][0] == r && cnt[n][str[i]][1] == s && cnt[n][str[i]][2] == p) {
				if (ans == "" || ans > seq[n][str[i]])
					ans = seq[n][str[i]];
			}
		}
		cout << "Case #" << ++Case << ": ";
		if (ans == "") cout << "IMPOSSIBLE" << endl;
		else cout << ans << endl;
	}

	fclose(stdin);
	fclose(stdout);
	return 0;
}
