#include <stdio.h>
#include <algorithm>
using namespace std;

char s[110];
char g[110];
int cnt[110][110];

void solve(int test){
	int n;
	scanf("%d\n", &n);
	gets(s);
	int len = 0;
	for(int i = 0; s[i]; i++){
		g[len] = s[i];
		cnt[0][len] = 0;
		while(s[i] == g[len]){
			i++;
			cnt[0][len]++;
		}
		i--;
		len++;
	}
	g[len] = 0;
	for(int j = 1; j < n; j++){
		gets(s);
		int ptr = 0;
		for(int i = 0; s[i]; i++){
			cnt[j][ptr] = 0;
			while(s[i] == g[ptr]){
				i++;
				cnt[j][ptr]++;
			}
			if(cnt[j][ptr] == 0){
				puts("Fegla Won");
				return;
			}
			i--;
			ptr++;
		}
		if(ptr != len){
			puts("Fegla Won");
			return;
		}
	}
	int ans = 0;
	for(int i = 0; g[i]; i++){
		int res = 10000;
		for(int j = 1; j <= 100; j++){
			int sum = 0;
			for(int k = 0; k < n; k++)
				sum += abs(cnt[k][i] - j);
			if(sum < res)
				res = sum;
		}
		ans += res;
	}
	printf("%d\n", ans);
}

int main(){
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int tests;
	scanf("%d\n", &tests);
	for(int test = 1; test <= tests; test++){
		printf("Case #%d: ", test);
		solve(test);
	}
}