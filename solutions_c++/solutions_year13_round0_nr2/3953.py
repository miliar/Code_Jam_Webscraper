//C++ Template: http://pastebin.com/dGrr0CpX

#pragma comment(linker,"/STACK:256000000")

#include <algorithm>
#include <iostream>
#include <memory.h>
#include <iomanip>
#include <string>
#include <vector>
#include <cstdio>
#include <cmath>
#include <queue>
#include <ctime>
#include <set>
#include <map>

using namespace std;

#define all(a) a.begin(), a.end()
#define PI 3.14159265358979
#define sz(a) (int)a.size()
#define ppb push_back
#define mp make_pair
#define se second
#define fi first

template <class T> T sqr(T n) {
	return n*n;
}

template <class T> T gcd(T a, T b) {
	while (b) {
		a %= b;
		cout << a << " " << b << endl;
		swap(a, b);
	}
    return a;
}

const int SZ = 1010;
const int INF = 1000*1000*1000;

double start, finish;
/****************************************************************************/
void prepare(string s) {
#ifdef _DEBUG
	freopen("input.txt", "r", stdin);
#else
	if (sz(s) != 0) {
		freopen((s + ".in").c_str(), "r", stdin);
		freopen((s + ".out").c_str(), "w", stdout);
	}
#endif
}

void startTimer() {
#ifdef _DEBUG
	start = clock();
#endif
}

void stopTimer() {
#ifdef _DEBUG
	finish = clock();
    cout << "\n*** Total time ***\n" << (finish - start)/CLOCKS_PER_SEC << endl;
#endif
}
/****************************************************************************/

int n, m, tests;
int lawn[SZ][SZ];
bool confirm[SZ][SZ];

void reset() {
	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < m; ++j) {
			confirm[i][j] = false;
		}
	}
}

void getLawn() {
	cin >> n >> m;
	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < m; ++j) {
			cin >> lawn[i][j];
		}
	}
}

int getHeightRow(int k) {
	int ans = -INF;
	for (int j = 0; j < m; ++j) {
		ans = max(ans, lawn[k][j]);
	}
	return ans;
}

int getHeightCol(int k) {
	int ans = -INF;
	for (int i = 0; i < n; ++i) {
		ans = max(ans, lawn[i][k]);
	}
	return ans;
}

bool getAns() {

	for (int i = 0; i < n; ++i) {
		int h = getHeightRow(i);
		for (int j = 0; j < m; ++j) {
			if (lawn[i][j] == h) {
				confirm[i][j] = true;
			}
		}
	}

	for (int j = 0; j < m; ++j) {
		int h = getHeightCol(j);
		for (int i = 0; i < n; ++i) {
			if (lawn[i][j] == h) {
				confirm[i][j] = true;
			}
		}
	}

	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < m; ++j) {
			if (!confirm[i][j]) {
				return false;
			}
		}
	}

	return true;
}

int main() {

prepare("");
ios::sync_with_stdio(false);

startTimer();

	freopen("B-large.out", "w", stdout);
	cin >> tests;
	for (int z = 0; z < tests; ++z) {
		getLawn();
		reset();
		cout << "Case #" << z + 1 << ": ";
		if (n == 1 || m == 1) {
			cout << "YES" << endl;
		} else {
			if (getAns()) {
				cout << "YES" << endl;
			} else {
				cout << "NO" << endl;
			}
		}
	}

stopTimer();
	return 0;
}