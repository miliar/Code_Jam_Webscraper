#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <queue>
using namespace std;
#define sqr(x) ((x)*(x))
#define LL long long
#define eps 1e-9
#define INF 0x7fffffff
#define pi acos(-1.0);
#define CLR(x,v) memset(x,v,sizeof(x));
#define FOR(i,a,b) for(int i=a;i<b;i++)
char mp[10][10];


int main(int argc,char* argv[])
{
    std::ios::sync_with_stdio(false);
    int T;
    scanf("%d",&T);
    FOR(k,1,T+1)
    {
        FOR(p,0,4)  scanf("%s",mp[p]);
        printf("Case #%d: ",k);
        int dotnum=0;
        int flag=-1;
        int j;
        FOR(i,0,4)
        {
            j=0;
            for(;j<=2;j++)
            {
                if(mp[i][j]=='.'||(mp[i][j]!=mp[i][j+1]&&mp[i][j]!='T'&&mp[i][j+1]!='T'))
                    break;
            }
            if(j == 3)
            {
                for(int o=0;o<=3;o++)
                    if(mp[i][o]!='T')
                    {
                        if(mp[i][o]=='X')   flag=1;
                        else    flag=0;
                    }
            }
            if(flag !=-1)   break;
            j=0;
            for(;j<=2;j++)
                if(mp[i][j]=='.'||(mp[j][i]!=mp[j+1][i]&&mp[j][i]!='T'&&mp[j+1][i]!='T'))    
                    break;
            if(j == 3)
            {
                for(int o=0;o<=3;o++)
                {
                    if(mp[o][i]!='T')
                    {
                        if(mp[o][i]=='X')   flag=1;
                        else    flag=0;
                    }
                }
            }
            if(flag != -1)  break;
        }
        if(flag == -1)
        {
            int i;
            for(i=0;i<=2;i++)
                if(mp[i][i]=='.'||(mp[i][i]!=mp[i+1][i+1]&&mp[i][i]!='T'&&mp[i+1][i+1]!='T'))
                    break;
            if(i == 3)
            {
                for(int j=0;j<=3;j++)
                    if(mp[j][j]!='T')   
                    {
                        if(mp[j][j] == 'X') flag=1;
                        else    flag=0;
                        break;
                    }
            }
            for(i=0;i<=2;i++)
                if(mp[i][3-i]=='.'||(mp[i][3-i]!=mp[i+1][3-i-1]&&mp[i][3-i]!='T'&&mp[i+1][3-i-1]!='T'))
                    break;
            if(i == 3)
            {
                for(int j=0;j<=3;j++)
                    if(mp[j][3-j]!='T')   
                    {
                        if(mp[j][3-j] == 'X') flag=1;
                        else    flag=0;
                        break;
                    }
            }
        }
        if(flag == -1)
        {
            FOR(i,0,4)
            {
                FOR(j,0,4)
                {
                    if(mp[i][j] == '.') dotnum++;
                }
            }
            if(dotnum == 0)
                printf("Draw\n");
            else
                printf("Game has not completed\n");
        }
        else  if(flag==1)
            printf("X won\n");
        else
            printf("O won\n");
    }
    return 0;
}
