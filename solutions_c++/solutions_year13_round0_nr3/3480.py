#include <iostream>
#include <math.h>
#include <stdio.h>
#include <vector>
#include <string>
#include <iterator>
#include <sstream>

using namespace std;
int checkPalindrome(int);

int main() {
	int number = 0;
	
	string str = "";
	while (true) {
		getline(cin, str);

		stringstream stream(str);
		if (stream >> number)
			break;
	}

	for(int i = 0; i < number; i++) {
		if(i != 0)
			cout << endl;
		getline(cin, str);
		string buf;

		istringstream ss(str);
		vector<int> tokens;	
		copy(istream_iterator<int>(ss), istream_iterator<int>(), back_inserter<vector<int>>(tokens));
		int min = tokens[0];
		int max = tokens[1];

		int minSqrt = ceil(sqrt(double(min)));
		int maxSqrt = floor(sqrt(double(max)));
		int total = 0;

		for(int j = minSqrt; j <= maxSqrt; j++) {
			if(checkPalindrome(j) == 1)
				total += checkPalindrome(j * j);
		}
		cout << "Case #" << i + 1 << ": " << total;
	}
	return 0;
}

int checkPalindrome(int number) {
	int n1, rev = 0, rem;
	n1 = number;
	while (n1 > 0){
		rem = n1 % 10;
		rev = rev * 10 + rem;
		n1 = n1 / 10;
	}
	if (number == rev){
		return 1;
	}
	return 0;
}