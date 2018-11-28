#include <iostream>

using namespace std;

int const Max = 22;
int t;
int pole1[Max][Max], pole2[Max][Max];
bool mark[Max];

int main()
{
	freopen("out.txt", "w", stdout);
	cin >> t;
	for (int h = 1; h <= t; h++)
	{
		int a, b;
		cin >> a;
		for (int i = 1; i <= 4; i++)
			for (int j = 1; j <= 4; j++)
				cin >> pole1[i][j];
		cin >> b;
		for (int i = 1; i <= 4; i++)
			for (int j = 1; j <= 4; j++)
				cin >> pole2[i][j];
		for (int i = 0; i < Max; i++)
			mark[i] = false;
		for (int i = 1; i <= 4; i++)
			mark[pole1[a][i]] = true;
		int ans = 0;
		int col = 0;
		for (int i = 1; i <= 4; i++)
			if (mark[pole2[b][i]])
			{
				col = pole2[b][i];
				ans++;
			}
		cout << "Case #" << h << ": ";
		if (ans == 1)
			cout << col << endl;
		if (ans == 0)
			cout << "Volunteer cheated!" << endl;
		if (ans > 1)
			cout << "Bad magician!" << endl;
	}
	return 0;
}