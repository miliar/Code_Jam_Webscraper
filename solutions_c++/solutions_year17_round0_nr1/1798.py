#include <iostream>
#include <string>
#include <sstream>

using namespace std;

struct Problem
{
	string S;
	int K;
	string result;

	void solve()
	{
		string s(S.size(), '+');
		int moves = 0;

		for (int i = 0; (i <= s.size() - K) && (s != S); ++i)
		{
			if (s[i] != S[i])
			{
				for (int j = 0; j < K; ++j)
					s[i + j] = (s[i + j] == '+') ? '-' : '+';

				++moves;
			}
		}

		if (s == S)
		{
			stringstream ss;
			ss << moves;
			result = ss.str();
		}
		else
			result = "IMPOSSIBLE";
	}
};

istream &operator >>(istream &in, Problem &p)
{
	in >> p.S >> p.K;
	return in;
}

ostream &operator <<(ostream &out, Problem &p)
{
	out << p.result;
	return out;
}

void test()
{
	int T = 0;
	cin >> T;

	for (int i = 0; i < T; ++i)
	{
		Problem p;
		cin >> p;
		p.solve();
		cout << "Case #" << i + 1 << ": " << p << endl;
	}
}

int main()
{
	test();
	return 0;
}
