#include<stdio.h>

#define ll long long int

int main(){
	ll n, temp, N;
	int t,i, a[10]={0}, k;
	scanf("%d",&t);
	for( i = 1; i <= t; i++ ){
		scanf("%lld",&n);
		if ( n == 0 ){
			for( k =0; k <10; k++ )
				a[k] = i;
			printf("Case #%d: INSOMNIA\n",i);
		}
		else{
			k = 0;
			N = 0;
			while( k != 10 ){
				N += n;
				temp = N;
				while( temp != 0 && k != 10 ){
					if( a[temp%10] != i )
					{
						k++;
						a[temp%10] = i;
					}
					temp /= 10;
				}
				
			}
			printf("Case #%d: %lld\n", i, N);
		}
	}
	return 0;
}


