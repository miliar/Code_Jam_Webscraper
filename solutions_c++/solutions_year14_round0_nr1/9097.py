#include <cstdio>
#include <iostream>

using namespace std;

int cnt[17];

int main()
{
	int TC;
	cin >> TC;
	for (int tc = 1; tc <= TC; tc++)
	{
		int i;
		for (i = 1; i <= 16; i++)
			cnt[i] = 0;

		for (int t = 0; t < 2; t++)
		{
			int ans, i, j;

			cin >> ans;
			for (i = 1; i <= 4; i++)
			{
				for (j = 1; j <= 4; j++)
				{
					int x;
					cin >> x;
					if (i == ans)
						cnt[x]++;
				}
			}
		}
		int anscnt = 0;
		int ans;
		for (i = 1; i <= 16; i++)
		{
			if (cnt[i] == 2)
			{
				anscnt++;
				ans = i;
			}
		}
		cout << "Case #" << tc << ": ";
		if (anscnt == 0)
			cout << "Volunteer cheated!";
		if (anscnt > 1)
			cout << "Bad magician!";
		if (anscnt == 1)
			cout << ans;

		cout << endl;
	}
}