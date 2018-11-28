#include <stdio.h>

char str[1002];

int main() {
	int t;
	
	scanf("%d", &t);
	
	for(int i = 1; i <= t; i++) {

		int n;

		scanf("%d", &n);
		scanf("%s", str);
		
		int result = 0, finish = n+1, sum = 0;
		
		for(int j = 0; j < finish; j++) {
			
			int person = str[j] - '0';
			
			int remain = j - sum;

			if(remain > 0) {
				result += remain;
				sum += remain;
			}
			
			sum += person;   
		}
		
		printf("Case #%d: %d\n", i, result);
	}

	return 0;
}