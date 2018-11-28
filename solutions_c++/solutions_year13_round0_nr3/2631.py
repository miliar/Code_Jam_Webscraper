#include <iostream>
#include <cmath>
#include <string>
#include <sstream>
using namespace std;

bool isPalindrome(const string& str) {
	for (int i = 0; i < str.length(); i++) {
		if (str[i] != str[str.length() - i - 1]) return false;
	}
	return true;
}

string longLongToString(long long lng) {
	string str;
	stringstream sstream;
	sstream << lng;
	sstream >> str;
	return str;
}

bool isFairAndSquare(long long x) {
	if (!isPalindrome(longLongToString(x))) {
		return false;
	}
	long long y = (long long) sqrt((double) x);
	if (x != y * y) {
		return false;
	}
	if (!isPalindrome(longLongToString(y))) {
		return false;
	}
	return true;
}

int main(void) {
	int n;
	cin >> n;
	for (int i = 1; i <= n; i++) {
		long long a, b;
		cin >> a >> b;
		long long count = 0;
		for (long long j = a; j <= b; j++) {
			if (isFairAndSquare(j)) count++;
		}
		cout << "Case #" << i << ": " << count << endl;
	}
	return 0;
}
