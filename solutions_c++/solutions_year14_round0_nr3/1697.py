#include<stdio.h>
#include<vector>

using namespace std;

int map[20][20];


bool Near(int row, int col,int c) {
	if (col != 0) {
		if (map[row][col - 1] == c) return true;
		if (map[row + 1][col - 1] == c) return true;
		if (row != 0 && map[row - 1][col - 1] == c) return true;
	}
	if (row != 0 && map[row - 1][col] ==c) return true;
	if (map[row + 1][col] == c) return true;
	if (map[row][col + 1] ==c) return true;
	if (row != 0 && map[row - 1][col + 1] == c) return true;
	if (map[row + 1][col + 1] == c) return true;
	return false;
}
void Clean(int R, int C) {
	int i, j;
	for (i = 0; i < R; i++) {
		for (j = 0; j < C; j++) {
			if (map[i][j] != -1) map[i][j] = 0;
		}
	}
}
bool uncover(int R, int C) {
	int i, j;
	for (i = 0; i < R; i++) {
		for (j = 0; j < C; j++) {
			if (map[i][j] == 1) {
				if (!Near(i, j, -2)) return false;
			}
		}
	}
	return true;
}

void Mapping(int row, int col, int R, int C) {		// R끝에 -2가 있는ㄱ 묹
	int i, j;
	if (map[row][col] != 0) return;
	map[row][col] = -2;
	if (row > 0) {
		Mapping(row - 1, col, R, C);
		if (col > 0) Mapping(row - 1, col - 1, R, C);
		if (col < C - 1) Mapping(row - 1, col + 1, R, C);
	}

	if (row < R - 1 && col < C-1) Mapping(row + 1, col + 1, R, C);
	if (row < R - 1) Mapping(row + 1, col, R, C);
	if (col < C - 1) Mapping(row, col + 1, R, C);

	if (col > 0) {
		Mapping(row, col - 1, R, C);
		if (row < R - 1) Mapping(row + 1, col - 1, R, C);
	}
}

void Setting(int R, int C) {
	int i, j,row,col;
	int count = 0;
	
	for (row = 0; row < R; row++) {
		for (col = 0; col < C; col++) {
			if (map[row][col] == -1) {
				if (map[row][col + 1] != -1)map[row][col + 1] = 1;
				if (col != 0) {
					if (map[row][col - 1] != -1)map[row][col - 1] = 1;
					if (map[row+1][col - 1] != -1)map[row + 1][col - 1] = 1;
					if (row != 0&&map[row-1][col-1]!=-1) map[row - 1][col - 1] = 1;
				}

				if (map[row+1][col] != -1)map[row + 1][col] = 1;
				if (map[row+1][col + 1] != -1)map[row + 1][col + 1] = 1;
				if (row != 0){
					if (map[row-1][col + 1] != -1)map[row - 1][col + 1] = 1;
					if (map[row-1][col] != -1)map[row - 1][col] = 1;
				}
			}
		}
	}
}
bool Search(int R, int C) {
	int i, j;
	for (i = 0; i < R; i++) {
		for (j = 0; j < C; j++) {
			if (map[i][j] == 0) return false;
		}
	}
	return true;
}

bool MineSwipping(int row, int col, int count, int R, int C, int M) {
	int i, j;
	if (count == M) {
		Setting(R, C);
		if (R*C - M == 1) {
			for (i = 0; i < R; i++) {
				for (j = 0; j < C; j++) if (map[i][j] == 1) map[i][j] = -2;
			}
			return true;
		}

		bool stop = false;
		for (i = 0; i < R; i++) {
			for (j = 0; j < C; j++) {
				if (map[i][j] == 0) {
					stop = true;
					break;
				}
			}
			if (stop) break;
		}
		if (!stop) {
			Clean(R, C);
			return false;
			
		}

		Mapping(i, j, R, C);

		if (!uncover(R, C)) {
			Clean(R, C);
			return false;
		}

		if (Search(R, C)) return true;
		else {
			Clean(R, C);
			return false;
		}
	}

	map[row][col] = -1;
	for (i = row; i < R; i++) {
		if (i == row) j = col+1;
		else j = 0;
		for (; j < C; j++) {
			if (MineSwipping(i, j, count+1, R, C, M)) return true;
		}
	}
	map[row][col] = 0;
	return false;
}



int main()  {
	int t, i, j, k;
	int  R, C, M;
	bool check = false;
	bool click = false;
	FILE* f = fopen("C-small-attempt6.in", "r+");
	FILE*f1 = fopen("C-small-attempt.out", "w+");
	fscanf(f, "%d", &t);
	for (i = 0; i < t; i++){
		fscanf(f, "%d %d %d", &R, &C, &M);

		fprintf(f1, "Case #%d:\n", i + 1);
		for (j = 0; j < R+1; j++) {
			for (k = 0; k < C+1; k++) map[j][k] = 0;
		}
		check = false;
		click = false;

		if (M == 0) {
			map[0][0] = -2;
			check = true;
		}
		else {
			for (j = 0; j < R; j++) {			// initial setting
				for (k = 0; k < C; k++) {
					if (MineSwipping(j, k, 0, R, C, M) == true) {
						check = true;
						break;
					}
				}
				if (check) break;
			}
		}

		if (check) {
			for (j = 0; j < R; j++) {
				for (k = 0; k < C; k++) {
					if (map[j][k] == -1) fprintf(f1, "*");
					else if ((map[j][k] == -2) && click == false) {
						fprintf(f1, "c");
						click = true;
					}
					else fprintf(f1, ".");
				}
				fprintf(f1, "\n");
			}
		}
		else fprintf(f1, "Impossible\n");
	}
	fclose(f);
	fclose(f1);
	return 0;
}