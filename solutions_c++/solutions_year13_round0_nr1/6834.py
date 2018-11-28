#include <iostream>
#include <cstdio>
#include <cstdlib>
using namespace std;

int checkLine(char a[][16], int sx, int sy, int dx, int dy) {
	int xc = 0, oc = 0, tc = 0;
	for(int i = 0; i < 4; ++i){
		xc += a[sx][sy] == 'X';
		oc += a[sx][sy] == 'O';
		tc += a[sx][sy] == 'T';
		sx += dx;
		sy += dy;
	}
	if(xc == 4 || (xc == 3 && tc == 1)){
		return 0;
	}
	if(oc == 4 || (oc == 3 && tc == 1)){
		return 1;
	}
	return 2;
}

int main() {
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	char str[4][16];
	int T;
	scanf("%d", &T);
	for(int t = 1; t <= T; ++t){
		bool full = true;
		for(int i = 0; i < 4; ++i){
			scanf("%s", str[i]);
			for(int j = 0; j < 4; ++j){
				full &= str[i][j] != '.';
			}
		}

		int cnt[3] = {0, 0, 0};
		for(int r = 0; r < 4; ++r){
			cnt[checkLine(str, r, 0, 0, 1)]++;
		}
		for(int c = 0; c < 4; ++c){
			cnt[checkLine(str, 0, c, 1, 0)]++;
		}
		cnt[checkLine(str, 0, 0, 1, 1)]++;
		cnt[checkLine(str, 0, 3, 1, -1)]++;
		printf("Case #%d: ", t);
		if(cnt[0] > 0){
			puts("X won");
		}
		else if(cnt[1] > 0){
			puts("O won");
		}
		else if(full){
			puts("Draw");
		}
		else{
			puts("Game has not completed");
		}

	}
	return 0;
}
