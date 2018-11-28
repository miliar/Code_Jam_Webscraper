#include <fstream>
#include <string>

#define SIZE 200

using namespace std;

int greedy(string &s)
{
	int ret = 0;
	int len = s.length();
	for (int i = len - 1; i >= 0; --i)
		if (s[i] == '-')
		{
			// one more step
			if (s[0] == '+')
			{
				int j = 0;
				++ret;
				while (s[j] == '+')
				{
					s[j] = '-';
					++j;
				}
			}
			for (int j = 0; j <= i; ++j)
				s[j] = (s[j] == '+')? '-':'+';
			for (int j = 0; j <= i/2; ++j)
			{
				char tmp = s[j];
				s[j] = s[i - j];
				s[i - j] = tmp;
			}
			++ret;
		}
	return ret;
}

int main()
{
	ifstream infile("B-large.in");
	ofstream outfile("B-output");

	int t;
	infile >> t;
	infile.get();
	for (int ca = 1; ca <= t; ++ca)
	{
		string s;
		getline(infile, s);
		outfile << "Case #" << ca << ": " << greedy(s) << endl;
	}
	return 0;
}