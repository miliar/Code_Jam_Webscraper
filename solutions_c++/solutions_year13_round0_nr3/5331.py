#include <iostream>
#include <fstream>
#include <string>
#include <time.h>
#include <math.h>

using namespace std;

int isPalindrome(int n) {
	int rev,num;
	
	num = n;
	rev = 0;
	while(num > 0) {
		rev = rev*10 + num%10;
		num /= 10;
	}
	
	if(rev == n)
		return 1;
	
	return 0;
}

int isPerfectSquare(int n)
{
	int h = n & 0xF;
	if (h > 9)
		return 0;

	if ( h != 2 && h != 3 && h != 5 && h != 6 && h != 7 && h != 8 ) {
		int t = (int) floor( sqrt((double) n) + 0.5 );
		return t*t == n;
	}
	return 0;
}

int isFairAndSquare(int n) {
	
	if(isPalindrome(n) && isPerfectSquare(n)) {
		return isPalindrome((int)sqrt(n));
	}
	
	return 0;
}

int main() {
	clock_t one, two;
	one = clock();
	
	int numOfCases, ctr, leftLimit, rightLimit, i, j;
	string line;
	
	ifstream inFile ("C-small-attempt0.in");
	ofstream outFile ("outputC.txt");

	if (inFile.is_open() && outFile.is_open()) {
		getline(inFile,line);
		numOfCases = atoi(line.c_str());
		for(i = 1; i <= numOfCases; ++i) {
			ctr = 0;
			inFile >> leftLimit >> rightLimit;
			for(j = leftLimit; j <= rightLimit; ++j) {
				ctr += isFairAndSquare(j);
			}
			outFile << "Case #" << i << ": " << ctr << endl;
		}
		inFile.close();
		outFile.close();
	}

	two = clock();
	cout << "Time taken in sec: " << (((double) (two - one)) / CLOCKS_PER_SEC) << endl;
	return 0;
}