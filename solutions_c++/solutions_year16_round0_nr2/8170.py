#include <iostream>
#include <string>
#include <map>

using namespace std;

string flip(string S, int n) {
	string flipped = S;
	for (int i = 0; i < n; i++)
		flipped[i] = S[n - i - 1] == '+' ? '-' : '+';
	return flipped;
}

int solve(string S) {
	if (S.find('-') == string::npos)
		return 0;

	int i;
	for(i = 1; i < S.length() && S[i] == S[0]; i++);
	return 1 + solve(flip(S, i));
}

int main() {
	int T;
	cin >> T;

	for (int t = 0; t < T; t++) {
		string S;
		cin >> S;
		cout << "Case #" << t+1 << ": " << solve(S) << endl;
	}

	return 1;
}
