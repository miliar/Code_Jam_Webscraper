#include <stdio.h>
#include <iostream>
#include <string.h>
using namespace std;

char num[10][20] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", 
	"FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};

int T, n;
char s[20000];
int ans[10];
int c[26];
int use[10][26];

bool dfs() {
	//printf("n%d\n", n);
	bool flag;
	if (n == 0) {
		return true;
	}
	for (int i = 0;i < 10;++i){
		flag = true;
		for (int j = 0;j < 26;++j)
			if (use[i][j] > c[j]) {
				flag = false;
				break;
			}

		if (flag) {
			ans[i]++;
			//printf("na%d\n", n);
			for (int j = 0;j < 26;++j){
				c[j] -= use[i][j];
				n -= use[i][j];
			}
			// printf("nb%d\n", n);
			// printf("%d\n", i);
			if (dfs()) return true;
			for (int j = 0;j < 26;++j){
				c[j] += use[i][j];
				n += use[i][j];
			}
			ans[i]--;

		}
	}
	return false;
}

void process() {
	for (int i = 0;i < 10;++i)
		ans[i] = 0;
	for (int i =0 ;i < 26;++i)
		c[i] =0;
	n = strlen(s);
	for (int i = 0;i < n;++i) c[s[i]-'A']++;

	// for (int i= 0;i < 26;++i)
	// 	printf("%c %d\n", i+'A', c[i]);
	dfs();
	//if (!dfs()) printf("true");
}

void count() {
	for (int i = 0;i < 10;++i){
		for (int j = 0;j < 26;++j)
			use[i][j] = 0;
		for (int j = 0;j < strlen(num[i]); ++j)
			use[i][num[i][j]-'A']++;
	}
	// for (int j = 0; j < 26;++j)
	// 	printf("%c %d\n", j+'A', use[0][j]);
}

int main() {
	freopen("A-small.in", "r", stdin);
	freopen("A-small.out", "w", stdout);
	scanf("%d", &T);
	count();
	for (int i = 1;i <= T;++i) {
		scanf("%s", s);
		process();
		printf("Case #%d: ", i);
		for (int i = 0;i < 10;++i)
			for (int j = 0;j < ans[i];++j)
				printf("%d", i);
		printf("\n");
	}

	return 0;
}