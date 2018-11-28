#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

string lexmin[3][15];
int n, r, p, s, t;

string min(string a, string b) {
	for (int i = 0; i < a.length(); ++i) {
		if (a[i] < b[i])
			return a;
		if (a[i] > b[i])
			return b;
	}

	return a;
}

//r = 0, p = 1, s = 2;
void comp(int x, int j) {
	if (j == 0) {
		if (x == 0)
			lexmin[x][j] = "R";
		if (x == 1)
			lexmin[x][j] = "P";
		if (x == 2)
			lexmin[x][j] = "S";
		return;
	}

	if (x == 0)
		lexmin[x][j] = min(lexmin[0][j-1]+lexmin[2][j-1], lexmin[2][j-1]+lexmin[0][j-1]);
	if (x == 1)
		lexmin[x][j] = min(lexmin[0][j-1]+lexmin[1][j-1], lexmin[1][j-1]+lexmin[0][j-1]);
	if (x == 2)
		lexmin[x][j] = min(lexmin[2][j-1]+lexmin[1][j-1], lexmin[1][j-1]+lexmin[2][j-1]);
}

void run(int t) {
	cout << "Case #" << t+1 << ": ";
	cin >> n >> r >> p >> s;
	for (int i = 0; i < n; ++i) {
		int r1 = (r+p+s)/2-p;
		int s1 = (r+p+s)/2-r;
		int p1 = (r+p+s)/2-s;
		if (p1 < 0 || r1 < 0 || s1 < 0) {
			cout << "IMPOSSIBLE\n";
			return;
		}
		r = r1, p = p1, s = s1;
	}

	if (r == 1)
		cout << lexmin[0][n] << "\n";
	if (p == 1)
		cout << lexmin[1][n] << "\n";
	if (s == 1)
		cout << lexmin[2][n] << "\n";
}

int main() {
	cin >> t;
	for (int i = 0; i <= 12; ++i)
		for (int j = 0; j < 3; ++j)
			comp(j, i);
	for (int i = 0; i < t; ++i)
		run(i);
}
