#include <cstdio>

int main() {
	int t;
	scanf("%d", &t);
	for(int a = 0; a < t; a++) {
		char ttt[4][4];
		for(int i = 0; i < 4; i++)
			scanf(" %s", ttt[i]);
		bool x_won = false, o_won = false;
		int dots = 0;
		for(int i = 0; i < 4 && !x_won && !o_won; i++) {
			int x = 0, o = 0;
			for(int j = 0; j < 4; j++) {
				if(ttt[i][j] == 'X')
					x++;
				if(ttt[i][j] == 'O')
					o++;
				if(ttt[i][j] == '.')
					dots++;
				if(ttt[i][j] == 'T') {
					x++;
					o++;
				}
			}
			if(x == 4)
				x_won = true;
			if(o == 4)
				o_won = true;
		}
		for(int i = 0; i < 4 && !x_won && !o_won; i++) {
			int x = 0, o = 0;
			for(int j = 0; j < 4; j++) {
				if(ttt[j][i] == 'X')
					x++;
				if(ttt[j][i] == 'O')
					o++;
				if(ttt[j][i] == 'T') {
					x++;
					o++;
				}
			}
			if(x == 4)
				x_won = true;
			if(o == 4)
				o_won = true;
		}
		int x = 0, o = 0;
		for(int i = 0; i < 4 && !x_won && !o_won; i++) {
			if(ttt[i][i] == 'X')
				x++;
			if(ttt[i][i] == 'O')
				o++;
			if(ttt[i][i] == 'T') {
				x++;
				o++;
			}
		}
		if(x == 4)
			x_won = true;
		if(o == 4)
			o_won = true;
		x = 0;
		o = 0;
		for(int i = 0; i < 4 && !x_won && !o_won; i++) {
			if(ttt[3 - i][i] == 'X')
				x++;
			if(ttt[3 - i][i] == 'O')
				o++;
			if(ttt[3 - i][i] == 'T') {
				x++;
				o++;
			}
		}
		if(x == 4)
			x_won = true;
		if(o == 4)
			o_won = true;
		printf("Case #%d: ", a + 1);
		if(x_won)
			printf("X won\n");
		else
			if(o_won)
				printf("O won\n");
			else
				if(dots == 0)
					printf("Draw\n");
				else
					printf("Game has not completed\n");
	}
	return 0;
}
