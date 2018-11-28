#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cctype>
#include <cstdlib>
#include <fstream>
#include <vector>
#include <string>
#include <sstream>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <list>
#include <bitset>
#include <numeric>
#include <algorithm>
#include <functional>
using namespace std;

const inline int __GET_INT(){int ret;scanf("%d",&ret);return ret;}
#define INPT_INT __GET_INT()

typedef long long LL;

int R, C;
char grid[102][102];
string a = "><^v";
const int inf = (1<<30);

bool isArrow(char c)
{
    return (c == '>' || c == '<' || c == '^' || c == 'v');
}

pair<int,int> getxy(char c)
{
    int dx = 0, dy = 0;

    if(c == '>') dy = 1;
    else if(c == '<') dy = -1;
    else if(c == '^') dx = -1;
    else if(c == 'v') dx = 1;

    return make_pair(dx,dy);
}

bool isGood(int i, int j)
{
    pair<int,int> cur = getxy(grid[i][j]);

    bool good = true;
    int x = i, y = j;

    for(int k = 0; k < 101; ++k)
    {
        x += cur.first;
        y += cur.second;

        if(x < 0 || x >= R || y < 0 || y >= C)
        {
            good = false; break;
        }

        if(isArrow(grid[x][y])) break;
    }
    return good;
}

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);

    int total_test = INPT_INT;

    for(int cur_test = 1; cur_test <= total_test; ++cur_test)
    {
        R = INPT_INT; C = INPT_INT;

        for(int i = 0; i < R; ++i)
        {
            scanf("%s",grid[i]);
        }

        int res = 0;
        for(int i = 0; i < R && res != inf; ++i) for(int j = 0; j < C; ++j) if(isArrow(grid[i][j]))
        {
            if(!isGood(i,j))
            {
                char tmp = grid[i][j];
                bool good = false;

                for(int l = 0; l < 4; ++l)
                {
                    grid[i][j] = a[l];
                    good = isGood(i,j);
                    if(good) break;
                }
                grid[i][j] = tmp;

                if(good) ++res;
                else {res = inf; break;}
            }
        }

        printf("Case #%d: ",cur_test);
        if(res == inf) puts("IMPOSSIBLE");
        else printf("%d\n",res);
    }
	return 0;
}
