#include <stdio.h>
int main(void)
{
	int T;
	int ans;
	int Smax;
	char temp;
	int sum;
	
	scanf(" %d", &T);
	for(int i = 1; i <= T; i++){
		scanf(" %d", &Smax);
		sum = 0;
		ans = 0;
		for(int j = 0; j <= Smax; j++) {
			scanf(" %c", &temp);
			if(sum < j) {
				ans += j-sum;
				sum = j;
			}
			sum += temp-48;
		}
		printf("Case #%d: %d\n", i, ans);
	}
	return 0;
}