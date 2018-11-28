#include <cstdio>

char c[4][4];
#define XWON 0
#define OWON 1
#define DRAW 2
#define NOTCOMPLETE 3

int t_x, t_y; // position of T

bool hasdot = false;

int doIt() {
	//row check 

	int i, j;
	for (i = 0; i < 4; ++i) {
		if ( c[i][0] == c[i][1] && 
			c[i][0] == c[i][2] &&
			c[i][0] == c[i][3] ) {

			if (c[i][0] == 'X')
				return XWON;
			else if (c[i][0] == 'O')
				return OWON;

		}
	}

	for (j = 0; j < 4 ; ++j) {
		if (c[0][j] == c[1][j] &&
			c[0][j] == c[2][j] &&
			c[0][j] == c[3][j]) {
			if (c[0][j] == 'X')
				return XWON;
			else if (c[0][j] == 'O')
				return OWON;
			}
		}

	if(c[0][0] == c[1][1] &&
			c[0][0] == c[2][2] &&
			c[0][0] == c[3][3] ) {
			if (c[0][0] == 'O')
				return OWON;
			else if (c[0][0] == 'X')
				return XWON;
		} 

	if (c[3][0] == c[2][1] &&
		c[3][0] == c[1][2] &&
		c[3][0] == c[0][3]) {
		if (c[3][0] == 'X') {
			return XWON;
		} else if (c[3][0] == 'O')
			return OWON;
	}

	// test T t_x, t_y
	int a[3];
	int idx = 0;
	for (j = 0; j < 4; ++j) {
		if (j == t_y)
			continue;
		a[idx++] = c[t_x][j] - 'T';
	}
	if (a[0] == a[1] &&
		a[0] == a[2]) {
			if (c[t_x][0] == 'X'  || c[t_x][1] == 'X') return XWON;
			else if (c[t_x][0] == 'O'  || c[t_x][1] == 'O') return OWON;
	}

	idx = 0;
	for (i = 0; i < 4; ++i) {
		if ( i == t_x)
			continue;
		a[idx++] = c[i][t_y] - 'T';
	}

	if (a[0] == a[1] &&
		a[0] == a[2]) {
			if (c[0][t_y] == 'X'  || c[1][t_y] == 'X') return XWON;
			else if (c[0][t_y] == 'O'  || c[1][t_y] == 'O') return OWON;
	}


	if (t_x + t_y == 3) {
		if (t_x == 0) {
			if (c[1][2] == c[2][1] &&
				c[1][2] == c[3][0]) {
				if (c[1][2] == 'X') return XWON;
				else if (c[1][2] == 'O') return OWON;
			}
		} else if (t_x == 1) {
			if (c[0][3] == c[2][1] &&
				c[0][3] == c[3][0]) {
				if (c[0][3] == 'X') return XWON;
				else if (c[0][3] == 'O') return OWON;
			}
		} else if (t_x == 2) {
			if (c[0][3] == c[1][2] &&
				c[0][3] == c[3][0]) {
				if (c[0][3] == 'X') return XWON;
				else if (c[0][3] == 'O') return OWON;
			}
		} else {
			if (c[1][2] == c[0][3] &&
				c[1][2] == c[2][1]) {
				if (c[1][2] == 'X') return XWON;
				else if (c[1][2] == 'O') return OWON;
			}
		}

	}

	if (t_x == t_y) {
		if (t_x == 0) {
			if (c[1][1] == c[2][2] &&
				c[1][1] == c[3][3]) {
				if (c[1][1] == 'X') return XWON;
				else if (c[1][1] == 'O') return OWON;
			}
		} else if (t_x == 1) {
			if (c[0][0] == c[2][2] &&
				c[0][0] == c[3][3]) {
				if (c[0][0] == 'X') return XWON;
				else if (c[0][0] == 'O') return OWON;
			}
		} else if (t_x == 2) {
			if (c[1][1] == c[0][0] &&
				c[1][1] == c[3][3]) {
				if (c[1][1] == 'X') return XWON;
				else if (c[1][1] == 'O') return OWON;
			}
		} else {
			if (c[1][1] == c[2][2] &&
				c[1][1] == c[0][0]) {
				if (c[1][1] == 'X') return XWON;
				else if (c[1][1] == 'O') return OWON;
			}
		}
	}

	if (!hasdot) return DRAW;
	else return NOTCOMPLETE;
}
int main() {
	FILE *pFin = fopen("A-small-attempt0.in", "r");
	FILE *pFout = fopen("out.txt", "w");
	char cc;
	int n;
	fscanf(pFin, "%d\n", &n);

	int i, j , k ;
	for (i = 0; i < n; ++i) {
		hasdot = false;
		
		for (j = 0; j < 4; ++j) {
			for (k = 0; k < 4; ++k) {
		
				fscanf(pFin, "%c", &c[j][k]);
				if (c[j][k] == 'T') {
					t_x = j;
					t_y = k;
				} else if (c[j][k] == '.') hasdot = true;
			}
			cc = fgetc(pFin);
		}

		if (i != n - 1)
			cc = fgetc(pFin);

		fprintf(pFout, "Case #%d: ", i + 1);
		int ret = doIt();
		if (ret == XWON) fprintf(pFout, "X won\n");
		else if (ret == OWON) fprintf(pFout, "O won\n");
		else if (ret == DRAW) fprintf(pFout, "Draw\n");
		else if (ret == NOTCOMPLETE) fprintf(pFout, "Game has not completed\n");	

	}

	fclose(pFin);
	fclose(pFout);
	return 0;
}