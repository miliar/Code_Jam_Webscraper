#include <bits/stdc++.h>
using namespace std;

int main()
{
	int T, t;
	cin >> T;
	for(t = 1; t <= T; ++t)
	{
		int row1;
		cin >> row1;
		int a[4], ans[4], i, j;
		for(i = 1; i <= 4; ++i)
		{
			for(j = 0; j < 4; ++j)
			{
				cin >> a[j];
			}
			if(i == row1)
			{
				for(j = 0; j < 4; ++j)
				{
					ans[j] = a[j];
				}
			}
		}
		int row2, flag = 0, card;
		cin >> row2;
		for(i = 1; i <= 4; ++i)
		{
			for(j = 0; j < 4; ++j)
			{
				cin >> a[j];
			}
			if(i == row2)
			{
				for(j = 0; j < 4; ++j)
				{
					for(int k = 0; k < 4; ++k)
					{
						if(ans[j] == a[k])
						{
							++flag;
							card = a[k];
						}
					}
				}
			}
		}
		cout << "Case #" << t << ": ";
		if(flag == 0)
		{
			cout << "Volunteer cheated!\n";
		}
		else if(flag == 1)
		{
			cout << card << endl;
		}
		else
		{
			cout << "Bad magician!\n";
		}
	}
	return 0;
}
