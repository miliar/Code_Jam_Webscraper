
#include <iostream>
#include <iomanip>
#include <algorithm>
#include <cmath>
#include <vector>
#include <stack>
#include <queue>
#include <deque>
#include <map>
#include <set>
#include <functional>
#include <cctype>
#include <climits>
#include <string>
#include <utility>
using namespace std;

void prn(int testcase, int answer) {
	cout << "Case #" << testcase << ": ";
	cout << answer;
	cout << "\n";
}

const int maxn = (int)1e4;
int v[maxn][maxn];
int amt[6];

int di[4] = {0, 0, 1, -1};
int dj[4] = {1, -1, 0, 0};

bool good(int i, int j, int r, int c) {
	return 0 <= i && i < r && 0 <= j && j < c;
}

void offer(int r, int c, int n, int t) {
	for (int i = 0; i < 6; ++i) amt[i] = 0;

	for (int i = 0; i < r; ++i) {
		for (int j = 0; j < c; ++j) {
			if ((i + j) % 2 == 0) {
				v[i][j] = 1;
			} else {
				v[i][j] = 0;
			}
		}
	}

	for (int i = 0; i < r; ++i) {
		for (int j = 0; j < c; ++j) {
			if (v[i][j] == 1) {
				++amt[0];
			} else {
				int cnt = 0;
				int ni, nj;
				for (int s = 0; s < 4; ++s) {
					ni = i + di[s];
					nj = j + dj[s];
					if (good(ni, nj, r, c) && v[ni][nj] == 1) { // nnecessary
						++cnt;
					}
				}
				++amt[cnt];
			}
		}
	}

	int answer1 = 0;
	int save = n;
	while (n --> 0) {
		for (int s = 0; s < 6; ++s) {
			if (amt[s] > 0) {
				answer1 += s;
				--amt[s];
				break;
			}
		}
	}
	n = save;

	for (int i = 0; i < 6; ++i) amt[i] = 0;

	for (int i = 0; i < r; ++i) {
		for (int j = 0; j < c; ++j) {
			if ((i + j) % 2 == 0) {
				v[i][j] = 0;
			} else {
				v[i][j] = 1;
			}
		}
	}

	for (int i = 0; i < r; ++i) {
		for (int j = 0; j < c; ++j) {
			if (v[i][j] == 1) {
				++amt[0];
			} else {
				int cnt = 0;
				int ni, nj;
				for (int s = 0; s < 4; ++s) {
					ni = i + di[s];
					nj = j + dj[s];
					if (good(ni, nj, r, c) && v[ni][nj] == 1) { // nnecessary
						++cnt;
					}
				}
				++amt[cnt];
			}
		}
	}

	int answer2 = 0;
	while (n --> 0) {
		for (int s = 0; s < 6; ++s) {
			if (amt[s] > 0) {
				answer2 += s;
				--amt[s];
				break;
			}
		}
	}
	prn(t, min(answer1, answer2));
}

void solve() {
	int test;
	cin >> test;
	for (int t = 1; t <= test; ++t) {
		int r, c, n;
		cin >> r >> c >> n;
		if (r > c) swap(r, c); //r <= c
		offer(r, c, n, t);
	}
}

int main () {
//#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
//#endif

	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	solve();

	return 0;
}