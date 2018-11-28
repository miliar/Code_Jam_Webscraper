#include <sstream>
//#include <cstring>
//#include <string>
#include <iostream>
#include <cmath>
#include <cstdlib>
using namespace std;

void readInput();
void solveCase(int min, int max);
bool isSquare(int num);
bool isPalindrome(int num);

int main() {
	readInput();
	return 0;
}

void readInput() {
	int numCases, min, max;
	cin >> numCases;
	for (int i = 0; i < numCases; i++) {
		cout << "Case #" << i + 1 << ": ";
		cin >> min >> max;
		solveCase(min, max);
	}
}

void solveCase(int min, int max) {
	int count = 0;
	for (int i = min; i <= max; i++) {
		if (isSquare(i) && isPalindrome(i) && isPalindrome(int(sqrt(i)))) {
			count++;
		}
	}
	cout << count << endl;
}

bool isSquare(int num) {
	double root = sqrt(num);
	int intRoot = int(sqrt(num));
	return root == intRoot;
}

bool isPalindrome(int num) {
	stringstream stream;
	stream << num;
	string intStr = stream.str();
	int length = intStr.length();
//	cout << intStr << endl;
	for (int i = 0; i < length / 2; i++) {
//		cerr << intStr[i] << " " << intStr[length - i - 1] << endl;
		if (intStr[i] != intStr[length - i - 1]) {
			return false;
		}
	}
	return true;
}
