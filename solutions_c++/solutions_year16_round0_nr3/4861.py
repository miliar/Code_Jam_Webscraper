#include <iostream>
#include <fstream>
#include <sstream>
#include <cmath>
using namespace std;

int notList[40000] = {0};
int notPrimeNum = 0;
long long checkPrime(long long n) {
	for (long long i = 2; i <= sqrt(n); i++) {
		if (n % i == 0) {
			return i;
		}
	}
	return 0;
}

int main(int argc, char* argv[]) {
	int t;
	cin >> t;
	cout << "Case #1:" << endl;
	int n, j;
	cin >> n >> j;
	// 32769 -> 65535
	// 2147483649 -> 
	int divisor2[40000] = {0};
	int ansNum = 0;
	for (long long k = 32769; k <= 65535; ++k) {
		long long divisor[11] = {0};
		long long t = checkPrime(k);
		if (k % 2 == 0) {
			continue;
		}
		if (t) {
			divisor[2] = t;
		} else {
			continue;
		}
		// cerr << "checked base 2: " << k << endl;
		bool fail = false;
		for (int b = 3; b <= 10; ++b) {
			long long tk = k;
			long long sum = 0;
			for(int j = 0; j < 16; ++j) {
				sum += (tk % 2) * pow(b, j);
				tk /= 2;
			}
			long long r = checkPrime(sum);
			if(r) {
				divisor[b] = r;
				continue;
			} else {
				fail = true;
				break;
			}
		}
		for (int b = 2; b <= 10; ++b) {
			if (divisor[b] <= 0) {
				fail = true;
				break;
			}
		}
		if (fail) {
			continue;
		} else {
			ansNum++;
		}
		int ansK[16];
		long long tpk = k;
		for(int h = 15; h >= 0; --h) {
			ansK[h] = (tpk % 2);
			tpk /= 2;
		}
		for(int h = 0; h < 16; ++h) {
			cout << ansK[h] ;
		}
		cout <<" " ;
		for (int b = 2; b <= 10; ++b) {
			cout << divisor[b] << " " ;
		}
		cout << endl;
		if (ansNum >= j) {
			break;
		}
	}
	/*
	for (int k = 0; k < notPrimeNum; ++k) {
		cerr << "Num is " << notList[k] << " " << divisor2[k] <<endl;
	}
	*/
	cerr << ansNum << endl;
}