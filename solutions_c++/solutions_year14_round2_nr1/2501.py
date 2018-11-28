#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
#define MAXN 100
#define MAXL 100
int N;
char buf[MAXL+1];
int cnt[MAXN][MAXL];
char pat[MAXL];
int patN;
int ABS(int n) {
	if (n < 0)
		return -n;
	return n;
}
int main() {
	int T = 0;
	scanf("%d", &T);
	for (int t = 0; t < T; t++) {
		scanf("%d", &N);
		patN = 0;
		bool fail = false;
		for (int i = 0; i < N; i++) {
			scanf("%s", buf);
			if (fail)
				continue;
			if (i == 0) {
				for (char* c = buf; *c; c++) {
					if (c == buf || *c != *(c-1)) {
						pat[patN++] = *c;
						cnt[i][patN-1] = 1;
					} else {
						cnt[i][patN-1]++;
					}
				}
			} else {
				int patN0 = 0;
				for (char* c = buf; *c; c++) {
					if (c == buf || *c != *(c-1)) {
						if (patN0 >= patN || *c != pat[patN0]) {
							fail = true;
							break;
						}
						patN0++;
						cnt[i][patN0-1] = 1;
					} else {
						cnt[i][patN0-1]++;
					}
				}
				if (patN0 < patN)
					fail = true;
			}
		}/*
		if (fail) {
			printf("NA\n");
		} else {
			for (int j = 0; j < patN; j++)
				printf("%c ", pat[j]);
			printf("\n");
			for (int i = 0; i < N; i++) {
				for (int j = 0; j < patN; j++)
					printf("%d ", cnt[i][j]);
				printf("\n");
			}
		}*/
		int ans = 0;
		if (!fail) {
			for (int j = 0; j < patN; j++) {
				int targ = 0;
				for (int i = 0; i < N; i++)
					targ += cnt[i][j];
				targ /= N;
				int ans1 = 0, ans2 = 0;
				for (int i = 0; i < N; i++) {
					ans1 += ABS(cnt[i][j] - targ);
					ans2 += ABS(cnt[i][j] - (targ+1));
				}
				if (ans1 < ans2)
					ans += ans1;
				else
					ans += ans2;
			}
		}
		printf("Case #%d: ", t+1);
		if (fail)
			printf("Fegla Won\n");
		else
			printf("%d\n", ans);
	}
	return 0;
}

