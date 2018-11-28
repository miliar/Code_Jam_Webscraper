#include<cstdio>
#include<cstring>
#include<cmath>
#include<cstdlib>
#include<cctype>
#include<algorithm>
#include<string>
#include<vector>
#include<queue>
#include<map>
#include<set>
#include<sstream>
#include<stack>
#include<list>
#include<assert.h>
#define f_input freopen("a.txt","r",stdin)
#define mem(x,y) memset(x,y,sizeof(x))
#include<iostream>
#define pb push_back
#define eps 1e-4
#define pp pair<int,int>
using namespace std;
typedef vector<int>vint;
typedef vector<long long int>vlong;
typedef vector<string>vstr;
typedef queue<int>Qint;
typedef map<int,int>Mii;
typedef map<string,int>Msi;
typedef map<int,string>Mis;
typedef long long int llint;
typedef stack<int>stk;
const int inf=0x7FFFFFFF;
char grid[10][10];
void print()
{
    for(int i=0;i<4;i++)
    {
        printf("%s\n",grid[i]);
    }
    printf("\n");
}
string solve()
{
    int x1,y1,x2,y2,incomplete=0;
    int i,j;
    for(i=0;i<4;i++)
    {
        x1=y1=x2=y2=0;
        for(j=0;j<4;j++)
        {
            if(grid[i][j]=='.')
            {
                incomplete++;
            }
            if(grid[i][j]=='T')
            {
                x1++;
                y1++;
            }
            else if(grid[i][j]=='X')
            {
                x1++;
            }
            else if(grid[i][j]=='O')
            {
                y1++;
            }
            if(grid[j][i]=='T')
            {
                x2++;
                y2++;
            }
            else if(grid[j][i]=='X')
            {
                x2++;
            }
            else if(grid[j][i]=='O')
            {
                y2++;
            }
        }
        if(x1==4||x2==4)
        {
            return "X won";
        }
        else if(y1==4||y2==4)
        {
            return "O won";
        }
    }
    x1=y1=x2=y2=0;
    for(i=0,j=3;i<4;i++,j--)
    {
        if(grid[i][i]=='X')x1++;
        else if(grid[i][i]=='O')y1++;
        else if(grid[i][i]=='T')
        {
            x1++;
            y1++;
        }
        if(grid[i][j]=='X')x2++;
        else if(grid[i][j]=='O')y2++;
        else if(grid[i][j]=='T')
        {
            x2++;
            y2++;
        }
    }
    if(x1==4||x2==4)
        {
            return "X won";
        }
        else if(y1==4||y2==4)
        {
            return "O won";
        }
    if(incomplete)
    {
        return "Game has not completed";
    }
    else
    {
        return "Draw";
    }
}
int main()
{
    f_input;
    freopen("output.txt","w",stdout);
    int test,t;
    scanf("%d",&test);
    for(t=1;t<=test;t++)
    {
        int i,j;
        for(i=0;i<4;i++)
        {
            scanf("%s",grid[i]);
        }
        string ans=solve();
        //print();
        printf("Case #%d: %s\n",t,ans.c_str());
    }
    return 0;
}
