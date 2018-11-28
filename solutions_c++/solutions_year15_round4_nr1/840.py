#include<iostream>
#include<fstream>
#include<vector>
#include<stack>
#include<queue>
#include<algorithm>
#include<functional>

char map[100][100];
int arrowr[10000], arrowc[10000];

using namespace std;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	
	int T;
	cin >> T;
	for(int kase = 1; kase <= T; ++kase)
	{
		int r, c, arrow = 0;
		cin >> r >> c;

		for(int i = 0; i < r; ++i)
		for(int j = 0; j < c; ++j)
		{
			cin >> map[i][j];
			//printf("%c\n", map[i][j]);
			if(map[i][j] != '.')
			{
				arrowr[arrow] = i;
				arrowc[arrow] = j;
				++arrow;
			}
		}

		if(arrow == 0) 
		{
			printf("Case #%d: 0\n", kase);
			continue;
		}

		int ans = 0;
		bool print = true;
		for(int idx = 0; idx < arrow; ++idx)
		{
			int x = arrowr[idx], y = arrowc[idx];
				
			bool check = false, check2 = false;
			for(int i = 0; i < r; ++i)
			{
				if(map[i][y] != '.' && x != i)
				{
					check = true;
					if(i < x && map[x][y] == '^') check2 = true;
					if(i > x && map[x][y] == 'v') check2 = true;
				}	
			}
			for(int i = 0; i < c; ++i)
			{
				if(map[x][i] != '.' && y != i)
				{
					check = true;
					if(i < y && map[x][y] == '<') check2 = true;
					if(i > y && map[x][y] == '>') check2 = true;
				}
			}

			if(!check)
			{
				printf("Case #%d: IMPOSSIBLE\n", kase);
				print = false;
				break;
			}

			if(!check2) ++ ans;
		}
		
		if(print) printf("Case #%d: %d\n", kase, ans);


	}

	return 0;
}

