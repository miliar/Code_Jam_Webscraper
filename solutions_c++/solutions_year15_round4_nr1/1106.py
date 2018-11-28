#include <iostream>
#include <istream>
#include <stdio.h>
#include <string>
#include <vector> 
#include <fstream>
#include <queue>
#include <algorithm>
#define INF 2147483647
#define BIG 1000000007

using namespace std; 

int r, c;
char board [100][100];

bool check (int x, int y)
{
	for (int z = x-1; z >= 0; z--)
 	{
 		if (board[z][y] != '.')
			return true;
	}
	for (int z = x+1; z < r; z++)
 	{
 		if (board[z][y] != '.')
			return true;
	}
	for (int z = y-1; z >= 0; z--)
 	{
 		if (board[x][z] != '.')
			return true;
	}
	for (int z = y+1; z < c; z++)
 	{
 		if (board[x][z] != '.')
			return true;
	}
	return false;
}


int main ()
{
    freopen ("A-large.in", "r", stdin);
	freopen ("A.out", "w", stdout); 
 	int tt; 
 	cin >> tt; 
 	for (int cases = 1; cases <= tt; cases++)
 	{
 		cout << "Case #" << cases << ": ";
 		cin >> r >> c;
 		for (int x = 0; x < r; x++)
 			cin >> board[x];
 		bool dead = false;
 		int count = 0;
 		for (int x = 0; x < r; x++)
 		{
 			for (int y = 0; y < c; y++)
 			{
 				if (board[x][y] == '.')
 					continue;
 				bool found = false;
 				if (board[x][y] == '^')
 				{
 					for (int z = x-1; z >= 0; z--)
 					{
 						if (board[z][y] != '.')
						{
							found = true;
							break;
						}	
					}
 					if (found)
 						continue;
 					count++;
 					if (!check (x, y))
 					{
 						dead = true;
						break;	
					}
				}
				if (board[x][y] == 'v')
 				{
 					for (int z = x+1; z < r; z++)
 					{
 						if (board[z][y] != '.')
						{
							found = true;
							break;
						}	
					}
 					if (found)
 						continue;
 					count++;
 					if (!check (x, y))
 					{
 						dead = true;
						break;	
					}
				}
				if (board[x][y] == '<')
 				{
 					for (int z = y-1; z >= 0; z--)
 					{
 						if (board[x][z] != '.')
						{
							found = true;
							break;
						}	
					}
 					if (found)
 						continue;
 					count++;
 					if (!check (x, y))
 					{
 						dead = true;
						break;	
					}
				}
				if (board[x][y] == '>')
 				{
 					for (int z = y+1; z < c; z++)
 					{
 						if (board[x][z] != '.')
						{
							found = true;
							break;
						}	
					}
 					if (found)
 						continue;
 					count++;
 					if (!check (x, y))
 					{
 						dead = true;
						break;	
					}
				}
			}
			if (dead)
				break;	
		}
		if (dead)
			cout << "IMPOSSIBLE\n";
		else
			cout << count << "\n";
	}
}
