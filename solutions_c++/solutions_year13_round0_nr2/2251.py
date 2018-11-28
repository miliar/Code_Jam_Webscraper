#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <string>
#include <algorithm>
#include <cstdio>
using namespace std;
const long long million = 1000 * 1000;
const long long size_mas = 46;
int mas[million];
const string YES = "YES";
const string NO  = "NO";

string solve()
{
	int n, m;
	cin >> n >> m;
	vector<vector<int> > v(n, vector<int>(m));
	for (int i = 0; i < n; i++)
		for (int j = 0; j < m; j++)
			cin >> v[i][j];

	for (int i = 0; i < n; i++)
		for (int j = 0; j < m; j++)
		{
			int max1, max2, max3, max4;
			max1 = max2 = max3 = max4 = -1;
			for (int k = 0; k < j; k++)
				max1 = max(v[i][k], max1);

			for (int k = j + 1; k < m; k++)
				max2 = max(v[i][k], max2);

			if (v[i][j] >= max1 && v[i][j] >= max2)
				continue;

			for (int k = 0; k < i; k++)
				max3 = max(v[k][j], max3);

			for (int k = i + 1; k < n; k++)
				max4 = max(v[k][j], max4);

			if (v[i][j] >= max3 && v[i][j] >= max4)
				continue;
			else
				return NO;
		}
	return YES;
}
int main()
{
	freopen("input.in","r",stdin);
	freopen("output.txt","w",stdout);
	int TEST_COUNT;
	cin >> TEST_COUNT;
	for (int t = 1;t <= TEST_COUNT; t++)
	{
		cout << "Case #" << t << ": " << solve() << endl;
	}
	return 0;
}