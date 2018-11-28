#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main()
{
	int t, cases = 1, flips = 0;
	string str;

	freopen("input.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	cin >> t;

	while (cases <= t)
	{
		cin >> str;

		reverse(str.begin(), str.end());

		for (int i = 0; i < str.length(); i++)
		{
			if (str[i] == '+')
			{
				continue;
			}

			else
			{
				flips++;
				replace(str.begin(), str.end(), '+', 't');
				replace(str.begin(), str.end(), '-', '+');
				replace(str.begin(), str.end(), 't', '-');
			}
		}

		cout << "Case #" << cases << ": " << flips << endl;
		flips = 0;
		cases++;
	}

	return 0;
}