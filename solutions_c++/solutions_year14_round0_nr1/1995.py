#include <iostream>
#include <string>
#include <fstream>
using namespace std;

int main()
{
	ifstream inf("A-small-attempt1.in");
	ofstream outf("14q1.txt");
	int T;
	inf >> T;
	int k;
	for (k = 1;k <= T;k++)
	{
		int a, b, x[2][5][5];
		inf >> a;
		int i, j;
		for (i = 1;i <= 4;i++)
		{
			for (j = 1;j <= 4;j++)
				inf >> x[0][i][j];
		}
		inf >> b;
		for (i = 1;i <= 4;i++)
		{
			for (j = 1;j <= 4;j++)
				inf >> x[1][i][j];
		}
		int cnt = 0;
		int ans;
		for (i = 1;i <= 4;i++)
		{
			for (j = 1;j <= 4;j++)
			{
				if (x[0][a][i] == x[1][b][j])
				{
					cnt++;
					ans = x[0][a][i];
				}
			}
		}
		outf << "Case #" << k << ": ";
		if (cnt == 0)
			outf << "Volunteer cheated!";
		else
		{
			if (cnt == 1)
				outf << ans;
			else
				outf << "Bad magician!";
		}
		outf << endl;
	}
	return 0;
}
