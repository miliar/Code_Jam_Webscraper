#include <stdio.h>
#include <string.h>
#define MAXS 1001

int work(int kk){
	int maxs, ans, current;
	char s[MAXS + 9];

	ans = 0;
	current = 0;
	scanf("%d %s\n", &maxs, &s);

	for (int i = 0; i <= maxs; i++){
		if (i > current){
			ans += i - current;
			current = i;
		}
		current += s[i] - 48;
	}

	printf("Case #%d: %d\n", kk + 1, ans);

	return 0;
}

int main(){
	int tc, i, j;
	freopen("1.in", "r", stdin);
	freopen("1.out", "w", stdout);
	scanf("%d", &tc);
	for (i = 0; i < tc; i++){
		work(i);
	}
	return 0;
}