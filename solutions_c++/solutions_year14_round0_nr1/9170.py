#include<iostream>
using namespace std;

int main()
{
	int T;
	int firstArrangement[16];
	int secondArrangement[16];
	int x, icard,y;
	int firstRow, secondRow, found, ifirstRow, isecondRow;
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	cin >> T;
	for (x = 1; x <= T; x++)
	{
		cin >> firstRow;
		for (icard = 0; icard < 16; icard++)
			cin >> firstArrangement[icard];
		cin >> secondRow;
		for (icard = 0; icard < 16; icard++)
			cin >> secondArrangement[icard];
		found = 0;
		for (ifirstRow = (firstRow - 1) * 4; ifirstRow < firstRow * 4; ifirstRow++)
		{
			for (isecondRow = (secondRow - 1) * 4; isecondRow < secondRow * 4; isecondRow++)
			{
				if (firstArrangement[ifirstRow] == secondArrangement[isecondRow])
				{
					found++;
					y = firstArrangement[ifirstRow];
				}
			}

		}
		cout << "Case #" << x << ": ";
		if (found==0)
		{
			cout << "Volunteer cheated!\n";
		}
		else if (found == 1)
		{
			cout << y << '\n';
		}
		else
		{
			cout << "Bad magician!\n";
		}
	}
}