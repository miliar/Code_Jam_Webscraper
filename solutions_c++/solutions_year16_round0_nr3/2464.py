#include <iostream>
#include <cmath>
using namespace std;

void genNextBin(bool * in, int k);
long long getPrime(long long in);
long long toBase(bool * in, int base, int n);

int main() {
	int numCases;
	cin >> numCases;
	cout << "Case #1:\n";
	for(int i=0; i<numCases; i++){
		int n, j;
		cin >> n >> j;
		int count = 1;
		bool bin[j];
		bin[0] = true;
		bin[n-1] = true;
		for(int a = 1; a < n-1; a++)
			bin[a] = false;
		while(count <= j){
			long long interpreted;
			bool valid = true;
			long long divisors [9] = {0,0,0,0,0,0,0,0,0};
			/*cout << "Current Guess: ";
			for(int a = n-1; a >= 0; a--)
				cout << bin[a];
			cout << "\n";*/
			for(int base = 2; base < 11; base++){
				long long interpreted = toBase(bin, base, n);
				//cout << "Base " << base << ": " << interpreted << "\n";
				divisors[base-2] = getPrime(interpreted);
			}
			for(int i=0; i < 9; i++){
				valid = (divisors[i] == -1) ? false : valid;
			}
			if(valid){
				count ++;
				for(int a = n-1; a >= 0; a--)
					cout << bin[a];
				for(int i=0; i < 9; i++){
					cout << " " << divisors[i];
				}
				cout << "\n";
			}
			genNextBin(bin, n);
		}
	}
	return 0;
}

long long getPrime(long long in){
	long long lim = sqrt(in);
	for(long long x = 2; x < lim; x++){
		if((in % x) == 0)
			return x;
	}
	return -1;
}

long long toBase(bool * in, int base, int n){
	long long out = 0;
	for(long long x = 0; x < n; x++){
		out += pow((long long)base, (long long)x)* (long long)in[x];
	}
	return out;
}

void genNextBin(bool * in, int k){
	bool carry = in[1];
	in[1] = !in[1];
	for(int i=2; i<k-1; i++){
		bool old = in[i];
		in[i] = carry ^ in[i];
		carry = old && carry;
	}
}