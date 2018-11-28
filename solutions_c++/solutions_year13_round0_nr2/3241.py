#include<iostream>
#include<cstring>
#include<cstdio>
#include<algorithm>
using namespace std;
int map[110][110];
int T,m,n;
int fs(int x,int y)
{
    int i,j,xi=0,yi=0;
    for(i=x+1,j=y;i<=m;i++)
    {
        if(map[i][j]>map[x][y]){xi++;break;}
    }

    for(i=x,j=y+1;j<=n;j++)
    {
        if(map[i][j]>map[x][y]){yi++;break;}
    }
    for(i=x-1,j=y;i>=1;i--)
    {
        if(map[i][j]>map[x][y]){xi++;break;}
    }
    for(i=x,j=y-1;j>=1;j--)
    {
        if(map[i][j]>map[x][y]){yi++;break;}
    }
    if(xi>0&&yi>0)return 0;
    return 1;
}
int main()
{

	//freopen("in.txt","r",stdin);
//	freopen("out3.txt","w",stdout);
    int i,j,flag;
    cin>>T;
    int time=1;
    while(T--)
    {
        cin>>m>>n;
       // if(m==1||n==1){printf("Case #%d: YES\n",time++);continue;}
        flag=0;
        memset(map,0,sizeof(map));
        for(i=1;i<=m;i++)
        {
            for(j=1;j<=n;j++)
            {
                scanf("%d",&map[i][j]);
            }
        }
        for(i=1;i<=m;i++)
        {
            for(j=1;j<=n;j++)
            {
                if(fs(i,j)==0)
                {
                    printf("Case #%d: NO\n",time++);
                    flag=1;
                    break;
                }
            }
            if(flag)break;
        }
    if(flag==0)  {flag=1;printf("Case #%d: YES\n",time++);}
    }
	return 0;
}
