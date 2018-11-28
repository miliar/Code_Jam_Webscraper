#include <iostream>
#include <cmath>
#include <sstream>
#include <string>

using namespace std;

bool is_palindrome(int value){
	stringstream ss;
	ss << value;
	string s = ss.str();
	for(int i=0; i<s.size()/2; ++i){
		if(s[i] != s[s.size()-i-1]) return false;
	}
	return true;
}

int main(int argc, char** argv){

	int T;
	cin >> T;

	for(int t=1; t<=T; ++t){
		cout << "Case #" << t << ": ";

		int A,B;
		cin >> A >> B;

		int sqrt_A = (int) ceil(sqrt(A));
		int sqrt_B = (int) sqrt(B);

		int count = 0;

		for(int value=sqrt_A; value<=sqrt_B; value++){
			if(is_palindrome(value) && is_palindrome(value*value)) count++;
		}

		cout << count << endl;
	}

	return 0;
}
