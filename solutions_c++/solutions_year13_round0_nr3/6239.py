#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <cmath>

using namespace std;

int getPalindromes(unsigned long long a, unsigned long long b);
bool isPalindrome(unsigned long long n);
bool isPerfectSquare(unsigned long long n);

int main(int argc, const char ** argv) {

	// Read the inputs

	ifstream inputFile;
	inputFile.open(argv[1]);

	int testCases;
	inputFile >> testCases;

	for (int i = 0; i < testCases && inputFile.good(); i++) {
		unsigned long long a, b;
		inputFile >> a >> b;

		int output = getPalindromes(a, b);
	
		cout << "Case #" << (i+1) << ": " << output << endl;
	}

	return 0;
}

int getPalindromes(unsigned long long a, unsigned long long b) {
	unsigned long long count = 0;
	
	for (unsigned long long i = a; i <= b; i++) {
		if (isPerfectSquare(i) && isPalindrome(i) && isPalindrome(sqrt(i))) {
			count++;
		}
	}

	return count;
}

bool isPalindrome(unsigned long long n) {
	stringstream stream;
	stream << n;
	string original = stream.str();
	string reverse = string(original.rbegin(), original.rend());

	return (original == reverse);
}

bool isPerfectSquare(unsigned long long n) {
    if (n < 0) return false;
    unsigned long long root = round(sqrt(n));
    return n == root * root;
}