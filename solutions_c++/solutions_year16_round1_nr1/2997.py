#include <iostream>
#include <string>

using namespace std;
string Answer;
string s;

int main()
{
	int T;

	cin >> T;

	for (int test_case = 1; test_case <= T; test_case++)
	{
		cin >> s;

		
		Answer = "";
		int last = 0;

		for (int i = 0; i < s.length(); i++)
		{
			if (i == 0)
			{
				Answer += s[i];
				last++;
			}
			else
			{
				if (s[i] < Answer[0])
				{
					Answer += s[i];
				}
				else
				{
					Answer = s[i] + Answer;
				}
			}
		}

		cout << "Case #" << test_case << ": ";
		cout << Answer << endl;
	}

	return 0;
}