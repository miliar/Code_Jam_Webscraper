//Codejam 2014 Qualification A
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

#define N 4
int T, a[N + 1][N + 1], x, Case = 0;
bool v[N * N + 1];

int main(int argc, char *argv[]) {
#ifdef KANARI
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	
	cin >> T;
	while (T--) {
		for (int i = 1; i <= N * N; ++i) v[i] = false;
		cin >> x;
		for (int i = 1; i <= N; ++i)
			for (int j = 1; j <= N; ++j)
				cin >> a[i][j];
		for (int i = 1; i <= N; ++i)
			v[a[x][i]] = true;
		cin >> x;
		for (int i = 1; i <= N; ++i)
			for (int j = 1; j <= N; ++j)
				cin >> a[i][j];
		int cnt = 0, p = 0;
		for (int i = 1; i <= N; ++i)
			if (v[a[x][i]]) ++cnt, p = a[x][i];
		
		cout << "Case #" << ++Case << ": ";
		if (cnt == 0) cout << "Volunteer cheated!" << endl;
		else if (cnt > 1) cout << "Bad magician!" << endl;
		else cout << p << endl;
	}
	
	fclose(stdin);
	fclose(stdout);
	return 0;
}
