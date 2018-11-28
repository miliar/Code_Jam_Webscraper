#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <cmath>

using namespace std;
const int X = 17;
int table1[X][X], table2[X][X], cnt1[X], cnt2[X];

int main()
{
	int i, j, n, m, test, cnt_test, cnt;
	
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	cin >> cnt_test;
	for(test = 0; test < cnt_test; test++)
	{
		cin >> n;
		for(i = 0; i < X; i++) cnt1[i] = 0, cnt2[i] = 0;
		for(i = 0; i < 4; i++)
		{
			for(j = 0; j < 4; j++)
			{
				cin >> table1[i][j];
			}
		}
		cin >> m;
		for(i = 0; i < 4; i++)
		{
			for(j = 0; j < 4; j++)
			{
				cin >> table2[i][j];
			}
		}
		for(i = 0; i < 4; i++)cnt1[table1[n - 1][i]] = 1, cnt2[table2[m - 1][i]] = 1;
		cnt = 0;
		for(i = 0; i < X; i++)
		{
			if(cnt1[i] && cnt2[i]) cnt++;
		}
		if(cnt == 0)
		{
			cout << "Case #" << test + 1 << ": Volunteer cheated!\n";
		}
		else if(cnt == 1)
		{
			cout << "Case #"<< test + 1 <<": ";
			for(i = 0; i < X; i++)
			{
				if(cnt1[i] && cnt2[i]) cout << i << '\n';
			}
		}
		else
		{
			cout << "Case #"<< test + 1 <<": Bad magician!\n";
		}
	}
	return 0;
}