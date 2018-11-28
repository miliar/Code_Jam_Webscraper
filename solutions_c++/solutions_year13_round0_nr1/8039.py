#include<iostream>
#include<cstring>
#include<cstdio>
#include<cstdlib>
#include<utility>
#include<algorithm>
#include<vector>
#include<map>
#include<set>
#include<string>
#include<iomanip>
#include<queue>
#include<iterator>
using namespace std;

#define LL long long
#define MAXN 4

char grid[10][10];
char states[][100] =
{
    "X won",
    "O won",
    "Draw",
    "Game has not completed"
};
bool over()
{
    for(int i = 0; i < 4; ++i)
    {
        for(int j = 0; j < 4; ++j)
        {
            if(grid[i][j] == '.') return true;
        }
    }
    return false;
}
int check()
{
    int cntx = 0;
    int cnto = 0;
    bool T = false;
    //for each raw
    for(int i = 0; i < 4; ++i)
    {
        cntx = 0;
        cnto = 0;
        T = false;
        for(int j = 0; j < 4; ++j)
        {
            if(grid[i][j] == 'X') ++cntx;
            if(grid[i][j] == 'O') ++cnto;
            if(grid[i][j] == 'T') T = true;
        }
        if(cntx == 4 || (T && cntx == 3)) return  0;
        if(cnto == 4 || (T && cnto == 3)) return 1;
    }
    //for each col
    for(int i = 0; i < 4; ++i)
    {
        cntx = 0;
        cnto = 0;
        T = false;
        for(int j = 0; j < 4; ++j)
        {
            if(grid[j][i] == 'X') ++cntx;
            if(grid[j][i] == 'O') ++cnto;
            if(grid[j][i] == 'T') T = true;
        }
        if(cntx == 4 || (T && cntx == 3)) return  0;
        if(cnto == 4 || (T && cnto == 3)) return 1;
    }
    // for dig
    cntx = 0;
    cnto = 0;
    T = false;
    for(int i = 0, j = 0; i < 4; ++i, ++j)
    {
        if(grid[i][j] == 'X') ++cntx;
        if(grid[i][j] == 'O') ++cnto;
        if(grid[i][j] == 'T') T = true;
    }
    if(cntx == 4 || (T && cntx == 3)) return  0;
    if(cnto == 4 || (T && cnto == 3)) return 1;
    cntx = 0;
    cnto = 0;
    T = false;
    for(int i = 3, j = 0; i >= 0; --i, ++j)
    {
        if(grid[i][j] == 'X') ++cntx;
        if(grid[i][j] == 'O') ++cnto;
        if(grid[i][j] == 'T') T = true;
    }
    if(cntx == 4 || (T && cntx == 3)) return  0;
    if(cnto == 4 || (T && cnto == 3)) return 1;
    //for state 3, 4
    if(!over()) return 2;
    else return 3;

}
int main(int argv, char **args)
{
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for(int kase = 1; kase <= T; ++kase)
    {
        for(int i = 0; i < 4; ++i) scanf("%s", grid[i]);
        printf("Case #%d: %s\n", kase, states[check()]);
        getchar();
    }
    return 0;
}
