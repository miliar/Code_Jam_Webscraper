#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <algorithm>	


char S[101];
char temp[101];
void swap(int a, int b) {
	for (int i = a; i <= b; i++)
		temp[i] = S[i];
	for (int i = a; i <= b; i++) {
		//S[i] = temp[b - i];
		if (temp[b - i] == '-')
			S[i] = '+';
		else 
			S[i] = '-';
	}
}
int dfs(int n) {
	if (n == 0) {
		if (S[0] == '+')
			return 0;
		else 
			return 1;
	}
	int res = INT_MAX;
	if (S[n] == '+')
		return dfs(n - 1);
	else {
		if (S[0] == '-') {
			swap(0, n);
			return 1 + dfs(n - 1);
		}
		else {// +가 나올때까지 내려감
			int d = n;
			while (S[--d] == '-');
			swap(0, d);
			return 1 + dfs(n);
		}
	}
	return res;
}

int main() {
	FILE* in = fopen("problem.txt", "r");
	FILE* out = fopen("solve.txt", "w");

	int T;
	fscanf(in,"%d", &T);
	int times = 0;
	while (T >= ++times) {
		for (int i = 0; i <= 100; i++) {
			S[i] = 0;
			temp[i] = 0;
		}
		fscanf(in, "%s", S);
		int n = 0;
		while (S[n+1] != 0) {
			n++;
		}
		printf("%s", S);
		int res = dfs(n);
		fprintf(out, "Case #%d: %d\n", times, res);
		
	}
}