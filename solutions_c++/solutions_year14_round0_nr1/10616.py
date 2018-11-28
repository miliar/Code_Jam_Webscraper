#include<iostream>
using namespace std;

int main()
{
	int t, map1[4][4], map2[4][4], no = 0;
	cin >> t;
	while (t--)
	{
		int firstrow, secondrow;
		cin >> firstrow;
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++)
				cin >> map1[i][j];
		cin >> secondrow;
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++)
				cin >> map2[i][j];
		int cnt = 0, ans = 0;
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++)
				if (map1[firstrow - 1][i] == map2[secondrow - 1][j])
				{
					cnt++;
					ans = map1[firstrow - 1][i];
				}
		cout << "Case #" << ++no << ": ";
		if (cnt == 0)
			cout << "Volunteer cheated!" << endl;
		else if (cnt == 1)
			cout << ans << endl;
		else
			cout << "Bad magician!" << endl;
	}
}