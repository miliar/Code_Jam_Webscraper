#include<bits/stdc++.h>
using namespace std;

typedef long long LL;
typedef unsigned long long ULL;
typedef long double LD;

double PI = acos(-1.0);
double EPS = 1e-9;
int INF = 2000000000;

#define FOR(i, a, b) for (int i = a; i < b; i++)

template <typename Type>
void print_array(Type arr, int start, int end) {
	cout << "[";
	FOR(i, start, end) {
		cout << arr[i] << ", ";
	}
	cout << "]" << endl;
}

template <typename Type>
void print_vector(vector<Type> v) {
	cout << "[";
	FOR(i, 0, v.size()) {
		cout << v[i] << ", ";
	}
	cout << "]" << endl;
}

string solve(string word, int start) {
	if (word == "") {
		return "";
	} else if (start > 9) {
		return "!";
	} else {
		string rep;
		if (start == 0) {
			rep = "ZERO";
		} else if (start == 1) {
			rep = "ONE";
		} else if (start == 2) {
			rep = "TWO";
		} else if (start == 3) {
			rep = "THREE";
		} else if (start == 4) {
			rep = "FOUR";
		} else if (start == 5) {
			rep = "FIVE";
		} else if (start == 6) {
			rep = "SIX";
		} else if (start == 7) {
			rep = "SEVEN";
		} else if (start == 8) {
			rep = "EIGHT";
		} else if (start == 9) {
			rep = "NINE";
		}

		string copy = word;
		string new_word = "";
		bool without_int = false;
		for (string::iterator it = rep.begin(); it != rep.end(); ++it) {
			bool found = false;
			for (string::iterator in = copy.begin(); in != copy.end(); ++in) {
				if (found == true || *in != *it) {
					new_word.push_back(*in);
				} else {
					found = true;
				}
			}

			if (!found) {
				without_int = true;
				break;
			} else {
				copy = new_word;
				new_word = "";
			}
		}

		if (without_int) {
			return solve(word, start + 1);
		} else {
			string with = to_string(start) + solve(copy, start);

			if (with.back() == '!') {
				return solve(word, start + 1);
			} else {
				return with;
			}
			return to_string(start) + solve(copy, start);
		}
	}
}

int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(NULL);

	// END OF HEADER

	freopen("1b-a.in", "r", stdin);
	freopen("1b-a.res", "w", stdout);

	int testcases;
	cin >> testcases;

	for (int cse = 1; cse <= testcases; cse++) {
		// END OF CODE JAM HEADER

		string word;
		cin >> word;
		string res = solve(word, 0);

		// START OF CODE JAM FOOTER
		cout << "Case #" << cse << ": " << res << endl;
	}
}
// END OF CODE JAM FOOTER
