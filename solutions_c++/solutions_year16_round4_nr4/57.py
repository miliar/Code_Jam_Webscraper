#include<stdio.h>
#include<vector>
#include<algorithm>
using namespace std;
int map[4][4];
int main()
{
	freopen("d-small-attempt0.in", "r", stdin);
	freopen("small.txt", "w", stdout);
	int data;
	scanf("%d", &data);
	for (int p = 1; p <= data; p++)
	{
		int num;
		scanf("%d", &num);
		for (int i = 0; i < num; i++)
		{
			for (int j = 0; j < num; j++)
			{
				char z;
				scanf(" %c", &z);
				map[i][j] = z - '0';
			}
		}
		int mini = 1000000000;
		for (int q = 0; q < (1 << (num*num)); q++)
		{
			bool flag = true;
			int cnt = 0;
			for (int i = 0; i < num*num; i++)
			{
				if (q&(1 << i))
				{
					if (map[i / num][i%num] == 0)cnt++;
				}
				else
				{
					if (map[i / num][i%num] == 1)cnt = -1000;
				}
			}
			if (cnt < 0)continue;
			int zm[4][4];
			for (int i = 0; i < num; i++)for (int j = 0; j < num; j++)zm[i][j] = map[i][j];
			for (int i = 0; i < num*num; i++)if (q&(1 << i))zm[i / num][i%num] |= 1;
			vector<int>v;
			for (int i = 0; i < num; i++)v.push_back(i);
			for (;;)
			{
				int dp[5][16];
				for (int i = 0; i < 5; i++)for (int j = 0; j < 16; j++)dp[i][j] = 0;
				dp[0][0] = 1;
				for (int i = 0; i < num; i++)
				{
					for (int j = 0; j < (1 << num); j++)
					{
						if (dp[i][j])
						{
							int c = 0;
							for (int k = 0; k < num; k++)
							{
								if (!(j&(1 << k)) && zm[v[i]][k])dp[i + 1][j | (1 << k)] = 1, c++;
							}
							if (c == 0)
							{
								goto l01;
							}
						}
					}
				}
				if (!next_permutation(v.begin(), v.end()))break;
			}
			mini = min(mini, cnt);
		l01:;
		}
		printf("Case #%d: %d\n", p, mini);
	}
}