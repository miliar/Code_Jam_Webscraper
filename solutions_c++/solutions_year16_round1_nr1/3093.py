#include <fstream>
#include <iostream>
#include <string>
using namespace std;

string lastWord(string S) {
	int i, n = S.length();
	string result;
	result = S[0];
	for (i = 1; i < n; i++) {
		if (result[0] > S[i]) {
			result += S[i];
		}
		else {
			result = S[i] + result;
		}
	}
	return result;
}

int main() {
	ifstream in("input.in");
	ofstream out("output.out");
	int T, i;
	in >> T;
	string S;
	for (i = 0; i < T; i ++) {
		in >> S;
		out << "Case #" << i + 1 << ": " << lastWord(S) << endl;
	}
	return 0;
}