#include <stdio.h>
int maxs, a[2048];

void solve(int testcase){
	int standsum = 0, count = 0;
	for (int i = 0; i <= maxs; i++){
		if (standsum >= i)
			standsum += a[i];
		else
			if (a[i] == 0)
				continue;
			else {
				count += i - standsum;
				standsum += a[i] + i - standsum;
			}
	}
	printf("Case #%d: %d\n", testcase, count);
	return;
}


int main(void){
	int t;
	char c;
	scanf("%d", &t);
	for (int i = 0; i < t; i++){
		scanf("%d", &maxs);
		scanf("%c", &c); //eat blank
		for (int j = 0; j <= maxs; j++){
			scanf("%c", &c);
			a[j] = c - '0';
		}
		solve(i + 1);
	}
	return 0;
}
