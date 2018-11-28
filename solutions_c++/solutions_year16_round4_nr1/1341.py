#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<algorithm>
#include<vector>
#include<queue>
#include<stack>
#include<functional>
#include<math.h>

using namespace std;

#define int_max 2000000000 // 20djr
#define int_min -2000000000 // -20djr
#define long_max ((long long)int_max*(long long)int_max) // 400kung
#define long_min -((long long)int_max*(long long)int_max) // -400kung

char ans[3][5000];

void make(int N);

int main(void) {
	int T;
	int N, R, P, S;
	int i, j, k;
	int temp;

	freopen("A-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);

	scanf("%d", &T);

	for (i = 1; i <= T; i++) {
		scanf("%d %d %d %d", &N, &R, &P, &S);
		temp = 1;
		for (int j = 1; j <= N; j++) {
			temp *= 2;
		}
		make(N);
		printf("Case #%d: ", i);
		if(max(R, max(P, S)) != temp / 3 + 1 || min(R, min(P, S)) != temp / 3){
			printf("IMPOSSIBLE\n");
			continue;
		}
		int length = strlen(ans[0]);
		if (N % 2 == 0) {
			if (max(R, max(P, S)) == R) {
				int cou = 0;
				for (int k = 0; k < 3; k++) {
					cou = 0;
					for (int j = 0; j < length; j++) {
						if (ans[k][j] == 'R') {
							cou++;
						}
					}
					if (cou == R) {
						printf("%s\n", ans[k]);
					}
				}
			}
			else if (max(R, max(P, S)) == P) {
				int cou = 0;
				for (int k = 0; k < 3; k++) {
					cou = 0;
					for (int j = 0; j < length; j++) {
						if (ans[k][j] == 'P') {
							cou++;
						}
					}
					if (cou == P) {
						printf("%s\n", ans[k]);
					}
				}
			}
			else {
				int cou = 0;
				for (int k = 0; k < 3; k++) {
					cou = 0;
					for (int j = 0; j < length; j++) {
						if (ans[k][j] == 'S') {
							cou++;
						}
					}
					if (cou == S) {
						printf("%s\n", ans[k]);
					}
				}
			}
		}
		else {
			if (min(R, min(P, S)) == R) {
				int cou = 0;
				for (int k = 0; k < 3; k++) {
					cou = 0;
					for (int j = 0; j < length; j++) {
						if (ans[k][j] == 'R') {
							cou++;
						}
					}
					if (cou == R) {
						printf("%s\n", ans[k]);
					}
				}
			}
			else if (min(R, min(P, S)) == P) {
				int cou = 0;
				for (int k = 0; k < 3; k++) {
					cou = 0;
					for (int j = 0; j < length; j++) {
						if (ans[k][j] == 'P') {
							cou++;
						}
					}
					if (cou == P) {
						printf("%s\n", ans[k]);
					}
				}
			}
			else {
				int cou = 0;
				for (int k = 0; k < 3; k++) {
					cou = 0;
					for (int j = 0; j < length; j++) {
						if (ans[k][j] == 'S') {
							cou++;
						}
					}
					if (cou == S) {
						printf("%s\n", ans[k]);
					}
				}
			}
		}
	}
}

void make(int N) {
	char temp[3][5000];
	temp[0][0] = 'R';
	temp[0][1] = 0;
	temp[1][0] = 'P';
	temp[1][1] = 0;
	temp[2][0] = 'S';
	temp[2][1] = 0;

	char temp2[3][5000];

	for (int i = 1; i <= N; i++) {
		if (strcmp(temp[0], temp[2]) < 0) {
			strcpy(temp2[0], temp[0]);
			strcat(temp2[0], temp[2]);
		}
		else{
			strcpy(temp2[0], temp[2]);
			strcat(temp2[0], temp[0]);
		}

		if (strcmp(temp[0], temp[1]) < 0) {
			strcpy(temp2[1], temp[0]);
			strcat(temp2[1], temp[1]);
		}
		else {
			strcpy(temp2[1], temp[1]);
			strcat(temp2[1], temp[0]);
		}

		if (strcmp(temp[1], temp[2]) < 0) {
			strcpy(temp2[2], temp[1]);
			strcat(temp2[2], temp[2]);
		}
		else {
			strcpy(temp2[2], temp[2]);
			strcat(temp2[2], temp[1]);
		}

		strcpy(temp[0], temp2[0]);
		strcpy(temp[1], temp2[1]);
		strcpy(temp[2], temp2[2]);
	}

	strcpy(ans[0], temp[0]);
	strcpy(ans[1], temp[1]);
	strcpy(ans[2], temp[2]);
}