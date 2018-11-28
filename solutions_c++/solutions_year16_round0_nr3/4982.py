#include <iostream>
#include <string.h>
#include <cstdlib>
#include <cmath>
#include <math.h>

using namespace std;

/* run this program using the console pauser or add your own getch, system("pause") or input loop */
/*
int div(char ps, int n) 
{
	if( ps[n-1]=='-' ) {
		int a = swap(ps,n,n-1);
		int b = swap(ps,n,n);
		return min(a,b);
	}
	else
	{
		return div(ps,n-1);
	}
}

int main(int argc, char** argv) {
	
	int T;
	cin >> T;
	
	while( T-- ) {
		
		char ps[100]; // pancake stack
		char n;
		cin >> pstack;
		n = strlen(ps);
		
		div(ps,n);
		swap(ps,n,n);
	}
	
	return 0;
}*/
/*AAAA
int main(int argc, char** argv) {
	
	int T,c=0;
	cin >> T;
	
	while( T-- ) {
		c++;
		
		int N;
		cin >> N;
		
		int M = 0;
		int k = 1;
		int D[10] = {0};
		bool keepon = true;
		
		while(keepon) {
		
			M = k*N;
			k++;
			
			if( M==0 )
			 {
			 	cout << "Case #" << c << ": INSOMNIA" << endl;
			 	break;
			 }
			
			char sM[100];
			itoa(M,sM,10);
			//cout << sM << endl;
			
			for( int i=0; i<strlen(sM);i++)
				D[sM[i]-48] = 1;
				
			int ones = 0;
			for( int i=0; i<10;i++)
				ones += D[i];
			if(ones==10){
				cout << "Case #" << c << ": " << M << endl;
				keepon = false;
			}
			
		}
	}
	
	return 0;
}***/
#define LONG unsigned long long
LONG dividor(LONG n) {
	
	for( LONG i=3; i<=sqrt(n); i++)
	{
		if(n % i == 0)
			return i;
	}
	
	return 0;
}

LONG valueOf(string n, int base_of_n){
 
    char aux[n.size()], *end;
    strcpy(aux,n.c_str());
    return strtoll(aux,&end,base_of_n);
 
}



int main(int argc, char** argv) {

	int T;
	cin >> T;
	int c = 0;
	
	while( T-- ) {
		
		int J, N;
		cin >> N >> J;
		
		cout << "Case #" << ++c << ":" << endl;
		
		LONG a = pow(2,N-1) + 1;
		LONG b = pow(2,N);
		
		for( unsigned long i=a; i<b && J>0; i+=2 ){
			
			LONG D[11] = {0};
			bool fail = false;
			
			char g[100];
			itoa(i,g,2);
			
			int ones = 0;
			for( int j=2; j<=10; j++ ) {
				
				LONG k = valueOf(g,j);
				LONG d = dividor(k);
				//cout << k << endl;
				
				if(d==0){
					fail = true;
					break;
				}
				else {
					D[j] = d;
					ones++;
				}
			}
			/*
			cout << g << " | ";
			for( int j=2; j<=10; j++)
					cout << (D[j]>0) << " ";
			cout << endl;
			*/
			// Output
			if( fail==false ) {
				J--;
				
				char n[100];
				itoa(i,n,2);
				cout << n << " ";
				for( int j=2; j<=10; j++)
					cout << D[j] << " ";
				cout << endl;
			}
		}
		
	}
	
	return 0;
}
