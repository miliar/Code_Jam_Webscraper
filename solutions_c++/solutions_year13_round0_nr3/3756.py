#include <cmath>
#include <string>
#include <iostream>

bool checkSquare(const long);
bool checkPalindrome(const long);
using namespace std;

int main(void){
	int testCase, NumCases;;
	cin >> NumCases;
	while(testCase++ < NumCases){
		long lower, upper;
		cin >> lower >> upper;
		long lTotal = 0;
		for(long i = lower; i <= upper; i++){
			if(checkSquare(i) && checkPalindrome(i) && checkPalindrome(sqrt(i))){
				lTotal++;
			}
		}
		cout << "Case #" << testCase << ": " << lTotal << endl;
	}
	return 0;
}

bool checkSquare(const long x){
	long sq = sqrt(x);
	return sq*sq == x;
}

bool checkPalindrome(const long x){
	const string s = to_string(x);
	for(int i = 0; i < s.size()/2; i++){
		if(s[i] != s[s.size() - i - 1]){
			return false;
		}
	}
	return true;
}