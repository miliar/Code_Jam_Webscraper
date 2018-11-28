#include <iostream>
#include <algorithm>
#include <cstdio>

using namespace std;

int main (void)
{
	int t;

	cin >> t;

	int c = 1;

	while (t--)
	{
		string s;
		cin >> s;

		int contFlip = 0;	

		while (s.find('-') != s.npos)
		{
			size_t f;
			if (s[0] == '+')
			{
				f = s.find("-");
				s.replace(s.begin(), s.begin() + f, "-");
				contFlip ++;
			}
			else
			{
				f = s.find("+");
				s.replace(s.begin(), s.begin() + f, "+");
				contFlip ++;
			}
		}

		cout << "Case #" << c ++ << ": " << contFlip << '\n';
	}
	return 0;
}