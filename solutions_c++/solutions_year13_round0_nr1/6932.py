#include <stdio.h>
#include <fstream>

using namespace std;
int main(int argc, char **argv){
	FILE *f = fopen(argv[1], "r");
	int T;

	fseek(f, 0, SEEK_END);
	long size = ftell(f);
	rewind(f);
	fscanf(f, "%d\n", &T);
	int done = ftell(f);

	char *buf = (char *) malloc(size - done);
	fread(buf, 1, size - done, f);
	fclose(f);

	char c;

	int i = 0;
	int rows [] = {0,0,0,0};
	int cols [] = {0,0,0,0};
	int diag [] = {0,0};
	bool has_dots;

	for (int case_num = 1; case_num <= T; ++case_num) {
		has_dots = false;
		rows[0] = rows[1] = rows[2] = rows[3] = 0;
		cols[0] = cols[1] = cols[2] = cols[3] = 0;
		diag[0] = diag[1] = 0;

		for (int row = 0; row < 4; ++row){
			for (int col = 0; col < 4; ++col){
				c = buf[i];
				++i;

				switch (c){
					case 'X':
						rows[row] |= 1;
						cols[col] |= 1;
						diag[0] |= 1&(row == col);
						diag[1] |= 1&(row + col == 3);
						break;
					case 'O':
						rows[row] |= 2;
						cols[col] |= 2;
						diag[0] |= 2*(row == col);
						diag[1] |= 2*(row + col == 3);
						break;
					case '.':
						has_dots = true;
						rows[row] = cols[col] = 3;
						diag[0] |= 3*(row == col);
						diag[1] |= 3*(row + col == 3);
				}
			}
			++i;
		}
		++i;
		printf("Case #%d: ", case_num);
		if (diag[0] == 1 or diag[1] == 1) {
			printf("X won\n");
			continue;
		}
		if (diag[0] == 2 or diag[1] == 2) {
			printf("O won\n");
			continue;
		}
		bool fin = false;
		for (int j = 0; j<4; ++j){
			if (rows[j] == 1 || cols[j] == 1) {
				printf("X won\n");
				fin = true;
				break;
			} else if (rows[j] == 2 || cols[j] == 2){
				printf("O won\n");
				fin = true;
				break;
			}
		}
		if (fin) continue;
		if (has_dots) {
			printf("Game has not completed\n");
			//printf("rows[0]=%d", rows[0]);
		} else {
			printf("Draw\n");
		}
	}

	free(buf);
	return 0;
}