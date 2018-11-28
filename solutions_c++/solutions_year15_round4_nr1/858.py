#if 0==0

#include<iostream>
#include<cstdio>
#include<vector>
#include<algorithm>
#include<string>

using namespace std;

string map[101];

int main()
{
	
	//freopen("A-small.in", "r", stdin);
	//freopen("A-small.out", "w", stdout);
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	
	int i_ans;

	int T;
	
	scanf("%d", &T);
	for (int i_case = 1 ; i_case <= T ; i_case++)
	{		
		int r, c;

		scanf("%d%d", &r, &c);

		for (int i = 0 ; i < r ; i++)
		{
			cin>>map[i];	
		}

		bool ok = true;
		int ans = 0;

		for (int i = 0 ; i < r ; i++)
			for (int j = 0 ; j < c ; j++)
				if (map[i][j] != '.')
				{
					bool good = false;
					if (map[i][j] == '<')
					{
						for (int x = j - 1 ; x >= 0 ; x--)
							if (map[i][x] != '.') good = true;
					} else
					if (map[i][j] == '>')
					{
						for (int x = j + 1 ; x < c ; x++)
							if (map[i][x] != '.') good = true;
					} else
					if (map[i][j] == '^')
					{
						for (int x = i - 1 ; x >= 0 ; x--)
							if (map[x][j] != '.') good = true;
					} else
					if (map[i][j] == 'v')
					{
						for (int x = i + 1 ; x < r ; x++)
							if (map[x][j] != '.') good = true;
					}

					if (!good)
					{
						for (int x = j - 1 ; x >= 0 ; x--)
							if (map[i][x] != '.') good = true;
						for (int x = j + 1 ; x < c ; x++)
							if (map[i][x] != '.') good = true;
						for (int x = i - 1 ; x >= 0 ; x--)
							if (map[x][j] != '.') good = true;
						for (int x = i + 1 ; x < r ; x++)
							if (map[x][j] != '.') good = true;

						if (!good)
						{
							ok = false;
						} else
						{
							ans++;
						}
					}
				}

		printf("Case #%d: ", i_case);

		if (ok)
			printf("%d\n", ans);
		else
			printf("IMPOSSIBLE\n");
	}

	return 0;
}

#endif