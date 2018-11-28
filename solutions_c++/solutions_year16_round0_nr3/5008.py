#include <iostream>
#include <cstdio>
#include <string>
#include <cmath>
#include <cstdlib>
using namespace std;

typedef struct {
	bool notPrime;
	unsigned long long firstDivisor;
} NP;

typedef struct {
	bool allNotPrime;
	unsigned long long divisors[9];
} Answer;

NP notPrime(unsigned long long number) {
	NP temp;
	if (number%2==0) {
		temp.notPrime = true;
		temp.firstDivisor = 2;
	}
	else if (number%3==0) {
		temp.notPrime = true;
		temp.firstDivisor = 3;
	}
	else if (number%5==0) {
		temp.notPrime = true;
		temp.firstDivisor = 5;
	}
	else {
		unsigned long long divisor = 7;
		unsigned long long upLimit = (unsigned long long) sqrt( (double) number) + 1;
		bool notPrime = false;
		temp.notPrime = false;
		temp.firstDivisor = 0;

		while (divisor <= upLimit && !notPrime) {
			if (number%divisor==0) {
				temp.notPrime = true;
				temp.firstDivisor = divisor;
				notPrime = true;
			}
			divisor += 2;
		}
		return temp;
	}
}

unsigned long long decimalToBinary(unsigned long long number, unsigned long long base) {
	string result = "";
	while (number>0) {
		if (number%base==0) {
			result = '0' + result;
		}
		else result = '1' + result;
		number /= base;
	}
	return atoll(result.c_str());
}

unsigned long long binaryToDecimal(unsigned long long binary, unsigned long long base) {
	unsigned long long result = 0;
	unsigned long long perpangkatan = 1;

	while (binary>0) {
		unsigned long long currDigit = binary%10;
		result += (currDigit * perpangkatan);
		perpangkatan *= base;
		binary /= 10;
	}

	return result;
}

Answer allNotPrime(unsigned long long interpret[9]) {
	Answer ans;
	ans.allNotPrime = true;	

	for (int i=0; i<9 && ans.allNotPrime; i++) {
		NP retVal = notPrime(interpret[i]);
		if (retVal.notPrime==false) {
			ans.allNotPrime = false;
		}
		else { //notPrime
			ans.divisors[i] = retVal.firstDivisor;
		}
	}
	//cout << endl;
	return ans;
}

int main() {
	int T;
	scanf("%d",&T);
	for (int z=1; z<=T; z++) {
		int N, J;
		scanf("%d %d",&N,&J);

		unsigned long long interpret[9]; //yang kesembilan pake conversion aja
		unsigned long long base = 1;
		for (int j=1; j<=15; j++) {
			base *= 2;
		}
		interpret[0] = base + 1;

		unsigned long long binary = decimalToBinary(interpret[0], 2);
		for (int i=3; i<=10; i++) {
			interpret[i-2] = binaryToDecimal(binary, i);
		}

		printf("Case #%d:\n",z);
		int got = 0;
		while (got<J) {
			Answer ans = allNotPrime(interpret);
			if (ans.allNotPrime) {
				cout << interpret[8] << " "; 
				//cout<<endl;
				
				for (int i=0; i<9; i++) {
					cout << ans.divisors[i];
					if (i<8) cout << " ";
				}

				/*unsigned long long base10[8];
				for (int i=0; i<8; i++) {
					base10[i] = decimalToBinary(interpret[i], i+2);
					cout << base10[i] << endl;
				}
				cout << endl;*/

				cout << endl;
				got++;
			}

			//next
			interpret[0] += 2;
			unsigned long long binary = decimalToBinary(interpret[0], 2);
			for (int i=3; i<=10; i++) {
				interpret[i-2] = binaryToDecimal(binary, i);
			}
		}
	}
	return 0;
}