#include <iostream>
#include <string.h>
#include <stdlib.h>
#include <stdio.h>
#include<algorithm>
using namespace std;
#define maxn 105
char map[maxn][maxn];
int dis[4][2]={0,1,0,-1,1,0,-1,0};
char z[5]="><v^";
int main()
{
    freopen("/Users/ZZ/Desktop/in.txt","r",stdin);
    freopen("/Users/ZZ/Desktop/out.txt","w",stdout);
    int t;
    int n,m;
    int cas=1;
    scanf("%d",&t);
    while (t--) {
        scanf("%d%d",&n,&m);
        for(int i=0;i<n;i++) scanf("%s",map[i]);
        int ans=0,sign=1;
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<m;j++)
            {
                if(map[i][j]=='.') continue;
                int nnum=0;
                for(int k=0;k<4;k++)
                {
                    int num=0;
                    int nx=i+dis[k][0],ny=j+dis[k][1];
                    while(nx>=0&&nx<n&&ny>=0&&ny<m)
                    {
                        if(map[nx][ny]!='.')
                        {
                            nnum++;
                            num++;
                            break;
                        }
                        nx=nx+dis[k][0],ny=ny+dis[k][1];
                    }
                    if(map[i][j]==z[k]&&num==0) ans++;
                }
                if(nnum==0) sign=0;
            }
        }
        printf("Case #%d: ",cas++);
        if(!sign)
        {
            puts("IMPOSSIBLE");
        }
        else printf("%d\n",ans);
        
    }
}