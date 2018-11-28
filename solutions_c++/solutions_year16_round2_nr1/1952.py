
#include "stdafx.h"
#include "stdafx.h"
#include <iostream>
#include <string>
#include <bitset>
#include <vector>
#include <array>

using namespace std;


int countChars(char oneChar, string someString){
	int count = 0;

	for (int i = 0; i < someString.size(); i++)
		if (someString[i] == oneChar) count++;

	return count;
}



using namespace std;
int main() {
	int T;
	cin >> T;
	for (int i = 1; i <= T; i++){
		string s;
		cin >> s;
		int arr[10] = { 0 };
		arr[0] = countChars('Z', s); //
		arr[2] = countChars('W', s); //
		arr[4] = countChars('U', s); //
		arr[3] = countChars('R', s) - arr[0] - arr[4]; //
		arr[5] = countChars('F', s) - arr[4]; //
		arr[6] = countChars('X', s); //
		arr[7] = countChars('S', s) - arr[6]; //
		arr[8] = countChars('G', s);
		arr[9] = countChars('I', s) - arr[5] - arr[6] - arr[8];
		arr[1] = countChars('N', s) - arr[7] - arr[9]*2;

		cout << "Case #" << i << ": " ;

		for (int j = 0; j < 10; j++){
			for (; arr[j] != 0; arr[j]--){
				cout << j;
			}
		}
		cout << endl;
	}



	cin >> T;
	return 0;
}
