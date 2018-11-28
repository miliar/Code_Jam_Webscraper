//#include "stdafx.h"

#include <iostream>
#include <set>

using namespace std;

typedef struct {
	int N = 0;
} input;

typedef struct {
	int S = 0;
} output;

auto& operator>>(istream& is, input& in) {
	is >> in.N;

	return is;
}

auto& operator<<(ostream& os, output& out) {
	if (out.S <= 0)
		os << "INSOMNIA";
	else
		os << out.S;

	return os;
}

struct Solution
{
	set<int> digits;

	output solve(input in) {
		output out;

		int n = in.N;

		if (n == 0)
			return out;

		parse(n);
		while (digits.size() < 10) {
			n += in.N;
			parse(n);
		}
		out.S = n;

		return out;
	}

	void parse(int n)
	{
		while (n > 0) {
			int div = n % 10;
			digits.insert(div);
			n = n / 10;
		}
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
