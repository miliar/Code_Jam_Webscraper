#include<stdio.h>
#include<string.h>
int t, i, l, cnt, tt;
char cake[105];
int main() {
	//freopen("input.txt", "r", stdin);
	//freopen("output.txt", "w", stdout);
	
	scanf("%d", &t);
	for (tt=1;tt<=t;tt++) {
		scanf("%s", cake);
		l = strlen(cake);
		cake[l] = '+';
		cnt = 0;
		for (i=0;i<l;i++) {
			if (cake[i] != cake[i+1])
			cnt++;
		}
		printf("Case #%d: %d\n", tt, cnt);
	}
	return 0;
}
