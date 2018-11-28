#include <iostream>
#include <cstdio>
#include <cmath>
int onedigit ( int num ) 
{
//	printf ( "%din one\n", num );
	return ( num >= 0 && num < 10 );
}

bool chk_pali ( int num, int *num1)
{
	if ( onedigit (num ) ){
//		printf ( "in one %d\t%d\n", num, *num1 % 10 );
		if ( num == *num1%10 ) {
			*num1 /= 10;
			return true;
		}else {
			return false;
		}
	}

	if ( chk_pali ( num/10, num1 )) {
//		printf ( "in chk pali %d\t%d\n", num, *num1 );
		if ( num % 10 == *num1 % 10 ){
			*num1 /= 10;
		       return true;
		}else {
	 		return false;
		}		
	}
}

int main()
{
	int num,num2,test;
	scanf ( "%d", &test );
	int u = 1;
	while ( u <= test ){
		scanf ( "%d%d", &num, &num2);
		int u1 = 0;
		for ( int i = num; i <= num2; i++) {
			int *num1 = new int ( i );
			if ( chk_pali ( i, num1 ) ){
				int u_s = sqrt ( i );
				if ( u_s * u_s == i ) {
					int *num1 = new int ( u_s );
					if ( chk_pali ( u_s, num1 ) ) {
						u1++;
					}
				}
			}
		}
		printf ( "Case #%d: %d\n", u,u1 );
		u++;
	}
	return 0;
}
	
