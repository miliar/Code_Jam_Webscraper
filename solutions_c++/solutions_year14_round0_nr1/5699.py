#include<cstdlib>
#include<cctype>
#include<cstring>
#include<cstdio>
#include<cmath>
#include<algorithm>
#include<vector>
#include<string>
#include<map>
#include<iostream>
#include<sstream>
#include<fstream>
#include<bitset>
#include<list>
using namespace std;
int main()
{

	freopen("E:\\A.in", "r", stdin);
	freopen("E:\\B.out", "w", stdout);

	int T;
	int start_square[4][4];
	int end_square[4][4];

	scanf("%d", &T);
	for (int cas = 0; cas < T; cas++)
	{
		memset(start_square,0,16*sizeof(int));
		memset(end_square,0,16*sizeof(int));
		int n = 0;
		int m = 0;
		scanf("%d", &n);
		for (int i = 0; i < 4; ++i)
		{
			for (int j = 0; j < 4; j++)
			{
				scanf("%d", &start_square[i][j]);
			}
		}
		scanf("%d", &m);
		for (int i = 0; i < 4; ++i)
		{
			for (int j = 0; j < 4; j++)
			{
				scanf("%d", &end_square[i][j]);
			}
		}
		putchar(10);

		int num = 0;
		int ans = 0;

		for (int i = 0; i < 4; i++)
		{
			for (int j = 0; j < 4; ++j)
			{
				char a = start_square[n-1][i];
				char b = end_square[m-1][j];
				if (a == b)
				{
					ans = start_square[n-1][i];
					num++;
				}
			}
		}
		if (num == 1)
		{
			printf("Case #%d: %d", cas + 1, ans);
		}
		else if (num == 0)
		{
			printf("Case #%d: Volunteer cheated!", cas + 1);
		}
		else
		{
			printf("Case #%d: Bad magician!", cas + 1);
		}
	}

	return 0;
}
