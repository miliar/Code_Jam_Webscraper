#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <string>
#include <queue>
#include <stack>
#include <bitset>
#include <cmath>
#include <sstream>
#include <map>


using namespace std;

string const ZERO = "ZERO";
string const ONE = "ONE";
string const TWO = "TWO";
string const THREE = "THREE";
string const FOUR = "FOUR";
string const FIVE = "FIVE";
string const SIX = "SIX";
string const SEVEN = "SEVEN";
string const EIGHT = "EIGHT";
string const NINE = "NINE";

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> ii;
typedef vector<ii> vii;
typedef long long ll;

map<char,int> letters;

vi digits;

void collect_letters(string S) {
	for (char c = 'A'; c <= 'Z'; c++) {
		letters[c] = 0;
	}

	int L = (int) S.size();
	for (int i = 0; i < L; i++) {
		char c = S[i];
		letters[c]++;
	}

}

void collect_sure() {
	// collect zeros
	if (letters['Z'] > 0) {
		int k = letters['Z'];
		for (char c : ZERO) {
			letters[c] -= k;
		}
		digits[0] += k;
	}

	// collect twos
	if (letters['W'] > 0) {
		int k = letters['W'];
		for (char c : TWO) {
			letters[c] -= k;
		}
		digits[2] += k;
	}

	// collect fourss
	if (letters['U'] > 0) {
		int k = letters['U'];
		for (char c : FOUR) {
			letters[c] -= k;
		}
		digits[4] += k;
	}

	// collect sixes
	if (letters['X'] > 0) {
		int k = letters['X'];
		for (char c : SIX) {
			letters[c] -= k;
		}
		digits[6] += k;
	}

}

void count_number(string cur) {
	if (cur == ONE) {
		digits[1]++;
	} 
	else if (cur == THREE) {
		digits[3]++;
	}
	else if (cur == FIVE) {
		digits[5]++;
	}
	else if (cur == SEVEN) {
		digits[7]++;
	}
	else if (cur == EIGHT) {
		digits[8]++;
	}
	else if (cur == NINE) {
		digits[9]++;
	}
}

void remove_number(string cur) {
	if (cur == ONE) {
		digits[1]--;
	} 
	else if (cur == THREE) {
		digits[3]--;
	}
	else if (cur == FIVE) {
		digits[5]--;
	}
	else if (cur == SEVEN) {
		digits[7]--;
	}
	else if (cur == EIGHT) {
		digits[8]--;
	}
	else if (cur == NINE) {
		digits[9]--;
	}
}

void take(string number) {
	for (char c : number) {
		letters[c]--;
	}
}

void add(string number) {
	for (char c : number) {
		letters[c]++;
	}
}

bool possible(string number) {
	take(number);
	for (char c : number) {
		if (letters[c] < 0) {
			add(number);
			return false;
		}
	}

	add(number);
	return true;
}

string next(string cur) {
	if (cur == ONE) {
		return THREE;
	} 
	else if (cur == THREE) {
		return FIVE;
	}
	else if (cur == FIVE) {
		return SEVEN;
	}
	else if (cur == SEVEN) {
		return EIGHT;
	}
	else if (cur == EIGHT) {
		return NINE;
	}

	return "";
}

bool rec(string S, string cur) {

	if (cur == "") {
		for (char c = 'A'; c <= 'Z'; c++) {
			if (letters[c] != 0) return false;
		}
		//cout << letters['V'] << endl;
		return true;
	}

	//cout << "without " << cur << endl;
	//rec(S, next(cur));
	bool done = false;

	for (int i = 0; i < 1000 && !done; i++) {
		string make = "";
		for (int j = 0; j < i; j++) {
			make += cur;
		}

		if (possible(make)) {
			take(make);
			for (int j = 0; j < i; j++) count_number(cur);
			done |= rec(S, next(cur));
			if (!done) for (int j = 0; j < i; j++) remove_number(cur);
			add(make);
		} else {
			break;
		}
	}

	return done;

}

void solve(string S) {
	collect_letters(S);
	collect_sure();

	rec(S, ONE);

}


int main() {
	ifstream in ("in.txt");
	ofstream out ("out.txt");

	int T; in >> T;
	string line;
	getline(in, line);

	for (int i = 1; i <= T; i++) {
		getline(in, line);
		digits.assign(10,0);

		solve(line);

		out << "Case #" << i << ": ";
		for (int j = 0; j <= 9; j++) {
			for (int k = 0; k < digits[j]; k++) {
				out << j;
			}
		}

		out << endl;
	}

	return 0;
} 