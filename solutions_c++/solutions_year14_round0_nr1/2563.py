#include <iostream>
#include <cstdio>
#include <cstring>
#include <queue>
#include <vector>
#include <algorithm>
using namespace std;
#define mid ((l+r)>>1)
const long long INF = 1e9 + 7;
int a[4][4];
int b[4][4];
int main()
{
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small-attempt0.out", "w", stdout);
	int ncase;
	cin >> ncase;
	int ks = 1;
	while (ncase--)
	{
		int r1, r2;
		cin >> r1;
		for (int i = 0; i < 4; i++)
		{
			for (int j = 0; j < 4; j++)
			{
				cin >> a[i][j];
			}
		}
		cin >> r2;
		for (int i = 0; i < 4; i++)
		{
			for (int j = 0; j < 4; j++)
			{
				cin >> b[i][j];
			}
		}
		r1--;
		r2--;
		int ans;
		int cnt = 0;
		for (int i = 0; i < 4; i++)
		{
			for (int j = 0; j < 4; j++)
			{
				if (a[r1][i] == b[r2][j])
				{
					cnt++;
					ans = a[r1][i];
				}
			}
		}
		if (cnt == 0) printf("Case #%d: Volunteer cheated!\n", ks++);
		else if (cnt == 1) printf("Case #%d: %d\n", ks++, ans);
		else printf("Case #%d: Bad magician!\n", ks++);
	}
	return 0;
}