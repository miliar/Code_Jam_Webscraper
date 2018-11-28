#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <climits>
#include <cassert>

using namespace std;
typedef long long ll;
#define MODD(a,b) (((a)%(b)+(b))%(b))
#define EPS 1E-9
#define REP(i,s,t) for(int i=(s);i<(t);i++)
#define FILL(x,v) memset(x,v,sizeof(x))

vector<string> m;
int b[105][105];
int dx[4] = {0,1,0,-1};
int dy[4] = { 1, 0, -1, 0 };

char dc[4] = {'>', 'v', '<', '^'};


int main()
{
	int __t;
	cin >> __t;

	for (int cs = 1; cs <= __t; cs++)
	{
		FILL(b, 0);
		printf("Case #%d: ", cs);
		int r, c;
		cin >> r >> c;
		m.clear();
		m.resize(r);
		for (int i = 0; i < r; i++)
			cin >> m[i];
		
		for (int d = 0; d < 4; d++)
		{
			for (int i = 0; i < r; i++)
				for (int j = 0; j < c; j++)
				{
					if (m[i][j] != '.')
					{
						int x = i, y = j;
						bool hit = 0;
						while (1)
						{
							x += dx[d];
							y += dy[d];
							if (!(x >= 0 && x < r && y >= 0 && y < c)) break;
							if (m[x][y] != '.') {
								hit = 1; break;
							}
						}
						b[i][j] += (!hit);
						char tmp = m[i][j];
						if (hit && dc[d] == m[i][j])
						{
							b[i][j] = -10;
						} 
					}
				}
		}
		bool bad = 0;
		int ans = 0;
		for (int i = 0; i < r && !bad; i++)
			for (int j = 0; j < c && !bad; j++)
			{
				if (b[i][j] == 4) bad = 1;
				else ans += (b[i][j] > 0);
			}
		if (bad) puts("IMPOSSIBLE");
		else printf("%d\n", ans);
	}

	
	return 0;
}