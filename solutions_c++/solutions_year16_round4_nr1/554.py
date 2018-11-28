#include <iostream>
#include <cstdio>
#include <cstring>  
#include <string>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <ctime>
#include <algorithm>
#include <iomanip>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <cassert>
#include <bitset>

using namespace std;

const int maxn = 13;

string ans[maxn][3];
int num[maxn][3][3];

void update(int i, int x, int y, int z) {
	ans[i][x] = ans[i - 1][y] + ans[i - 1][z];
	for (int k = 0; k < 3; ++k) {
		num[i][x][k] = num[i - 1][y][k] + num[i - 1][z][k];
	}
}

int main() {
	memset(num, 0, sizeof(num));
	ans[0][0] = "P";
	num[0][0][0] = 1;
	ans[0][1] = "R";
	num[0][1][1] = 1;
	ans[0][2] = "S";
	num[0][2][2] = 1;
	for (int i = 1; i < maxn; ++i) {
		update(i, 0, 0, 1);
		update(i, 1, 0, 2);
		update(i, 2, 1, 2);
	}
	int cases;
	scanf("%d", &cases);
	for (int o = 0; o < cases; ++o) {
		int n, r, p, s;
		scanf("%d %d %d %d", &n, &r, &p, &s);
		int f = -1;
		for (int i = 0; i < 3; ++i) {
			if (num[n][i][0] == p && num[n][i][1] == r && num[n][i][2] == s) {
				f = i;
				break;
			}
		}
		printf("Case #%d: ", o + 1);
		if (f == -1) {
			printf("IMPOSSIBLE\n");
		} else {
			printf("%s\n", ans[n][f].c_str());
		}
	}
	return 0;
}
