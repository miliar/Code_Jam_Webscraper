#include <cstdio>

int table[50][50];
int size;
int num[99][50];
int isUsed[99] = {};
int ansId;
bool isAnsHorizontal;

bool isWin;

bool isOK(int pos, int rowId, bool isHorizontal) {
	int i;
	if (isHorizontal) {
		for (i = 0; i < pos; i++) {
			if (table[pos][i] != -1 && table[pos][i] != num[rowId][i]) {
				return false;
			}
		}
		return true;
	} else {
		for (i = 0; i < pos; i++) {
			if (table[i][pos] != -1 && table[i][pos] != num[rowId][i]) {
				return false;
			}
		}
		return true;
	}
}

void calc(int pos) {
	int i, j, k;

	if (pos == size) {
		if (isAnsHorizontal) {
			for (i = 0; i < size; i++) {
				if (i > 0) printf(" ");
				printf("%d", table[ansId][i]);
			}
		} else {
			for (i = 0; i < size; i++) {
				if (i > 0) printf(" ");
				printf("%d", table[i][ansId]);
			}
		}
		
		printf("\n");
		isWin = true;
		return;
	}

	int minNum = 9999;
	for (i = 0; i < 2 * size - 1; i++) {
		if (isUsed[i] > 0) continue;

		if (minNum > num[i][pos]) {
			minNum = num[i][pos];
		}
	}

	int rowId[2];
	int countId = 0;
	for (i = 0; i < 2 * size - 1; i++) {
		if (isUsed[i] > 0) continue;

		if (minNum == num[i][pos]) {
			rowId[countId] = i;
			countId++;
			isUsed[i]++;
		}
	}

	int oldTable[2][50];
	for (i = 0; i < size; i++) {
		oldTable[0][i] = table[pos][i];
		oldTable[1][i] = table[i][pos];
	}

	if (countId == 1) {
		if (isOK(pos, rowId[0], true)) {
			for (i = 0; i < size; i++) {
				table[pos][i] = num[rowId[0]][i];
			}
			ansId = pos;
			isAnsHorizontal = false;
			calc(pos + 1);
			if (isWin) return;
			for (i = 0; i < size; i++) {
				table[pos][i] = oldTable[0][i];
			}
		}
		if (isOK(pos, rowId[0], false)) {
			for (i = 0; i < size; i++) {
				table[i][pos] = num[rowId[0]][i];
			}
			ansId = pos;
			isAnsHorizontal = true;
			calc(pos + 1);
			if (isWin) return;
			for (i = 0; i < size; i++) {
				table[i][pos] = oldTable[1][i];
			}
		}

		isUsed[rowId[0]]--;
	} else if (countId == 2) {
		if (isOK(pos, rowId[0], true) && isOK(pos, rowId[1], false)) {
			for (i = 0; i < size; i++) {
				table[pos][i] = num[rowId[0]][i];
				table[i][pos] = num[rowId[1]][i];
			}
			calc(pos + 1);
			if (isWin) return;
			for (i = 0; i < size; i++) {
				table[pos][i] = oldTable[0][i];
				table[i][pos] = oldTable[1][i];
			}
		}
		if (isOK(pos, rowId[0], false) && isOK(pos, rowId[1], true)) {
			for (i = 0; i < size; i++) {
				table[pos][i] = num[rowId[1]][i];
				table[i][pos] = num[rowId[0]][i];
			}
			calc(pos + 1);
			if (isWin) return;
			for (i = 0; i < size; i++) {
				table[pos][i] = oldTable[0][i];
				table[i][pos] = oldTable[1][i];
			}
		}

		isUsed[rowId[0]]--;
		isUsed[rowId[1]]--;
	} else {
		printf("ERROR!!! [%d]\n", countId);
	}
}

void calcCase() {
	scanf("%d", &size);
	int i, j;
	for (i = 0; i < size * 2 - 1; i++) {
		for (j = 0; j < size; j++) {
			scanf("%d", &num[i][j]);
		}
		isUsed[i] = 0;
	}
	for (i = 0; i < size; i++) {
		for (j = 0; j < size; j++) {
			table[i][j] = -1;
		}
	}
	isWin = false;
	calc(0);
}

int main() {
	int tc, t;

	scanf("%d", &tc);
	for (t = 1; t <= tc; t++) {
		printf("Case #%d: ", t);
		calcCase();
	}

	return 0;
}