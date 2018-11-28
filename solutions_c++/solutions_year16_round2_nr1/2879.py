#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <stdio.h>

using namespace std;

void subsDigits (int dig[], string str);
void passtwo (char c, string str, int arr[], vector<int>* v, int digit);

int main () {
	int T, i, j, num, flag = 0; 
	int arr[26];
	vector<int> digits;
	char c;

	cin >> T;
	c = getchar();

	for (int i=1;i<=T;i++) {

		for (j=0;j<26;j++){
			arr[j] = 0;
		}

		digits.clear();
		flag = 0;

		do {
			c = getchar();
			if (c != '\n') {
				flag = 1;
				arr[ int(c) - int('A') ]++;
				switch (c) {
					case 'Z':
						digits.push_back(0);
						subsDigits(arr, "ZERO"); 
						break;
					case 'W': 
						digits.push_back(2);
						subsDigits(arr, "TWO"); 
						break;
					case 'X': 
						digits.push_back(6);
						subsDigits(arr, "SIX"); 
						break;
					case 'U': 
						digits.push_back(4);
						subsDigits(arr, "FOUR"); 
						break;
					case 'G': 
						digits.push_back(8);
						subsDigits(arr, "EIGHT"); 
						break;
				}
			}
		} while (c != '\n' || flag == 0 );

		passtwo('O', "ONE", arr, &digits, 1);
		passtwo('T', "THREE", arr, &digits, 3);
		passtwo('F', "FIVE", arr, &digits, 5);
		passtwo('S', "SEVEN", arr, &digits, 7);

		num = arr[int('I') - int('A')];
		for (j=0;j<num;j++) {
			digits.push_back(9);
		}

		sort(digits.begin(), digits.end());
		num = digits.size();
		cout << "Case #" << i << ": ";
		for (j=0;j<num;j++) {
			cout << digits[j];
		}
		cout << endl;
	}

	return 0;
}

void passtwo (char c, string str, int arr[], vector<int>* v, int digit) {
	int j,times;
	times = arr[int(c) - int('A')];
	for (j=0;j<times;j++) {
		(*v).push_back(digit);
		subsDigits(arr, str); 
	}
}

void subsDigits (int dig[], string str) {
	int i, size;
	size = str.size();
	for (i=0;i<size;i++) {
		dig[ int(str[i]) - int('A')]--;
	}
}