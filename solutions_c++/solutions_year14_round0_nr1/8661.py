#include<map>
#include<set>
#include<iostream>
#include<string.h>
#include<string>
#include<queue>
#include<cmath>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<memory.h>
using namespace std;

#define mp make_pair
#define X first
#define Y second

double const eps = 1e-10;
int const INF = 100000;
int const MOD = 1;
int const MAX = 1000 + 5;

int a[3][20];

void read(int k)
{
	for(int i = 0; i < 4; ++i)
		for(int j = 0; j < 4; ++j)
		{
			int x;
			cin >> x;
			a[k][x] = i + 1;
		}
}

int main()
{
#ifdef _DEBUG
    freopen("in.txt", "rt", stdin);
	freopen("out.txt", "wt", stdout);
#endif
	int t, i, j, x, y;
	cin >> t;
	for(j = 0; j < t; ++j)
	{
		memset(a, 0, sizeof(a));
		cin >> x;
		read(0);
		cin >> y;
		read(1);
		int cnt = 0, ans = 0;
		for(i = 1; i < 17; ++i)
			if(a[0][i] == x &&a[1][i] == y)
			{
				++ cnt;
				ans = i;
			}
		cout << "Case #" << j + 1 << ": ";
		if(cnt == 0)
			cout << "Volunteer cheated!";
		if(cnt == 1)
			cout << ans;
		if(cnt > 1)
			cout << "Bad magician!";
		cout << endl;
	}

	return 0;
}