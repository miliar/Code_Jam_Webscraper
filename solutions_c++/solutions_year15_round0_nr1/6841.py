#include <iostream>

using namespace std;

int T;
int S;
string input;
int inputs[1000];

int solve(int size) {
	int needed = 0;
	int friends = inputs[0];
	for ( int i = 1 ; i < size ; i++) {
		//cout << "i: " << i << " friends: " << friends << " needed: " << needed << endl; 
		int new_needed = 0;
		if ((friends < i) && (inputs[i])) {
			new_needed = i - friends;
		}
		needed += new_needed;
		friends += inputs[i] + new_needed;
		//cout << "i: " << i << " friends: " << friends << " needed: " << needed << endl; 
	}
//	cout << friends << ">=" << size-1 << endl;
	return needed;
}

int main() {
	cin >> T;
	for ( int i = 0 ; i < T ; ++i) {
		cin >> S;
		cin >> input;
		for (int j = 0 ; j < input.length() ; ++j) {
			inputs[j] = input[j] - '0';
		}
		int answer = solve(input.length());
		cout << "Case #" << i+1 << ": " << answer << endl;
	}
	return 0;
}
