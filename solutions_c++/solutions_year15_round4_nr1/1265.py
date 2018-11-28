#include<iostream>
#include<algorithm>
#include<cstdio>
using namespace std;

const char UP = '^', DOWN = 'v', LEFT = '<', RIGHT = '>';
int r, c;
char board[111][111];

int impossible[111][111];

int main(){
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T;
	scanf("%d", &T);
	for (int tc = 1; tc <= T; tc++){
		printf("Case #%d: ", tc);

		scanf("%d%d", &r, &c);
		for (int i = 1; i <= r; i++)
			scanf("%s", &(board[i][1]));

		for (int i = 0; i < 111; i++)
			for (int j = 0; j < 111; j++)
				impossible[i][j] = 0;

		// UP
		for (int j = 1; j <= c; j++){
			int i = 1;
			while (i <= r && (board[i][j] == '.'))
				i++;
			if (i > r) continue;
			impossible[i][j] += (1 << 0);
		}

		// DOWN
		for (int j = 1; j <= c; j++){
			int i = r;
			while (i > 0 && (board[i][j] == '.'))
				i--;
			if (!i) continue;
			impossible[i][j] += (1 << 1);
		}

		// LEFT
		for (int i = 1; i <= r; i++){
			int j = 1;
			while (j <= c && (board[i][j] == '.'))
				j++;
			if (j > c) continue;
			impossible[i][j] += (1 << 2);
		}

		// RIGHT
		for (int i = 1; i <= r; i++){
			int j = c;
			while (j > 0 && (board[i][j] == '.'))
				j--;
			if (!j) continue;
			impossible[i][j] += (1 << 3);
		}

		int ans = 0;
		bool possible = true;

		for (int i = 1; i <= r; i++){
			for (int j = 1; j <= c; j++){
				if (impossible[i][j]){
					char here = board[i][j];
					int here_int = 0;
					switch (here){
					case UP: here_int = 1; break;
					case DOWN: here_int = 2; break;
					case LEFT: here_int = 4; break;
					case RIGHT: here_int = 8; break;
					}

					if (impossible[i][j] == 15) possible = false;

					if (here_int & impossible[i][j])
						ans++;
				}
			}
		}

		if (possible){
			printf("%d\n", ans);
		}
		else{
			printf("IMPOSSIBLE\n");
		}
	}
}