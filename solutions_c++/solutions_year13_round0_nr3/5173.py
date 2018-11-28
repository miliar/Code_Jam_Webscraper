#include "stdio.h"

int N = 0;
long long resp[ 50 ];

bool f(long long X){
	long long n = X;
 	long long m = 0LL;
 	while (X > 0){
 		m *= 10LL;
 		m += X % 10;
 		X /= 10;
 	}
 	return n == m;
}

int main()
{
	long long num = 1LL;
	while ( num*num <= 100000000000000LL ){
		if ( f(num) && f(num*num) ) resp[ N++ ] = num*num;
		num++;
	}

	int T;
	long long A, B;
	int num_caso = 1;

	scanf("%d",&T);
	while ( T-- ){
		int cont = 0;
		scanf("%lld %lld",&A,&B);
		for (int i=0; i<N; i++){
			if ( A <= resp[i] && resp[i] <= B )
				cont++;
		}
		printf("Case #%d: %d\n", num_caso, cont);
		num_caso++;
	}

	return 0;
}
