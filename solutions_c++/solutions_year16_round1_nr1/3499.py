#include <iostream>
#include <string>

using namespace std;

int T, cases = 1;
string s;

int main()
{
	freopen("input.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	cin >> T;

	while (cases <= T)
	{
		cin >> s;

		string t(1, s[0]);

		for (int i = 1; i < s.length(); i++)
		{
			if (s[i] >= t[0])
			{
				t = s[i] + t;
			}

			else
				t = t + s[i];
		}

		cout << "Case #" << cases << ": " << t << endl;

		cases++;
	}

	return 0;
}