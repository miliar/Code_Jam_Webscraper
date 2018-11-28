/*************************************************************************
    > File Name: A.cpp
    > Author: ALex
    > Mail: zchao1995@gmail.com 
    > Created Time: 2015年05月30日 星期六 22时07分03秒
 ************************************************************************/

#include <functional>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <queue>
#include <stack>
#include <map>
#include <bitset>
#include <set>
#include <vector>

using namespace std;

const double pi = acos(-1.0);
const int inf = 0x3f3f3f3f;
const double eps = 1e-15;
typedef long long LL;
typedef pair <int, int> PLL;


char mat[120][120];
int n, m;

int check(int x, int y)
{
    return x >= 0 && x < n && y >= 0 && y < m;
}

int dir[8][2] = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}, {-1, 1}, {1, 1}, {1, -1}, {-1, -1}};

void solve( ) {
	int res = 0;
    bool has = 1;
    for(int i = 0; i < n && has; i++)
        for(int j = 0; j < m && has; j++)
            if(mat[i][j] != '.')
             {
                int dx = 0, dy = 0;
                if(mat[i][j] == '^') dx = -1, dy = 0;
                if(mat[i][j] == '<') dx = 0, dy = -1;
               	if(mat[i][j] == '>') dx = 0, dy = 1;
           		if(mat[i][j] == 'v') dx = 1, dy = 0;
                int di = i + dx, dj = j + dy;
                while(check(di, dj) && mat[di][dj] == '.')
                    di += dx, dj += dy;
                    if(!check(di, dj))
                    {
                        bool flag = 0;
                        for(int k = 0; k < 4; k++)
                        {
                            dx = dir[k][0], dy = dir[k][1];
                            di = i + dx, dj = j + dy;
                            while(check(di, dj) && mat[di][dj] == '.')
                            {
                                di += dx, dj += dy;
                            }
                            if(check(di, dj)) flag = 1;
                        }
                        if(flag) res++;
                        else has = 0;
                    }
        }
    if(has)
        printf("%d\n", res);
    else
        printf("IMPOSSIBLE\n");
}

int main()
{
    int t, icase = 1;
 //   freopen("A-large.in", "r", stdin);
   // freopen("a.out", "w", stdout);
    scanf("%d",&t);
    while (t--)
    {
        scanf("%d%d", &n, &m);
        for(int i = 0; i < n; i++)
            scanf("%s", mat[i]);
        printf("Case #%d: ", icase++);
        solve();
    }
    return 0;
}

