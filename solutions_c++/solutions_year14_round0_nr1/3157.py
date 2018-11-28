#include<algorithm>
#include<iostream>
#include<string.h>
#include<sstream>
#include<stdio.h>
#include<math.h>
#include<vector>
#include<string>
#include<queue>
#include<set>
#include<map>
//#pragma comment(linker,"/STACK:1024000000,1024000000")
using namespace std;
const int INF=0x3f3f3f3f;
const double eps=1e-8;
const double PI=acos(-1.0);
const int maxn=100010;
//typedef __int64 ll;
int maze[8][8],vis[30];
int main()
{
    int t,cas=1,i,j,row,cnt,p;
    freopen("A-small-attempt2.in","r",stdin);
    freopen("out.out","w",stdout);
    scanf("%d",&t);
    while(t--)
    {
        memset(vis,0,sizeof vis);
        cnt=0;
        scanf("%d",&row);
        for(i=1;i<=4;i++)
            for(j=1;j<=4;j++)
                scanf("%d",&maze[i][j]);
        for(i=1;i<=4;i++)
            vis[maze[row][i]]=1;
        scanf("%d",&row);
        for(i=1;i<=4;i++)
            for(j=1;j<=4;j++)
                scanf("%d",&maze[i][j]);
        for(i=1;i<=4;i++)
            if(vis[maze[row][i]])
                p=maze[row][i],cnt++;
        if(cnt==1)
            printf("Case #%d: %d\n",cas++,p);
        else if(cnt>1)
            printf("Case #%d: Bad magician!\n",cas++);
        else
            printf("Case #%d: Volunteer cheated!\n",cas++);
    }
    return 0;
}
