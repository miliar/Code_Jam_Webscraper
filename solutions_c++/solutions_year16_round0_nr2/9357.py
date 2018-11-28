#include <iostream>
#include <set>
#include <algorithm> 
#include <functional> 
#include <cctype>
#include <locale>

using namespace std;

typedef struct {
	string S;
} input;

typedef struct {
	int S = 0;
} output;

auto& operator>>(istream& is, input& in) {
	is >> in.S;

	return is;
}

auto& operator<<(ostream& os, output& out) {
	os << out.S;

	return os;
}

struct Solution
{
	output solve(input in) {
		output out;

		out.S = count(trim(in.S));

		return out;
	}

	string trim(string& s) {
		if (s.size() == 0)
			return s;
		if (s.at(s.size() - 1) == '+')
			return trim(s.substr(0, s.size() - 1));
		return s;
	}

	int count(string& s, char prev = '.') {
		if (s.size() == 0)
			return 0;
		if (s.size() == 1) {
			if (s.at(0) == prev)
				return 0;
			return 1;
		}
		if (s.at(0) == prev)
			return 0 + count(s.substr(1, s.size() - 1), s.at(0));
		return 1 + count(s.substr(1, s.size() - 1), s.at(0));
	}
};

int main()
{
	int T;
	cin >> T;

	for (int t = 0; t < T; t++) {
		input in;
		cin >> in;

		Solution sol;

		output out = sol.solve(in);
		cout << "Case #" << (t + 1) << ": " << out << endl;
	}

	return 0;
}
