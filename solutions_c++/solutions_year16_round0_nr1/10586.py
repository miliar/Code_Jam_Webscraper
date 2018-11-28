#include <iostream>
#include <cstdio>

using namespace std;

int main() {
	int T, N;
	int a, b, data[10], counter, n, rem;
	long long int num;

	scanf("%d",&T);
	for( a = 1; a <= T; a ++ )  {
		scanf("%d",&N);
		if( N == 0 ) {
			printf("Case #%d: INSOMNIA\n",a);
			continue;
		}
		for( b = 0; b < 10; b ++ ) {
			data[b] = 1;		
		}
		counter = 10;
		n = 0;
		while( counter != 0 ) {
			n += 1;
			num = (long long int)n * (long long int)N;
			while( num != 0 ) {
				rem = num % 10;
				if( data[rem] == 1 ) {
					data[rem] = 0;
					counter --;
				}
				num /= 10;
			}
		}
		num = (long long int)n * (long long int)N;
		printf("Case #%d: %lld\n",a,num);
	}
	return 0;
}
