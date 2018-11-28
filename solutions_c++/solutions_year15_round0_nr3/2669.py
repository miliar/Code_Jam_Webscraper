#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cstdio>
#include <cmath>

using namespace std;

#define INF 1000000007

int table[5][5] = {
	0, 0, 0, 0, 0,
	0, 1, 2, 3, 4,
	0, 2, -1, 4, -3,
	0, 3, -4, -1, 2,
	0, 4, 3, -2, -1
};

inline int get(int c, int r) {
	if (c < 0 && r < 0) {
		return table[-c][-r];
	} 
	if (c < 0) {
		return -table[-c][r];
	}
	if (r < 0) {
		return -table[c][-r];
	}
	return table[c][r];
}

inline int num(char c) {
	if (c == '1') return 1;
	if (c == 'i') return 2;
	if (c == 'j') return 3;
	if (c == 'k') return 4;
}

int a[10000][10000];

string solve() {
	long long L, X, size;
	string s;
	cin >> L >> X >> s;
	size = L * X;
	for (int i = 0; i < X; i++) {
		for (int j = 0; j < L; j++) {
			a[i * L + j][i * L + j] = num(s[j]);
		}
	}
	for (int i = 0; i < size; i++) {
		for (int j = i + 1; j < size; j++) {
			a[i][j] = get(a[i][j - 1], a[j][j]);
		}
	}
	for (int i = 0; i + 2 < size; i++) {
		for (int j = i + 1; j + 1 < size; j++) {
			if (a[0][i] == 2 && a[i + 1][j] == 3 && a[j + 1][size - 1] == 4) {
				return "YES";
			}
		}
	}
	return "NO";
}

int main() {
	std::ios_base::sync_with_stdio(false);
	std::cin.tie(nullptr);
	
	int T;
	cin >> T;
	for (int i = 1; i <= T; i++) {
		cout << "Case #" << i << ": ";
		cout << solve() << '\n';
	}
	
	return 0;
}

