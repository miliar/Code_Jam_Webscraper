#include<stdio.h>


int num[10];

bool count(long long number) {

	while(number>0) {
		num[number%10] +=1;
		number = number/10;
	}

	for(int i=0; i<10; i++)  {
		if( 0 == num[i])
			return false;
	}
	return true;
}


int main()
{
	int i,j, k, T, N;

	//while(scanf("%d %d %d", &i, &j, &k)!= EOF) {
	//	prlong longf("%d %d %d", i, j, k);
	//}


	scanf("%d", &T);
	long long Nin;
	for(int ca = 1; ca<=T; ++ca) {
		for(i=0; i<10; i++) num[i] = 0;
		scanf("%lld", &Nin);

		long long N = Nin;
		j = 1;
		while(false == count(N)) {
			if(0 == N) {
				break;
			}
			j++;
			N = Nin*j;	

			//printf("--- Case #%d: %lld\n", ca, N);
		}	
		if (0 == N) {
			printf("Case #%d: INSOMNIA\n", ca);

		} else {
			printf("Case #%d: %lld\n", ca, N);
		}
	}



}
