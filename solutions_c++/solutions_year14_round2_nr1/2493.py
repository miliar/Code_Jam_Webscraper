#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#define MIN(x,y) x<y?x:y
int n, len, ln[105][105], ave[105];
char str[105][105], let[105][105];
bool Fwon() {
	for(int i = 1; i < n; i++)
		if(strcmp(let[i], let[i-1])) return true;
	return false;
}
int main(){
	int t, tc = 1;
	for(scanf("%d", &t); tc <= t; tc++) {
		scanf("%d", &n);
		memset(ln, 0, sizeof(ln[0])*n);
		for(int i = 0; i < n; i++) {
			scanf("%s", str[i]);
			len = strlen(str[i]);
			int k = 0;
			for(int j = 0; j < len; j++) {
				if(j == 0 || str[i][j] != str[i][j-1])
					let[i][k++] = str[i][j];
				ln[i][k-1]++;
			}
			let[i][k] = '\0';
		}
		if(Fwon()) {
			printf("Case #%d: Fegla Won\n", tc);
			continue;
		}
		len = strlen(let[0]);
		memset(ave, 0, sizeof(ave));
		for(int i = 0; i < n; i++)
			for(int j = 0; j < len; j++) ave[j] += ln[i][j];
		for(int j = 0; j < len; j++) ave[j] /= n;
		int ans[2] = {0};
		for(int i = 0; i < n; i++) {
			for(int j = 0; j < len; j++) {
				ans[0] += abs(ln[i][j] - ave[j]);
				ans[1] += abs(ln[i][j] - (ave[j]+1));
			}
		}
		printf("Case #%d: %d\n", tc, MIN(ans[0], ans[1]));
	}
	return 0;
}
