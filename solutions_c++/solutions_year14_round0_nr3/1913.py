/*
    Title:
    Author: RudySnow
    Algorithm:
    Date:
    License: GNU GPL
    Quote: Night Gathers, and My Watch Begins, it shall Never End until My Death
*/

#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <memory.h>
#include <cstring>
#include <cmath>
#include <ctime>
#include <algorithm>
#include <set>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <bitset>

using namespace std;

int t, r, c, m;
int ans = 0;
int num = 0;
int flag[30] = {0};
int vis[30] = {0};

typedef pair<int, int> P;
int dir[8][2] = {{-1, -1}, {-1, 0}, {-1, 1}, {0, -1}, {0, 1}, {1, -1}, {1, 0}, {1, 1}};

void bfs(int x, int y)
{
    queue<P> que;

    que.push(P(x, y));
    vis[x*r+y] = 1;
    ans = 1;

    while(que.size())
    {
        //cout << "Hey" << endl;

        P p = que.front();
        que.pop();

        int mark = 1;
        for(int i = 0; i < 8; ++i)
        {
            int nx = p.first + dir[i][0], ny = p.second + dir[i][1];
            if(nx >= 0 && nx < r && ny >= 0 && ny < c)
            {
                if(flag[nx*r+ny] == 1) mark = 0;
            }
        }
        if(mark)
        {
            for(int i = 0; i < 8; ++i)
            {
                int nx = p.first + dir[i][0], ny = p.second + dir[i][1];
                if(nx >= 0 && nx < r && ny >= 0 && ny < c && vis[nx*r+ny] == 0)
                {
                    vis[nx*r+ny] = 1;
                    ans++;
                    //cout << ans << endl;
                    //system("pause");
                    que.push(P(nx, ny));
                }
            }
        }
    }
}

int dfs()
{
	int comb = (1 << m) - 1;
	memset(flag, 0, sizeof(flag));
	int i = 1;
	int j = 0;
	while(true)
	{
		if(i & comb)
		{
			flag[j] = 1;
		}
		++j;
		i*=2;
		if(j >= r*c) break;
	}

	int res = r * c - m;

	for(int x = 0; x < r; ++x)
	{
		for(int y = 0; y < c; ++y)
		{
			if(flag[x*r+y] == 0)
			{
				ans = 0;
				memset(vis, 0, sizeof(vis));
				bfs(x, y);
				if(ans == res)
				{
					cout << "Case #" << num << ": " << endl;
					for(int l = 0; l < r; ++l)
					{
						for(int g = 0; g < c; ++g)
						{
							if(l == x && g == y) cout << "c";
							else if(flag[l*r+g] == 1) cout << "*";
							else cout << ".";
						}
						cout << endl;
					}
					return 1;
				}
			}
		}
	}

	while(comb < 1 << r*c)
	{
		int p1 = comb & -comb, p2 = comb + p1;
		comb = ((comb & ~p2) / p1 >> 1) | p2;

		memset(flag, 0, sizeof(flag));
		int i = 1;
		int j = 0;
		int ans1 = 0;
		while(true)
		{
			if(i & comb)
			{
				flag[j] = 1;
				++ans1;
			}
			++j;
			i*=2;
			if(j >= r*c) break;
		}

		ans1 = 0;
		for(int i = 0; i < r; ++i)
		{
			for(int j = 0; j < c; ++j)
			{
				if(flag[i*r+j]) ans1++;
			}
		}
		if(ans1 == 4) cout << "WTF" << endl;

		for(int x = 0; x < r; ++x)
		{
			for(int y = 0; y < c; ++y)
			{
				if(flag[x*r+y] == 0)
				{
					ans = 0;
					memset(vis, 0, sizeof(vis));
					bfs(x, y);
					if(x*r+y == 8 && flag[6] && flag[13] && flag[23])
					{

						cout << ans << endl;
						for(int l = 0; l < r; ++l)
						{
							for(int g = 0; g < c; ++g)
							{
								if(flag[l*r+g] == 1) cout << "*";
								else if(x==l && y==g) cout << "c";
								else cout << ".";
							}
							cout << endl;
						}
						cout << endl;
					}
					if(ans == res)
					{
						cout << "Case #" << num << ": " << endl;
						for(int l = 0; l < r; ++l)
						{
							for(int g = 0; g < c; ++g)
							{
								if(l == x && g == y) cout << "c";
								else if(flag[l*r+g] == 1) cout << "*";
								else cout << ".";
							}
							cout << endl;
						}
						return 1;
					}
				}
			}
		}
	}
	return 0;
}

void Solve()
{
    //cout << "Begin" << endl;
    memset(flag, 0, sizeof(flag));
    if(dfs() == 0)
    {
        cout << "Case #" << num << ": " << endl << "Impossible" << endl;
    }
}

int main()
{
    //freopen("B-large.in", "r", stdin);
    //freopen("B-1.out", "w", stdout);

    cin >> t;
    int tFirst = t;
    while(t--)
    {
        cin >> r >> c >> m;
        num = tFirst - t;
        Solve();
    }
    return 0;
}
