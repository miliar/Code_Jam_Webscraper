#include <stdio.h>

int main(){
	int ct, cn = 0;
	scanf("%d", &ct);
	while(ct--){
		int n, sum = 0, r = 0;
		scanf("%d", &n);
		char s[n + 1];
		scanf("%s", s);
		for(int i = 0; i <= n; i++){
			if(i > sum) r += i - sum, sum += i - sum;
			sum += s[i] - '0';
		}
		printf("Case #%d: %d\n", ++cn, r);
	}
	
	return 0;
}