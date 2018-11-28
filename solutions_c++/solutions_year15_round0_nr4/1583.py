#include <bits/stdc++.h>

using namespace std;

int G[10][10][10];

int main()
{
	int cnt = 0;
	for (int X = 1; X <= 4; X++) {
		for (int R = 1; R <= 4; R++) {
			for (int C = R; C <= 4; C++) {
				if (R * C % X != 0) {
					G[X][R][C] = G[X][C][R] = 2;
					continue;
				}
				if (X == 1 || X == 2) {
					G[X][R][C] = G[X][C][R] = 1;
					continue;
				}
				if (X > R && X > C) {
					G[X][R][C] = G[X][C][R] = 2;
					continue;
				}
				//cout << X << ' ' << R << ' ' << C << endl;
			}
		}
	}
	G[3][1][3] = G[3][3][1] = 2;
	G[3][2][3] = G[3][3][2] = 1;
	G[3][3][3] = 1;
	G[3][3][4] = G[3][4][3] = 1;

	G[4][1][4] = G[4][4][1] = 2;
	G[4][2][4] = G[4][4][2] = 2;
	G[4][3][4] = G[4][4][3] = 1;
	G[4][4][4] = 1;

	for (int X = 1; X <= 4; X++) {
		for (int Y = 1; Y <= 4; Y++) {
			for (int Z = 1; Z <= 4; Z++) {
				if (G[X][Y][Z] == 0)  {
					//cout << X << ' ' << Y << ' '<< Z << endl;
				}
			}
		}
	}
	int T;
	cin >> T;
	static char str[10][50] = {"", "GABRIEL", "RICHARD"};
	for (int cas = 1; cas <= T; cas++) {
		int X, R, C;
		cin >> X >> R >> C;
		//cout << G[X][R][C] << endl;
		printf("Case #%d: %s\n", cas, str[G[X][R][C]]);
	}
}
