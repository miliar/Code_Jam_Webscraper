#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <string>
using namespace std;

#define eps 1e-9
#define PB push_back
#define LL long long
#define INF 0x3f3f3f3f

template<class T> void checkMax(T &a, T b){a = max(a, b);}
template<class T> void checkMin(T &a, T b){a = min(a, b);}

const int N = 105;
char grid[N][N];
int n, m, dir[4][2] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
int inRange(int x, int y)
{
	return (0 <= x && x < n && 0 <= y && y < m);
}
int main()
{
	int t, cas = 1;
	map<char, int> d2i;
	d2i['v'] = 0;
	d2i['^'] = 1;
	d2i['>'] = 2;
	d2i['<'] = 3;
	scanf("%d", &t);
	while(t--)
	{
		scanf("%d%d", &n, &m);
		for(int i = 0; i < n; i++)
			scanf("%s", grid[i]);
		int ans = 0, impossible = 0;
		for(int i = 0; i < n; i++)
		{
			for(int j = 0; j < m; j++)
			{
				if(grid[i][j] == '.')
					continue;
				int can = 0, cnt = 0;
				for(int k = 0; k < 4; k++)
				{
					int x = i, y = j;
					while(1)
					{
						x += dir[k][0];
						y += dir[k][1];
						if(!inRange(x, y))
							break;
						if(grid[x][y] != '.')
						{
							cnt++;
							if(k == d2i[grid[i][j]])
								can = 1;
							break;
						}
					}
				}
				if(can)	continue;
				if(cnt == 0)	impossible = 1;
				else			ans++;
			}
		}
		if(impossible)	printf("Case #%d: IMPOSSIBLE\n", cas++);
		else			printf("Case #%d: %d\n", cas++, ans);
	}
    return 0;
}
