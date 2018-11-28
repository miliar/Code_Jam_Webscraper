/**

	author:zhongao@zhongao.HP
	date:2013.03.23
	function:
*/
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <algorithm>
#include <set>
#include <vector>
#include <iostream>
#include <sstream>
#include <queue>
#include <stack>
#include <list>
using namespace std;

#define FOR2(i,a,b) for(int i = (a);i < (b);i++)
#define FOR(i,n) for(int i = 0;i < n;i++)
#define S(n) scanf("%d",&(n))
char map[5][5];
int fc,fo,fx;
void judge()
{
    for(int i = 0;i < 4;i++)
    {
        int o = 0,x = 0,t = 0;
        for(int j = 0;j < 4;j++)
        {
            if(map[i][j]=='O') o++;
            else if(map[i][j]=='T') t++;
            else if(map[i][j]=='X') x++;
            else fc = 0;
        }
        if((o+t)==4) fo = 1;
        if((x+t)==4) fx = 1;
    }
}
int main()
{
    int cas = 0,n;
    S(n);
    while(n--)
    {
        cas ++;
        fc = 1,fo = 0,fx = 0;
        getchar();
        for(int i = 0;i < 4;i++)
        {
            scanf("%s",map[i]);
            getchar();
        }
        printf("Case #%d: ",cas);
        judge();
        for(int i = 0;i < 4;i++)
        {
            int o = 0,x = 0,t = 0;
            for(int j = 0;j < 4;j++)
            {
                if(map[j][i]=='O') o++;
                else if(map[j][i]=='T') t++;
                else if(map[j][i]=='X') x++;
                else fc = 0;
            }
            if((o+t)==4) fo = 1;
            if((x+t)==4) fx = 1;
        }
        int o = 0,x = 0,t = 0;
        for(int i = 0;i < 4;i++)
        {
            if(map[i][i]=='O') o++;
            else if(map[i][i]=='T') t++;
            else if(map[i][i]=='X') x++;
            else fc = 0;
        }
        if((o+t)==4) fo = 1;
        if((x+t)==4) fx = 1;
        o = 0,x = 0,t = 0;
        for(int i = 0;i < 4;i++)
        {
            if(map[i][3-i]=='O') o++;
            else if(map[i][3-i]=='T') t++;
            else if(map[i][3-i]=='X') x++;
            else fc = 0;
        }
        if((o+t)==4) fo = 1;
        if((x+t)==4) fx = 1;
        if(fo) printf("O won\n");
        if(fx) printf("X won\n");
        if(fc==0)
        {
            if(!fo&&!fx) printf("Game has not completed\n");

        }
        else
        {
            if(!fo&&!fx) printf("Draw\n");
        }
    }
    return 0;
}
