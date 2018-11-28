#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<algorithm>
#include<vector>
#include<queue>
#include<stack>

#define int_max 2000000000 // 20djr
#define int_min -2000000000 // -20djr
#define long_max ((long long)int_max*(long long)int_max) // 400kung
#define long_min -((long long)int_max*(long long)int_max) // -400kung

char ans[3000];
int dp[27];
int num[10];
char str[3000];

int main(void) {
	int T;
	int N;
	int i, j, k;

	freopen("A-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);

	scanf("%d", &T);

	for (i = 1; i <= T; i++) {
		scanf("%s\n", &str);
		int length = strlen(str);
		for (j = 0; j <= 26; j++) {
			dp[j] = 0;
		}
		for (j = 0; j < 10; j++) {
			num[j] = 0;
		}
		for (j = 0; j < length; j++) {
			dp[str[j] - 'A' + 1]++;
		}

		num[0] = dp['Z' - 'A' + 1];
		dp['O' - 'A' + 1] -= dp['Z' - 'A' + 1];
		num[2] = dp['W' - 'A' + 1];
		dp['O' - 'A' + 1] -= dp['W' - 'A' + 1];
		dp['T' - 'A' + 1] -= dp['W' - 'A' + 1];
		num[4] = dp['U' - 'A' + 1];
		dp['O' - 'A' + 1] -= dp['U' - 'A' + 1];
		dp['F' - 'A' + 1] -= dp['U' - 'A' + 1];
		num[6] = dp['X' - 'A' + 1];
		dp['S' - 'A' + 1] -= dp['X' - 'A' + 1];
		num[8] = dp['G' - 'A' + 1];
		dp['T' - 'A' + 1] -= dp['G' - 'A' + 1];
		num[3] = dp['T' - 'A' + 1];
		num[5] = dp['F' - 'A' + 1];
		num[7] = dp['S' - 'A' + 1];
		dp['N' - 'A' + 1] -= dp['S' - 'A' + 1];
		num[1] = dp['O' - 'A' + 1];
		dp['N' - 'A' + 1] -= dp['O' - 'A' + 1];
		num[9] = dp['N' - 'A' + 1] / 2;

		int index = 0;
		for (j = 0; j < 10; j++) {
			if (num[j] > 0) {
				num[j]--;
				ans[index] = j + '0';
				index++;
				j--;
				continue;
			}
		}
		ans[index] = 0;

		printf("Case #%d: %s\n", i, ans);
	}


}