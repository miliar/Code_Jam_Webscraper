#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <set>
#include <string>
using namespace std;
typedef long long ll;
const int N = 6;
const ll MOD = 1000000009;
char v[N][N];
int go[4][2] = {1, 0, 0, 1, 1, 1, 1, -1};
int jude(int x, int y) {
	return x >= 0 && y >= 0 && x < 4 && y < 4;
}
int ok(int x, int y) {
	int t1, t2, t3;
	for (int j = 0; j < 4; ++j) {
		t1 = t2 = t3 = 0;
		for (int i = 0; i < 4; ++i) {
			int tx = x + i * go[j][0];
			int ty = y + i * go[j][1];
			if (!jude(tx, ty)) break;
			if (v[tx][ty] == 'T') t3 ++;
			else if (v[tx][ty] == 'O') t2 ++;
			else if (v[tx][ty] == 'X') t1 ++;
			if (t1 == 3 && t3 == 1 || t1 == 4) return 1;
			if (t2 == 3 && t3 == 1 || t2 == 4) return -1;
		}
	}
	return 0;
}
int main() {
#ifndef ONLINE_JUDGE
	freopen("C:\\Users\\Slon\\Desktop\\A-large.in","r",stdin);
	freopen("C:\\Users\\Slon\\Desktop\\out.txt","w",stdout);
#endif

	int T, cs = 0;
	scanf("%d", &T);
	while (T--) {
		for (int i = 0; i < 4; ++i)
			scanf("%s", v[i]);
		int f1, f2;
		f1 = f2 = 0;
		for (int i = 0; i < 4; ++i) {
			for (int j = 0; j < 4; ++j) {
				if (v[i][j] == '.') f2 = 1;
				else {
					int t = ok(i, j);
					if (t == -1) f1 = -1;
					else if (t == 1) f1 = 1;
				}
			}
		}
		printf("Case #%d: ", ++cs);
		if (f1 == 1) printf("X won\n"); 
		else if (f1 == -1) printf("O won\n");
		else if (f2 == 0) printf("Draw\n");
		else printf("Game has not completed\n");
	}
	return 0;
}