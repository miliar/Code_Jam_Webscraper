#include <iostream>
#include <stdio.h>

using namespace std;

void solve(int step) {

	char d[4][4];
	for(int i = 0; i < 4; ++i) {
		for(int j = 0; j < 4; ++j) {
			char t = 0;
			scanf("%c", &t);
			d[i][j] = t;
		}
		scanf("\n");
	}

	scanf("\n");

	int p = 0;
	for(int i = 0; i < 4; ++i) {
		int z = 0, x = 0;
		for(int j = 0; j < 4; ++j) {
			z += d[i][j] == 'O' || d[i][j] == 'T';
			x += d[i][j] == 'X' || d[i][j] == 'T';
			p += d[i][j] == '.';
		}
		if (x == 4 || z == 4) {
			char r = x == 4 ? 'X' : 'O';
			printf("Case #%d: %c won\n", step, r);
			return;
		}
	}

	for(int i = 0; i < 4; ++i) {
		int z = 0, x = 0;
		for(int j = 0; j < 4; ++j) {
			z += d[j][i] == 'O' || d[j][i] == 'T';
			x += d[j][i] == 'X' || d[j][i] == 'T';
		}
		if (x == 4 || z == 4) {
			char r = x == 4 ? 'X' : 'O';
			printf("Case #%d: %c won\n", step, r);
			return;
		}
	}

	int z = 0, x = 0;
	for(int i = 0; i < 4; ++i) {	
		z += d[i][i] == 'O' || d[i][i] == 'T';
		x += d[i][i] == 'X' || d[i][i] == 'T';
	}

	if (x == 4 || z == 4) {
		char r = x == 4 ? 'X' : 'O';
		printf("Case #%d: %c won\n", step, r);
		return;
	}
	
	z = 0, x = 0;
	for(int i = 0; i < 4; ++i) {	
		z += d[i][ 4 - i - 1] == 'O' || d[i][4 - i - 1] == 'T';
		x += d[i][ 4 - i - 1] == 'X' || d[i][4 - i - 1] == 'T';
	}

	if (x == 4 || z == 4) {
		char r = x == 4 ? 'X' : 'O';
		printf("Case #%d: %c won\n", step, r);
		return;
	}

	if (p == 0) {
		printf("Case #%d: Draw\n", step);
		return;
	}

	printf("Case #%d: Game has not completed\n", step);
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int t;
	scanf("%d\n", &t);
	for(int i = 0; i < t; ++i) {
		solve(i + 1);
	}
}