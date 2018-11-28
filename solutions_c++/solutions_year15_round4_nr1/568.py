#include <stdio.h>
#include <stdlib.h>
#include <algorithm>
#include <vector>
#include <stack>
#include <queue>
#include <string>
#include <string.h>
#include <map>
#include <set>
#include <math.h>


using namespace std;


int T, R, C;
char m[200][200];

int solve()
{
	int cnt = 0;

	for (int i = 0; i < R; i++) {
		for (int j = 0; j < C; j++) {
			int flag = 0;
			int check = 0;
			if (m[i][j] != '.') {
				for (int k = i-1; k >= 0; k--) {
					if (m[k][j] != '.') {
						flag = 1;
						if (m[i][j] == '^')
							check = 1;
					}
				}

				for (int k = i+1; k < R; k++) {
					if (m[k][j] != '.') {
						flag = 1;
						if (m[i][j] == 'v')
							check = 1;
					}
				}

				for (int k = j-1; k >= 0; k--) {
					if (m[i][k] != '.') {
						flag = 1;
						if (m[i][j] == '<')
							check = 1;
					}
				}

				for (int k = j+1; k < C; k++) {
					if (m[i][k] != '.') {
						flag = 1;
						if (m[i][j] == '>')
							check = 1;
					}
				}

				if (flag == 0)return -1;
				if (check == 0)cnt++;
			}
		}
	}
	return cnt;
}

int main()
{
	scanf(" %d", &T);

	for (int cas = 1; cas <= T; cas++) {
		scanf(" %d %d", &R, &C);

		for (int i = 0; i < R; i++) {
			for (int j = 0; j < C; j++) {
				scanf(" %c",&m[i][j]);
			}
		}

		int res = solve();
		if (res < 0)
			printf("Case #%d: IMPOSSIBLE\n", cas);
		else
			printf("Case #%d: %d\n", cas, res);
	}



	return 0;
}