#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <algorithm>
#include <fstream>
#include <math.h>

using namespace std;

int main()
{
	ifstream infile;
	infile.open("data.in");
	ofstream outfile;
	outfile.open("data.out");

	int T;
	infile>>T;

	for (int caseIndex = 1; caseIndex <= T; caseIndex++)
	{
		
		string ans = "";

		int a[101][101];
		int n,m;
		infile>>n>>m;

		int maxRow[101];
		int maxCol[101];

		for (int i = 1; i <= n; i++)
		{
			for (int j = 1; j <= m; j++)
			{
				infile>>a[i][j];
			}
		}

		for (int i = 1; i <= n; i++)
		{
			maxRow[i] = -1;
		}
		for (int j = 1; j <= m; j++)
		{
			maxCol[j] = -1;
		}


		for (int i = 1; i <= n; i++)
		{
			for (int j = 1; j <= m; j++)
			{
				maxRow[i] = max(maxRow[i], a[i][j]);
			}
		}

		for (int i = 1; i <= m; i++)
		{
			for (int j = 1; j <= n; j++)
			{
				maxCol[i] = max(maxCol[i], a[j][i]);
			}
		}

		bool ava = true;
		for (int i = 1; i <= n; i++)
		{
			for (int j = 1; j <= m; j++)
			{
				if (a[i][j] < maxRow[i] && a[i][j] < maxCol[j])
				{
					ava = false;
					break;
				}
			}

			if (!ava)
				break;
		}

		if (ava)
			ans = "YES";
		else
			ans = "NO";
		outfile<<"Case #"<<caseIndex<<": "<<ans<<endl;
		

	}

	infile.close();
	outfile.close();
	return 0;
}