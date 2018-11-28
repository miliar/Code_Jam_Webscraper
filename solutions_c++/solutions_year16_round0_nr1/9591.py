#include <bits/stdc++.h>

using namespace std;

void checkDigits( int n, bool b[]){
	for( int i = 0; n != 0; i++ ){
		int r = n % 10;
		n /= 10;
		b[r] = true;	
	}
}

bool slept( bool b[]){
	for( int  i = 0; i < 10; i++ ){
		if( !b[i] )
			return false;	
	}
	return true;
}

int main(){
	int T;
	scanf("%d\n", &T);
	
	for( int t = 0; t < T; t++ ){
		int n, kn;
		scanf("%d\n", &n);
		if( n == 0 ){
			printf( "case #%d: INSOMNIA\n", t+1 );
			continue;
		}
		kn = n;
		bool in[10];
		memset( in, 0, 10 );
		for( int  k = 2; k < 100; k++ ){
			checkDigits(kn, in);
			if( slept(in) ){
				printf( "case #%d: %d\n", t+1, kn);
				break;
			}
			kn = k*n;
		}	
	}
}
