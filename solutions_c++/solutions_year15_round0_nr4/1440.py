#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <string>
using namespace std;

int main()
{
	freopen("D-small-attempt1.in", "r", stdin);
	freopen("d.out", "w", stdout);
	int map[5][5][5];
	int x = 1, r = 1, c = 1;
	for(r = 1; r <= 4; r++)
	{
		for(c = 1; c <= 4; c++)
		{
			map[x][r][c] = 0;
		}
	}
	x++;
	r = 1, c = 1;
	for(r = 1; r <= 4; r++)
	{
		for(c = 1; c <= 4; c++)
		{
			if(r * c % x == 0)
			{
				map[x][r][c] = 0;
			}
			else
				map[x][r][c] = 1;
		}
	}
	
	map[3][1][1] = 1;
	map[3][1][2] = 1;
	map[3][1][3] = 1;
	map[3][1][4] = 1;
	map[3][2][1] = 1;
	map[3][2][2] = 1;
	map[3][2][3] = 0;
	map[3][2][4] = 1;
	map[3][3][1] = 1;
	map[3][3][2] = 0;
	map[3][3][3] = 0;
	map[3][3][4] = 0;
	map[3][4][1] = 1;
	map[3][4][2] = 1;
	map[3][4][3] = 0;
	map[3][4][4] = 1;
	
	map[4][1][1] = 1;
	map[4][1][2] = 1;
	map[4][1][3] = 1;
	map[4][1][4] = 1;
	map[4][2][1] = 1;
	map[4][2][2] = 1;
	map[4][2][3] = 1;
	map[4][2][4] = 1;
	map[4][3][1] = 1;
	map[4][3][2] = 1;
	map[4][3][3] = 1;
	map[4][3][4] = 0;
	map[4][4][1] = 1;
	map[4][4][2] = 1;
	map[4][4][3] = 0;
	map[4][4][4] = 0;
	
	int T;
	while(cin >> T)
	{
		for(int i = 1; i <= T; i++)
		{
			int X, R, C;
			cin >> X >> R >> C;
			if(map[X][R][C] == 0)
				cout << "Case #" << i << ": " << "GABRIEL" << endl;
			else
				cout << "Case #" << i << ": " << "RICHARD" << endl;
		}
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}
