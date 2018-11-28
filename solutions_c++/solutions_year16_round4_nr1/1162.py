#include <iostream>
#include <cstdio>
#include <vector>
using namespace std;

const int N = 13;
// 0 R 1 P 2 s
string c[3] = {"R", "P", "S"};
int t[3][2] =
	{ {0, 2}
	, {1, 0}
	, {2, 1}
	};
string s[N][3];
int a[N][3][3];
int itc;

void solve() {
	int n;
	cin >> n;
	int b[3];
	for (int i = 0; i < 3; i++) {
		cin >> b[i];
	}
	int w = -1;
	for (int i = 0; i < 3; i++) {
		bool eq = true;
		for (int j = 0; j < 3; j++) {
			eq = eq && b[j] == a[n][i][j];
		}
		if (eq) {
			w = i;
			break;
		}
	}
	if (w == -1) {
		puts("IMPOSSIBLE");
	} else {
		puts(s[n][w].c_str());
	}
}

int main() {
	cin.sync_with_stdio(false);
	for (int i = 0; i < 3; i++) {
		for (int j = 0; j < 3; j++) {
			a[0][i][j] = i == j;
		}
		s[0][i] = c[i];
	}
	for (int n = 1; n < N; n++) {
		for (int i = 0; i < 3; i++) {
			for (int j = 0; j < 3; j++) {
				a[n][i][j] = a[n-1][t[i][0]][j] + a[n-1][t[i][1]][j];
			}
			string x = s[n-1][t[i][0]];
			string y = s[n-1][t[i][1]];
			s[n][i] = x < y ? x+y : y+x;
		}
	}
	int ntc;
	cin >> ntc;
	for (itc = 1; itc <= ntc; itc++) {
		printf("Case #%d: ", itc);
		solve();
	}
}
