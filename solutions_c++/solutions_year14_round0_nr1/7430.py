#include <iostream>
#include <string.h>

using namespace std;

int main()
{
	int T;
	int num[17];

	cin >> T;
	for (int t = 1; t <= T; ++t)
	{
		memset(num, 0, sizeof(num));

		int ans1, ans2;
		cin >> ans1;
		for (int i = 1; i <= 4; i++)
		{
			for (int j = 1; j <= 4; j++)
			{
				int tmp;
				cin >> tmp;
				if (i == ans1)
				{
					num[tmp]++;
				}
			}
		}

		cin >> ans2;
		for (int i = 1; i <= 4; i++)
		{
			for (int j = 1; j <= 4; j++)
			{
				int tmp;
				cin >> tmp;
				if (i == ans2)
				{
					num[tmp]++;
				}
			}
		}

		int card = 0;
		bool gotcard = false, bad = false;
		for (int n = 1; n <= 16; n++)
		{
			if (num[n] == 2)
			{
				if (!gotcard)
				{
					card = n;
					gotcard = true;
				}
				else
				{
					bad = true;
					break;
				}
			}
		}

		cout << "Case #" << t << ": ";
		if (bad)
			cout << "Bad magician!" << endl;
		else if (gotcard)
			cout << card << endl;
		else
			cout << "Volunteer cheated!" << endl;
	}

	return 0;
}
