#include <iostream>
#include <string.h>
#include <math.h>
using namespace std;

    int numero[10];
    int aNumero (int a) {
	int i = 0;
	
	while (a != 0) {
	    numero[i] = a % 10;
	    a = a / 10;
	    i++;
	}
	return i;
    }

    int Palindromo (int a) {
	if (a < 10) {
	    return 0;
	}
	int x = aNumero(a)-1;
	for(int i = 0; i <= x; i++) {
	    if (numero[i] == numero[x-i]) {
		continue;
	    }
	    else
	    {
		return 1;
	    }
	}
	return 0 ;
    }

    int main () {
	int T,co,i,k,a,b;
	int A[100], B[100];
	k = 0;
	cin >> T;
	do {
	    cin >> A[k] >> B[k];
	    k++;
	} while (k < T);
	
	k = 0;
	while (k < T) {
	    co = 0;
	    a = ceil(sqrt(A[k]));
	    b = sqrt(B[k]);
	    for (i=a; i < b+1; i++) {
		if (Palindromo(i) == 0) {
		    if (Palindromo(i*i) == 0) {
			co++;
		    }
		}
	    }
	    cout << "Case #" << k+1 << ": ";
	    cout << co << "\n";
	    k++;
	}


    }
    