#include <iostream>
#include <string>
#include <vector>
#include <list>
#include <fstream>
#include <map>
#include <algorithm>


typedef unsigned __int64	u64 ;
typedef signed	 __int64	si64 ;
typedef unsigned int		u32 ;


using namespace std;
static u64 a;
static u64 b;


bool isPalindrome(u64 num) {
	if(num < 10) {return true;}

	u64 n = num;
	u64 rev = 0;
	while (num > 0){
		u64 dig = num % 10;
		rev = rev * 10 + dig;
		num = num / 10;
	}

	return (n == rev);
}

int main(int argc, char* argv[]) {
	string inTestName, outTestName;

	cout << "Enter the in test file name : " << endl;
	cin >> inTestName;
	cout << endl;

	size_t found = inTestName.find_last_of(".");
	outTestName = inTestName.substr(0, found) + ".out";

	/* Open file */
	ifstream inFile(inTestName.c_str());
	if(!inFile.is_open()) {
		cout << "Can't open input file" << endl;
		system("PAUSE");
		return 1;
	}

	ofstream outFile(outTestName.c_str());
	if(!outFile.is_open()) {
		cout << "Can't open output file" << endl;
		system("PAUSE");
		return 1;
	}

	int T; /*number of tests */
	inFile >> T;

	cout << "Start : "<< endl;
	for(int t = 0; t < T; t++) {
		//cout << "Process test " << t + 1 << " out of " << T << endl;
		inFile >> a >> b;
		//cout << "Search from " << a << " to " << b << endl;

		u64 count = 0;

		u64 min = (u64)max<double>(0, sqrt((double)a) - 1);
		u64 max = (u64)sqrt((double)b) + 1;
		//cout << endl << "Search from " << a << " to " << max << endl;
		for(u64 n = min; n < max; n++) {
			if(isPalindrome(n)) {
				//cout << n << "is a palindrome and n2 = " << n * n << endl;
				int n2 = n*n;
				if(isPalindrome(n2)) {
					//cout << "N2 is also a palindrome" << endl;
					if(n2 >= a && n2 <= b) {
						count++;
					}
				}
			}
		}
		outFile << "Case #" << t + 1 << ": " << count << endl;
	}
	outFile.close();
	inFile.close();

	cout << endl << "Stop" << endl;

	system("PAUSE");
	return 0;
}
