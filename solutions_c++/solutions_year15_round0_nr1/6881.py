#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <sstream>

using namespace std;

unsigned load(vector<unsigned> &SMax, vector<string> &digits);
void save(unsigned n, const vector<unsigned> &res);
unsigned ctou(const char c);

int main()
{
	vector<unsigned> SMax;
	vector<string> digits;
	vector<unsigned> res;
	unsigned n = load(SMax, digits);

	for (size_t i = 0; i < n; ++i)
	{
		unsigned S = 0;
		unsigned toInvite = 0;
		for (size_t k = 0; k <= SMax[i]; ++k)
		{
			if (ctou(digits[i][k]) == 0)
				continue;
			if (k > S)
			{
				toInvite += k - S;
				S += k - S;
			}
			S += ctou(digits[i][k]);
		}
		res.push_back(toInvite);
	}

	save(n, res);

	return 0;
}

unsigned load(vector<unsigned> &SMax, vector<string> &digits)
{
	ifstream infile("input.txt");

	string s;
	getline(infile, s);

	stringstream ss;
	ss << s;
	unsigned n;
	ss >> n;

	for (size_t i = 0; i < n; ++i)
	{
		getline(infile, s);
		ss.clear();
		ss << s;
		unsigned max;
		ss >> max;
		SMax.push_back(max);
		ss >> s;
		digits.push_back(s);
	}

	infile.close();
	return n;
}

unsigned ctou(const char c)
{
	return c - '0';
}

void save(unsigned n, const vector<unsigned> &res)
{
	ofstream outfile("output.txt");
	for (size_t i = 1; i < n; ++i)
	{
		outfile << "Case #" << i << ": " << res[i - 1] << endl;
	}
	outfile << "Case #" << n << ": " << res[n - 1];
	outfile.close();
}
