//============================================================================
// Name        : FairAndSquare.cpp
// Author      : Jeongseok Son
// Version     :
// Copyright   : GNU LGPL
// Description : Google Code Jam Problem C. Fair and Square
//============================================================================

#include <iostream>
#include <cmath>
using namespace std;

bool isPalindrome(unsigned long long n) {
	unsigned long long temp = n;
	unsigned long long div = 1;
	unsigned long long mod = 1;

	while(temp) {
		temp /= 10;
		div *= 10;
	}

	while(div > mod * 10) {
		div /= 10;
		mod *= 10;
		if(n % mod != n / div) {
			return false;
		}
	}

	return true;
}

int main() {
	int cases;
	cin >> cases;
	for(int c = 1; c <= cases; c++) {
		unsigned long long a, b;
		unsigned long long l, h;
		int ans = 0;
		cin >> a >> b;
		l = ceil(sqrt(a));
		h = floor(sqrt(b));
		for(unsigned long long i = l; i <= h; i++) {
			if(isPalindrome(i) && isPalindrome(i * i)) {
				ans++;
			}
		}
		cout << "Case #" << c << ": " << ans << endl;
	}

	return 0;
}
