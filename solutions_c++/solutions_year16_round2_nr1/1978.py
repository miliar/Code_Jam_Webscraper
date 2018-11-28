#include <iostream>
#include <vector>
#include <map>

using namespace std;

string solve(const string &inputS) {
	// ZERO -> Z
	// TWO -> W
	// EIGHT -> G
	// SIX -> X
	// SEVEN -> S
	// FIVE -> V
	// FOUR -> F
	// ONE -> O
	// THREE -> R
	// NINE ->

	string result = "";
	string s = string(inputS);
	std::size_t found = s.find("Z");
	while (found != string::npos) {
		s.erase(s.begin() + found);
		s.erase(s.begin() + s.find("E"));
		s.erase(s.begin() + s.find("R"));
		s.erase(s.begin() + s.find("O"));
		result += "0";
		found = s.find("Z");
	}

	found = s.find("W");
	while (found != string::npos) {
		s.erase(s.begin() + found);
		s.erase(s.begin() + s.find("T"));
		s.erase(s.begin() + s.find("O"));
		result += "2";
		found = s.find("W");
	}

	// EIGHT -> G
	found = s.find("G");
	while (found != string::npos) {
		s.erase(s.begin() + found);
		s.erase(s.begin() + s.find("E"));
		s.erase(s.begin() + s.find("I"));
		s.erase(s.begin() + s.find("H"));
		s.erase(s.begin() + s.find("T"));
		result += "8";
		found = s.find("G");
	}

	// SIX -> X
	found = s.find("X");
	while (found != string::npos) {
		s.erase(s.begin() + found);
		s.erase(s.begin() + s.find("S"));
		s.erase(s.begin() + s.find("I"));
		result += "6";
		found = s.find("X");
	}

	// SEVEN -> S
	found = s.find("S");
	while (found != string::npos) {
		s.erase(s.begin() + found);
		s.erase(s.begin() + s.find("E"));
		s.erase(s.begin() + s.find("V"));
		s.erase(s.begin() + s.find("E"));
		s.erase(s.begin() + s.find("N"));
		result += "7";
		found = s.find("S");
	}

	// FIVE -> V
	found = s.find("V");
	while (found != string::npos) {
		s.erase(s.begin() + found);
		s.erase(s.begin() + s.find("F"));
		s.erase(s.begin() + s.find("I"));
		s.erase(s.begin() + s.find("E"));
		result += "5";
		found = s.find("V");
	}

	// FOUR -> F
	found = s.find("F");
	while (found != string::npos) {
		s.erase(s.begin() + found);
		s.erase(s.begin() + s.find("O"));
		s.erase(s.begin() + s.find("U"));
		s.erase(s.begin() + s.find("R"));
		result += "4";
		found = s.find("F");
	}

	// ONE -> O
	found = s.find("O");
	while (found != string::npos) {
		s.erase(s.begin() + found);
		s.erase(s.begin() + s.find("N"));
		s.erase(s.begin() + s.find("E"));
		result += "1";
		found = s.find("O");
	}

	// THREE -> R
	found = s.find("R");
	while (found != string::npos) {
		s.erase(s.begin() + found);
		s.erase(s.begin() + s.find("T"));
		s.erase(s.begin() + s.find("H"));
		s.erase(s.begin() + s.find("E"));
		s.erase(s.begin() + s.find("E"));
		result += "3";
		found = s.find("R");
	}

	// NINE ->
	found = s.find("N");
	while (found != string::npos) {
		s.erase(s.begin() + found);
		s.erase(s.begin() + s.find("I"));
		s.erase(s.begin() + s.find("N"));
		s.erase(s.begin() + s.find("E"));
		result += "9";
		found = s.find("N");
	}

	std::sort(result.begin(), result.end());
	return result;
}

int main() {


	int testCaseCount = 0;
	cin >> testCaseCount;
	for (int i = 1; i <= testCaseCount; ++i) {
		string S;
		cin >> S;
		cout << "Case #" << i << ": " << solve(S) << endl;
	}
	return 0;
}
