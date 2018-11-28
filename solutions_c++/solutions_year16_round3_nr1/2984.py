//#include "stdafx.h"

#include <iostream>
#include <vector>
#include <set>
#include <string>
#include <sstream>

using namespace std;

typedef struct {
	int N = 0;
	vector<int> P;
} input;

typedef struct {
	vector<string> S;
} output;

auto& operator>>(istream& is, input& in) {
	is >> in.N;
	in.P = vector<int>(in.N);
	for (int i = 0; i < in.N; ++i) {
		int p;
		is >> p;
		in.P[i] = p;
	}

	return is;
}

auto& operator<<(ostream& os, output& out) {
	for (unsigned int i = 0; i < out.S.size(); ++i) {
		if (i > 0)
			os << " ";
		os << out.S[i];
	}

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

		while (hasLeft(in)) {
			step(in, out);
		}

		return out;
	}

	void step(input& in, output& out) {
		for (int i = 0; i < in.N; i++) {
			for (int j = 0; j < in.N; j++) {
				if (in.P[i] == 0)
					continue;
				if (in.P[j] == 0)
					continue;

				input in1 = in;
				in1.P[i]--;
				in1.P[j]--;

				if (isValid(in1)) {
					in = in1;
					ostringstream oss;
					oss << char('A' + i) << char('A' + j);
					out.S.push_back(oss.str());
					return;
				}
			}
		}
		for (int i = 0; i < in.N; i++) {
			if (in.P[i] == 0)
				continue;

			input in1 = in;
			in1.P[i]--;

			if (isValid(in1)) {
				in = in1;
				ostringstream oss;
				oss << char('A' + i);
				out.S.push_back(oss.str());
				return;
			}
		}
	}

	bool hasLeft(const input& in) {
		for (int i = 0; i < in.N; ++i) {
			if (in.P[i] > 0)
				return true;
		}

		return false;
	}

	bool isValid(const input& in) {
		int total = 0;
		for (int i = 0; i < in.N; ++i)
			total += in.P[i];

		for (int i = 0; i < in.N; ++i) {
			if (in.P[i] > total / 2.0)
				return false;
		}

		return true;
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
