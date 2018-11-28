#include <iostream>
#include <string.h>
#include <cstdlib>


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
}
