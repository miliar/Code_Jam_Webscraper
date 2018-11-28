#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <unordered_map>
#include <utility>
#include <cmath>
using namespace std;
const int maxn = 105; 
char b[maxn][maxn]; 

int n, m; 

bool safe(int i, int j, char dir)
{
	int di, dj; 
	di = dj = 0; 
	if (dir == '>') dj = 1; 
	else if (dir == '<') dj = -1; 
	else if (dir == 'v') di = 1; 
	else di = -1; 

	i += di; j += dj; 
	while (i>=0 && i<n && j>=0 && j<m)
	{
		if (b[i][j] != '.') return true; 
		i += di; 
		j += dj; 
	}
	return false; 
}
int main()
{
	int T, I=0; 
	int i, j, d, ans; 
	bool fail; 
	string dir = "^>v<"; 

	scanf ("%d", &T); 
	while (++ I <= T)
	{
		scanf ("%d%d", &n, &m); 
		for (i=0; i<n; i++)
			scanf ("%s", b[i]); 

		fail = false; 
		ans = 0; 
		for (i=0; i<n && !fail; i++)
		{
			for (j=0; j<m && !fail; j++) if (b[i][j] != '.')
			{
				if (safe(i, j, b[i][j]) == false)
				{
					for (d=0; d<4; d++) 
					{
						if (dir[d] != b[i][j] && safe(i, j, dir[d]))
						{
							b[i][j] = dir[d]; 
							ans++; 
							break; 
						}
					}
					if (d == 4) fail = true; 
				}
			}
		}

		printf ("Case #%d: ", I); 
		if (fail)
			printf ("IMPOSSIBLE\n"); 
		else
			printf ("%d\n", ans); 
	}
}