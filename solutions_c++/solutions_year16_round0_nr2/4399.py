#include <iostream>
#include <fstream>
#include <stdio.h>
#include <vector>
#include <math.h>
#include <string>

using namespace std;

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int S;
	cin >> S;
	for (int i = 0; i < S; ++i)
	{
		string s;
		cin >> s;
		vector <bool> source;
		int count_blanks = 0;
		int is_first_balnk = 0;
		if (s[0] == '-')
		{
			is_first_balnk = 1;
		}
		bool inside_blanks = false;
		for (int j = 0; j < s.size(); ++j)
		{
			if (s[j] == '-')
			{
				inside_blanks = true;
			}
			else if (inside_blanks)
			{
				++count_blanks;
				inside_blanks = false;
			}
			else
			{
				inside_blanks = false;
			}
		}
		if (inside_blanks)
		{
			++count_blanks;
			inside_blanks = false;
		}
		else
		{
			inside_blanks = false;
		}
		cout << "Case #" << i + 1 << ": " << count_blanks * 2 - is_first_balnk << endl;
	}
	return 0;
}

