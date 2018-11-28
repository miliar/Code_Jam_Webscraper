#include<stdio.h>
int main(){

	int t, i, j, n,k,s;
	scanf("%d",&t);
	for( int c = 1; c <= t; c++ ){
		scanf("%d%d%d",&n,&k,&s);
		printf("Case #%d: ", c);
		while( --s )
			printf("%d ", s+1);
		printf("1\n");
	}
	return 0;
}

