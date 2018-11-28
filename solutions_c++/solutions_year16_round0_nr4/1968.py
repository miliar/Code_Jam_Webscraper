#include <stdio.h>

long long int getPos(int k, int c, int i){
	long long int res = 1;
	long long int aux = 1;
	for(int j = 0; j < c; j++){
		if(i <= k){
			res+=aux*(i-1);
		}
		i++;
		aux *= k;
	}
	return res;
}

int main(){
	int t;
	scanf(" %d", &t);
	for(int l = 1; l <= t; l++){
		int k, c, s;
		scanf(" %d %d %d", &k, &c, &s);
		if(s*c < k){
			printf("Case #%d: IMPOSSIBLE\n", l);
			continue;
		}
		printf("Case #%d:", l);
		
		for(int i = 1; i <= k; i+=c){
			printf(" %lld", getPos(k, c, i));
		}
		printf("\n");
	}
	return 0;
}