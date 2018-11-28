
#include <iostream>
#include <stdio.h>
#include <stdlib.h>
using namespace std;


int main() {

	int T,I=1;
	cin >> T;
	int N,L,A,B,K;
	while (T--) {
		cin >> A >> B >> K;
		N=0;
		for(int i=0; i<A; i++)
			for(int j=0; j<B; j++)
				if ((i&j)<K) N++;

		cout << "Case #" << I << ": ";
		cout << N;
		cout << endl;
		I++;
	}
	return 0;
}
