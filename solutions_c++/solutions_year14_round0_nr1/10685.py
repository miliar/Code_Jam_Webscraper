#include <iostream>
using namespace std;
int main()
{
	int n,cntr2=1;
	cin >> n;
	while (n--)
	{
		int ans1,ans2;
		cin >> ans1;
		ans1--;
		int card1[4][4],card2[4][4];
		for (int i = 0; i < 4; i++)
		{
			for (int j = 0; j < 4; j++)
			{
				cin >> card1[i][j];
			}
		}
		cin >> ans2;
		for (int i = 0; i < 4; i++)
		{
			for (int j = 0; j < 4; j++)
			{
				cin >> card2[i][j];
			}
		}
		int res;
		int cntr = 0;
		ans2--;
		for (int i = 0; i < 4; i++)
		{
			for (int j = 0; j < 4; j++)
			{
				if (card1[ans1][i] == card2[ans2][j])
				{
					res = card1[ans1][i];
					cntr++;
				}
			}
		}
		if (cntr == 0)
			cout <<"Case #"<< cntr2 <<": Volunteer cheated!" << endl;
		else if (cntr > 1)
			cout <<"Case #" << cntr2 << ": Bad magician!" << endl;
		else cout <<"Case #" << cntr2 <<": "<< res << endl;
		cntr2++;
	}
}