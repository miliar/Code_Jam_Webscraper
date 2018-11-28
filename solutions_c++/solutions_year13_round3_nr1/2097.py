#include <algorithm>
#include <iostream>
#include <fstream>
#include <vector>
#include <string>


using namespace std;


///////////////
// constants //
///////////////
static const bool DEBUG = false;


///////////////
// variables //
///////////////
bool IsConsonant['z'+1];
int T;
string s;
int n;


///////////////
// functions //
///////////////
inline bool is_consecutive (int i)
{
	if ((i+n) > s.length()) {
		return false;
	}

	for (int j = 0; j < n; ++j) {
		if (!IsConsonant[s[i+j]]) {
			return false;
		}
	}

	return true;
}


inline int count_front (int i)
{
	int sum = 0;
	for (int j = 1; (i-j) >= 0; ++j) {
		if (!is_consecutive (i-j)) {
			++sum;
		}
	}
	return sum;
}


inline int solve()
{
	int value = 0;
	int right = s.length() - n;
	for (int i = 0; i <= right; ++i) {
		if (is_consecutive (i)) {
			++value;
			int front = count_front (i);
			int rear = s.length() - (i+n);
			value += front * (rear + 1) + rear;
			if (DEBUG) cerr << "CONSECUTIVE: " << s.substr (i, n) << " " << front << ", " << rear << endl;
		}
	}
	return value;
}


inline int solve_brute()
{
	int value = 0;
	for (int i = 0; i <= s.length() - n; ++i) {
		for (int j = i+n; j <= s.length(); ++j) {
			for (int k = i; k + n <= j; ++k) {
				if (is_consecutive (k)) {
					if (DEBUG) cerr << "CONSECUTIVE: " << s.substr (i, (j - i)) << endl;
					++value;
					break;
				}
			}
		}
	}
	return value;
}


//////////
// main //
//////////
int main (int argc, char** argv)
{
	for (int i = 0; i <= 'z'; ++i) {
		IsConsonant[i] = true;
	}
	IsConsonant['a'] = false;
	IsConsonant['e'] = false;
	IsConsonant['i'] = false;
	IsConsonant['o'] = false;
	IsConsonant['u'] = false;

	ifstream fin;
	istream& input ((argc > 1) ? fin : cin);
	if (argc > 1) {
		fin.open (argv[1]);
	}

	input >> T;
	for (int t = 1; t <= T; ++t) {
		input >> s >> n;
		cout << "Case #" << t << ": " << solve_brute() << endl;
	}

	return 0;
}
