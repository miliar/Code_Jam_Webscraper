#include <cstdio>
#include <list>
#include <iostream>

#pragma warning(disable:4996)

using namespace std;

int t,n;
char stringAlpa[2001];

int main() {
	freopen("input.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	
	scanf("%d", &t);
	for (int i = 1; i <= t; i++) {
		scanf("%s", stringAlpa);

		int flag[16] = { 0 };
		int rlt[10] = { 0 };
		//Z E R O N E T W H F U I V S X G

		for (int z = 0; stringAlpa[z] != '\0'; z++) {
			if (stringAlpa[z] == 'Z') flag[0]++;
			else if (stringAlpa[z] == 'E') flag[1]++;
			else if (stringAlpa[z] == 'R') flag[2]++;
			else if (stringAlpa[z] == 'O') flag[3]++;
			else if (stringAlpa[z] == 'N') flag[4]++;
			else if (stringAlpa[z] == 'E') flag[5]++;
			else if (stringAlpa[z] == 'T') flag[6]++;
			else if (stringAlpa[z] == 'W') flag[7]++;
			else if (stringAlpa[z] == 'H') flag[8]++;
			else if (stringAlpa[z] == 'F') flag[9]++;
			else if (stringAlpa[z] == 'U') flag[10]++;
			else if (stringAlpa[z] == 'I') flag[11]++;
			else if (stringAlpa[z] == 'V') flag[12]++;
			else if (stringAlpa[z] == 'S') flag[13]++;
			else if (stringAlpa[z] == 'X') flag[14]++;
			else flag[15]++;
		}
		
		if (flag[0] != 0) {
			rlt[0] = flag[0];
			flag[1] = flag[1] - flag[0];
			flag[2] = flag[2] - flag[0];
			flag[3] = flag[3] - flag[0];
			flag[0] = 0;
		}

		if (flag[7] != 0) {
			rlt[2] = flag[7];
			flag[6] = flag[6] - flag[7];
			flag[3] = flag[3] - flag[7];
			flag[7] = 0;
		}

		if (flag[10] != 0) {
			rlt[4] = flag[10];
			flag[9] = flag[9] - flag[10]; // F
			flag[3] = flag[3] - flag[10]; // O
			flag[2] = flag[2] - flag[10]; // R
			flag[10] = 0;
		}

		if (flag[14] != 0) {
			rlt[6] = flag[14];
			flag[13] = flag[13] - flag[14];
			flag[11] = flag[11] - flag[14];
			flag[14] = 0;
		}

		if (flag[15] != 0) {
			rlt[8] = flag[15];
			flag[5] = flag[5] - flag[15];
			flag[11] = flag[11] - flag[15];
			flag[8] = flag[8] - flag[15];
			flag[6] = flag[6] - flag[15];
			flag[15] = 0;
		}

		if (flag[3] != 0) {
			rlt[1] = flag[3];
			flag[5] = flag[5] - flag[15];
			flag[4] = flag[4] - flag[15];
			flag[3] = 0;
		}

		if (flag[6] != 0) {
			rlt[3] = flag[6];
			flag[8] = flag[8] - flag[6];
			flag[2] = flag[2] - flag[6];
			flag[5] = flag[5] - flag[6];
			flag[5] = flag[5] - flag[6];
			flag[6] = 0;
		}

		if (flag[9] != 0) {
			rlt[5] = flag[9];
			flag[11] = flag[11] - flag[9];
			flag[12] = flag[12] - flag[9];
			flag[5] = flag[5] - flag[9];
			flag[9] = 0;
		}

		if (flag[11] != 0) {
			rlt[9] = flag[11];
		}

		if (flag[13] != 0) {
			rlt[7] = flag[13];
		}

		printf("Case #%d: ", i);
		for (int q = 0; q < 10; q++) {
			for (; rlt[q] > 0; rlt[q]--) {
				printf("%d", q);
			}
		}
		printf("\n");

	}
	return 0;
}

