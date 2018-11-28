#include <iostream>

using namespace std;

int main(void)
{
	int count = 0;
	int arrayfirst[4][4] = { 0 };
	int arraysecond[4][4] = { 0 };
	int first = 0;
	int second = 0;
	int num = 0;
	int res = 0;
/*	freopen("A-small-attempt3.in", "r", stdin);
	freopen("A-small-attempt3.out", "w", stdout);
*/	cin >> count;
	for (int i = 0; i < count; i++)
	{
		num = 0;
		res = 0;
		cin >> first;
		first--;
		for (int j = 0; j < 4; j++)
		{
			for (int k = 0; k < 4; k++)
			{
				cin >> arrayfirst[j][k];
			}
		}
		cin >> second;
		second--;
		for (int j = 0; j < 4; j++)
		{
			for (int k = 0; k < 4; k++)
			{
				cin >> arraysecond[j][k];
			}
		}
		for (int j = 0; j < 4; j++)
		{
			for (int k = 0; k < 4; k++)
			{
				if (arrayfirst[first][j] == arraysecond[second][k])
				{
					num++;
					res = arrayfirst[first][j];
				}
			}
		}
		cout << "Case #";
		cout << i + 1 << ": ";
		switch (num)
		{
		case 1:
			cout << res;
			break;
		case 0:
			cout << "Volunteer cheated!";
			break;
		default:
			cout << "Bad magician!";
			break;
		}
		cout << "\n";
	}
	return 0;
}