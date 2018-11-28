#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <iostream>
#include <string>

using namespace std;



long int divisor[9];
long int j;




long int isprime(long int nb){
	
	if (nb % 2 == 0)
		return 2; 
    for(long int i=3; (i*i)<=nb; i+=2){
        if(nb % i == 0 ) {
			return i;
		}
    }
    return 0;
}



bool isvalid(long int *jc, long int N) {
	
	// Convert to base b
	for (long int b=2; b<=10; b++) {
		long int f=1;	
		long int nb=0;

		for (long int n=N-1; n>=0; n--) {
			nb += jc[n]*f;			
			f *= b;
		} 

		divisor[b-2] = isprime(nb);

		if (divisor[b-2] == 0)	{		
			return false;
		}
	}

	return true;
}

void permute(long int *jc, long int N, long int i, long int J) {
	if (j==J)
		return;

	if (i==N-1) {
	
		// Check if valid jamcode
		if (j<J) {
			if (isvalid(jc, N)) {
				// Prlong int jc			
				for (long int k=0; k<N; k++)
					cout << jc[k];
				for (long int b=2; b<=10; b++) {
					cout << " " << divisor[b-2];
				} 
				cout << endl;
				j++;
			}
		}

		return;
	}


	for (long int l=0; l<=1; l++) {
		// Get a new permutation number
		jc[i]=l;

		// Go on to next number
		permute(jc, N, i+1, J);
	}
}

int main() {
	FILE *fin = freopen("C-small-attempt0.in", "r", stdin);
	assert( fin!=NULL );
	FILE *fout = freopen("C-small-attempt0.out", "w", stdout);
	long int T,N,J;
	cin >> T;

	for (long int t=1; t<=T; t++) {
		cin >> N >> J;
		j=0;
		
		cout << "Case #" << t << ":" << endl;

		// Initialize jc
		long int *jc = new long int[N];
		for (long int k=0; k<N; k++)
			jc[k] = 0;
		jc[0] = 1;
		jc[N-1] = 1;

		permute(jc, N, 1,J);

		delete[] jc;
	}

	return 0;
}
