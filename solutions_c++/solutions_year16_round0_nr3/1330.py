#include <iostream>
#include <fstream>
#include <string>
#include <math.h>
#include <iomanip>
#include <vector>
#include <algorithm>
using namespace std;

long long isPrime(long long n) {
	for (long long i = 2; i < sqrt(n); i++) {
		if (n%i == 0)
			return i;
	}
	return n;
}

bool elevenDivides(string a) {
	int sum = 0;
	for (int i = 0; i < a.size(); i++) {
		sum += (a[i] - '0') * ((i % 2) * 2 - 1);
	}
	return (sum % 11 == 0);
}

long long convertFromBase(string num, int base) {
	long long sum = 0;
	for (int i = 0; i < num.length(); i++) {
		sum += pow(base, num.length() - i - 1)*(num[i] - '0');
	}
	return sum;
}
string convertBaseB(long long num, int base) {
	string k = "";
	while (num > 0) {
		k = to_string(num%base) + k;
		num /= base;
	}
	return k;
}
int main() {
	int t;
	fstream input, output;
	input.open("input.txt", ios::in);
	output.open("output.txt", ios::out);
	int numPrinted = 0; 
	/*cout << elevenDivides("1111");
	cout << elevenDivides("1100");
	cout << elevenDivides("1101");
	cout << elevenDivides("1001");*/
	output << "Case #1:" << endl;
	for (long long k = pow(2,31)+1; k < pow(2,32); k += 2) {
		if (elevenDivides(convertBaseB(k, 2))) {
			output << convertBaseB(k, 2);
			for (int i = 3; i < 12; i++) {
				output << " " << i;
			}
			if (numPrinted != 499)
				output << endl;
			numPrinted++;
			if (numPrinted == 500)
				break;
		}
			
	}
}

