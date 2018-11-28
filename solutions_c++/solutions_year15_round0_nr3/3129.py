#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
#include <memory.h>

using namespace std;

int a[10001][10001], used[10001][10001];
int A[10][10], B[10][10];

int code(char ch) {
	if (ch == 'i') return 2;
	if (ch == 'j') return 3;
	return 4;
}


pair<int, int> multiply(int x, int y, char ch) {
	pair<int, int> res(0, 1);
	if (used[x][y] == -1) res.second = -1;
	int c = code(ch);
	res.first = A[a[x][y]][c];
	res.second *= B[a[x][y]][c];
	return res;
}

int main() {
	A[1][1] = 1, A[1][2] = 2, A[1][3] = 3, A[1][4] = 4;
	A[2][1] = 2, A[2][2] = 1, A[2][3] = 4, A[2][4] = 3;
	A[3][1] = 3, A[3][2] = 4, A[3][3] = 1, A[3][4] = 2;
	A[4][1] = 4, A[4][2] = 3, A[4][3] = 2, A[4][4] = 1;	
	B[1][1] = B[1][2] = B[1][3] = B[1][4] = 1;
	B[2][1] = 1, B[2][2] = -1, B[2][3] = 1, B[2][4] = -1;
	B[3][1] = 1, B[3][2] = -1, B[3][3] = -1, B[3][4] = 1;
	B[4][1] = 1, B[4][2] = 1, B[4][3] = -1, B[4][4] = -1;
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int test;
	scanf("%d\n", &test);
	for (int tst = 1; tst <= test; ++tst) {
		int n, m;
		scanf("%d %d\n", &n, &m);
		string s;
		getline(cin, s);
		string st = s;
		for (int i = 2; i <= m; ++i) s += st;
		n = s.size();
		for (int i = 0; i < n; ++i) {
			for (int j = i; j < n; ++j) {
				if (i == j) {
					a[i][j] = code(s[i]);
					used[i][j] = 1;
				} else {
					pair<int, int> mult = multiply(i, j - 1, s[j]);
					a[i][j] = mult.first;
					used[i][j] = mult.second;
				}
	//			cout << i << " " << j << " " << a[i][j] << endl;
			}
		}
		bool ok = false;
		for (int i = 1; i < n; ++i) {
			for (int j = i; j < n; ++j) {  	
				if (used[0][i - 1] != 1 || used[i][j] != 1 || used[j + 1][n - 1] != 1) continue;
				if (a[0][i - 1] != 2 || a[i][j] != 3 || a[j + 1][n - 1] != 4) continue;
				ok = true;
			}
		}
		cout << "Case #" << tst << ": ";
		if (ok) cout << "YES" << endl; else cout << "NO" << endl;	
	}
	return 0;
}          