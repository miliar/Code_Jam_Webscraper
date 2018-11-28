#include <stdio.h>

char infile[] = "A-large.in";
char outfile[] = "out.txt";
int table[100][100];
int used[100][100];

int main() {
	FILE* fin = fopen(infile, "rb");

	if(!fin) {
		printf("file not found\n");
		return 0;
	}

	FILE* fout = fopen(outfile, "wb");

	int T, SM;
	fscanf(fin, "%d", &T);
	int R, C;

	for(int i = 0; i < T; ++ i) {
		fscanf(fin, "%d%d", &R, &C);

		for(int r = 0; r < R; ++ r) {
			for(int c = 0; c < C; ++ c) {
				used[r][c] = 0;
				while(true) {
					char ch;
					fscanf(fin, "%c", &ch);

					if(ch == '.') {
						table[r][c] = 0; break;
					} else if(ch == '>') {
						table[r][c] = 1; break;
					} else if(ch == '^') {
						table[r][c] = 2; break;
					} else if(ch == '<') {
						table[r][c] = 3; break;
					} else if(ch == 'v') {
						table[r][c] = 4; break;
					} 
				}
			}
		}

		bool notPossible = false;
		int changed = 0;

		for(int r = 0; r < R && !notPossible; ++ r) {
			for(int c = 0; c < C && !notPossible; ++ c) {
				if(!used[r][c] && table[r][c] != 0) {
					int fInv = 0;

					int dir = table[r][c];
					int x = c;
					int y = r;
					int lx = c;
					int ly = r;
					used[r][c] = 1;

					while(true) {
						if(dir == 1) {
							x += 1;
						} else if(dir == 2) {
							y -= 1;
						} else if(dir == 3) {
							x -= 1;
						} else if(dir == 4) {
							y += 1;
						}

						if(x < 0 || y < 0 || x >= C || y >= R) {
							if(lx == c && ly == r) {
								//notPossible = true;
								//break;
								++ fInv;
								if(fInv == 4) {
									notPossible = true;
									break;
								}

								dir = (table[r][c] + fInv - 1)%4 + 1;
								x = c;
								y = r;
								continue;
							}
							++ changed;
							break; // can be fixed
						}

						if(used[y][x]) {
							break; // secured
						}

						if(table[y][x] != 0) {
							dir = table[y][x];
							lx = x;
							ly = y;
							used[y][x] = 1;
						}
					}

					if(!notPossible && fInv) {
						++ changed; // first changed
					}
				}
			}
		}

		if(notPossible) {
			fprintf(fout, "Case #%d: IMPOSSIBLE\n", i + 1);
		} else {
			fprintf(fout, "Case #%d: %d\n", i + 1, changed );
		}
	}


	fcloseall();
	return 0;
}