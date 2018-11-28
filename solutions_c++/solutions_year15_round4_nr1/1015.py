#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <map>
#include <queue>
#include <set>
#include <string>
#include <vector>

using namespace std;

enum class DIR
{
	None,
	Up,
	Right,
	Down,
	Left
};

DIR grid[110][110];
int R, C;

char line[110];

int solve()
{
	int ans = 0;
	
	for (int i=0; i<R; ++i)
	{
		for (int j=0; j<C; ++j)
		{
			if (grid[i][j] == DIR::None)
			{
				continue;
			}

			bool foundUp = false;
			bool foundRight = false;
			bool foundDown = false;
			bool foundLeft = false;

			// up
			for (int k=i-1; k>=0; --k)
			{
				if (grid[k][j] != DIR::None)
				{
					foundUp = true;
					break;
				}
			}

			// right
			for (int k=j+1; k<C; ++k)
			{
				if (grid[i][k] != DIR::None)
				{
					foundRight = true;
					break;
				}
			}

			// down
			for (int k=i+1; k<R; ++k)
			{
				if (grid[k][j] != DIR::None)
				{
					foundDown = true;
					break;
				}
			}

			// left
			for (int k=j-1; k>=0; --k)
			{
				if (grid[i][k] != DIR::None)
				{
					foundLeft = true;
					break;
				}
			}

			if (foundUp == false && foundRight == false
				&& foundDown == false && foundLeft == false)
			{
				return -1;
			}

			int count = 0;
			switch (grid[i][j])
			{
			case DIR::Up:
				if (foundUp == false)
				{
					++count;
				}
				break;
			case DIR::Right:
				if (foundRight == false)
				{
					++count;
				}
				break;
			case DIR::Down:
				if (foundDown == false)
				{
					++count;
				}
				break;
			case DIR::Left:
				if (foundLeft == false)
				{
					++count;
				}
				break;
			}

			ans += count;
		}
	}
	
	return ans;
}

int main()
{
	int t;
	scanf("%d", &t);
	for (int tc=1; tc<=t; ++tc)
	{
		scanf("%d %d", &R, &C);
		for (int i=0; i<R; ++i)
		{
			scanf("%s", line);
			for (int j = 0; j < C; ++j)
			{
				switch (line[j])
				{
					case '.':
						grid[i][j] = DIR::None;
						break;
					case '^':
						grid[i][j] = DIR::Up;
						break;
					case '>':
						grid[i][j] = DIR::Right;
						break;
					case 'v':
						grid[i][j] = DIR::Down;
						break;
					case '<':
						grid[i][j] = DIR::Left;
						break;
				}
			}
		}
		
		printf("Case #%d: ", tc);
		int ans = solve();
		if (ans < 0)
		{
			printf("IMPOSSIBLE");
		}
		else
		{
			printf("%d", ans);
		}

		printf("\n");
	}
	
	return 0;
}