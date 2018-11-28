#include <stdio.h>
int main() {
	int t;
	scanf("%d", &t);
	for(int tcount = 1; tcount <= t; tcount++) {
		int sMax;
		char shyness[1005];
		int sum = 0, friends = 0;
		scanf("%d", &sMax);
		scanf(" %s", shyness);
		for(int i = 0; i <= sMax; i++) {
			//printf("%c ", shyness[i]);
			shyness[i] -= '0';
			if(i <= sum) sum += int(shyness[i]);
			else {
				//printf("%d %d\n", tcount, friends);
				friends += i-sum;
				sum = i+int(shyness[i]);
			}
		}
		printf("Case #%d: %d\n", tcount, friends);
	}
	return 0;
}