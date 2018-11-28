#include <iostream>
#include <fstream>
#include <string>
#include <cstdio>
#include <cmath>
#include <sstream>

using namespace std;

bool isPerfect(long long n) {
	long long q = sqrt(n);
	return q * q == n;
}

bool isPalindrome(long long n) {
	ostringstream convert;
	convert << n;
	string s = convert.str();
	bool res = true;
	int len = s.size();
	for (int i = 0; i < len/2; i++)
		if (s[i] != s[len - 1 - i])
			res = false;
	return res;
}

int main() {


	int t;
	long long a, b;
	cin >> t;
	int c = 1;
	while (t--) {
		cin >> a >> b;
		long long result = 0;
		for (long long i = a; i <= b; i++) {

			if (isPerfect(i) && isPalindrome(i) && isPalindrome(sqrt(i)))
				result++;
		}
	//cout << isPalindrome(1) << endl;
	cout << "Case #" << c << ": " << result << endl;
	c++; 
	}
}