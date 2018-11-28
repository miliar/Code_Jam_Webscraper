#include <iostream>
#include <cmath>
using namespace std;

int cont;

bool palindromo(long long int orig) {
	int num = orig;
	int rev = 0;
	int dig;

	do {
		dig = num % 10;
		rev = (rev * 10) + dig;
		num = num / 10;
	} while(num > 0);

	if(rev == orig)
		return true;
	else
		return false;
}

void revisar(long long int a, long long int b) {
	long long int limite = b / 2;
	
	for(int i=1;i<=limite;i++){
		if(((i*i) >= a) && ((i*i) <= b)) {
			if((palindromo(i)) && (palindromo(i*i))) {
				cont++;
			}
		}
	}
}

int main() {
	int t;
	long long int A;
	long long int B;
	cin >> t;

	for(int a=1;a<=t;a++) {
		cont = 0;
		cin >> A >> B;

		revisar(A,B);

		cout << "Case #" << a << ": " << cont << endl;
	}

	return 0;
}
