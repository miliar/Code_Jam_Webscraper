#include<iostream>
#include<cstdio>
#include<string>
#include<set>
#include<algorithm>
#include<vector>
#include<map>
#include<cmath>
#include<queue>
using namespace std;

void Solution()
{
	int r[2];
	int m[2][4][4];
	for (int i = 0; i < 2; i++)
	{
		cin >> r[i];
		r[i]--;
		for (int x = 0; x < 4; x++)
			for (int y = 0; y < 4; y++)
				cin >> m[i][x][y];
	}

	set<int> can;
	for (int x = 0; x < 4; x++)
		for (int y = 0; y < 4; y++)
			if (m[0][r[0]][x] == m[1][r[1]][y])
				can.insert(m[0][r[0]][x]);
		
	if (can.size() == 0)
		cout << "Volunteer cheated!";
	if (can.size() == 1)
		cout << *can.begin();
	if (can.size() > 1)
		cout << "Bad magician!";
}

int main()
{
#ifdef LOCAL
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
#endif

	int T;
	cin >> T;
	for (int t = 1; t <= T; t++)
	{
		printf("Case #%d: ", t);
		Solution();
		printf("\n");
	}
}