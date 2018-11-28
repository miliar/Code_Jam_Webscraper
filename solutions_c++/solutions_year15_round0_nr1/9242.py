#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int main() {
	int smax;
	int T;
	char temp;
	int num[1002];
	scanf("%d",&T);
	int turn = 1;
	while(T--) {
		int ans = 0;
		int count = 0;
		scanf("%d", &smax);
		for(int i = 0; i <= smax; i++) {
			scanf(" %c", &temp);
			num[i] = temp-'0';
		}
		for(int i = 0; i <= smax; i++) {
			if(count < i) {
				ans += (i-count);
				count += (i-count);
			}
			count += num[i];
		}
		printf("Case #%d: %d\n", turn, ans);
		turn++;
	}
	return 0;
}

