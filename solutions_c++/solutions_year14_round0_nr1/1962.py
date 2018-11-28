#include <iostream>
#include <cstdio>
#include<cstring>
using namespace std;
int map[20][20];
int cmap[20][20];
int vis[100];
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int T,n,m;
    scanf("%d",&T);
    int cn  = 0;
    while(T--)
    {
        cin>>n;
        memset(vis,0,sizeof(vis));
        for(int i=1;i<=4;i++)
        for(int j=1;j<=4;j++)
        cin>>map[i][j];
        for(int i=1;i<=4;i++){
        vis[map[n][i]] = 1;
        }
        cin>>m;
        int sum = 0,t;
        for(int i=1;i<=4;i++)
        for(int j=1;j<=4;j++)
        cin>>cmap[i][j];
        for(int j = 1;j<=4;j++)
        if(vis[cmap[m][j]] == 1){
        sum++;
        t = cmap[m][j];
        }
        if(sum == 1)
        {
            printf("Case #%d: %d\n",++cn,t);
        }

        if(sum>1)
        {
            printf("Case #%d: Bad magician!\n",++cn);
        }
        if(sum == 0)
        printf("Case #%d: Volunteer cheated!\n",++cn);
    }
    return 0;
}
