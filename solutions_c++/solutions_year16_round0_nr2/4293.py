#include <iostream>
#include <string>
using namespace std;

int numOfManeuvers(string &);

int main() {
	int T;
	cin >> T;
	string S;
	for(int count = 1; count <= T; ++count) {
		cin >> S;
		cout << "Case #" << count << ": " << numOfManeuvers(S) << endl;
	}

	return 0;
}

int numOfManeuvers(string & s) {
	char to = '+';
	int result = 0;
	for(int i = s.length() - 1; i >= 0; --i) {
		if(s[i] != to) {
			result = result + 1;
			to = s[i];
		}
	}

	return result;
}