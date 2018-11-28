#include <stdio.h>
#include <string.h>
#include <iostream>
#include <string>

int main(){
	int t, i, j, ct, tc = 0;
	long long a, b, k;
	scanf("%d", &t);
	while(t--){
		scanf("%lld %lld %lld", &a, &b, &k);
		ct = 0;
		for(i = 0; i < a; i++)
			for(j = 0; j < b; j++)
				if((i & j) < k)
					ct++;
		printf("Case #%d: %d\n", ++tc, ct);
	}
	return 0;
}
