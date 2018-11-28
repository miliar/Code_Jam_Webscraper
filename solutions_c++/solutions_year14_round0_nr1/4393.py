#include <iostream>
#include <fstream>
using namespace std;

int a[4][4], b[4][4];

void solve()
{
	int row1, row2, i, j, count, card;
	bool find;
	
	cin >> row1;
	for (i = 0; i < 4; i++)
		for (j = 0; j < 4; j++)
			cin >> a[i][j];
	cin >> row2;
	for (i = 0; i < 4; i++)
		for (j = 0; j < 4; j++)
			cin >> b[i][j];
	
	row1--;
	row2--;
	count = 0;
	for (i = 0; i < 4; i++)
	{
		find = false;
		for (j = 0; j < 4; j++)
			if (a[row1][i] == b[row2][j])
			{
				find = true;
				break;
			}
		if (find)
		{
			if (++count > 1) break;
			card = a[row1][i];
		}
	}
	if (count == 1) cout << card << endl;
	else if (count == 0) cout << "Volunteer cheated!\n";
	else cout << "Bad magician!\n";
}

ifstream fin("A-small-attempt0.in");
ofstream fout("a.out");

int main()
{
	int t, i;
	
	cin.rdbuf(fin.rdbuf());
	cout.rdbuf(fout.rdbuf());
	
	cin >> t;
	for (i = 1; i <= t; i++)
	{
		cout << "Case #" << i << ": ";
		solve();
	}
	
	return 0;
}