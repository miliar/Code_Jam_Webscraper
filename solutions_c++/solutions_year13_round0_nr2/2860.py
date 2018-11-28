#include <iostream>
#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;
struct Node
{
    int x;
    int y;
    int value;
    bool operator < (const Node &tmp)const
    {
        return value<tmp.value;
    }
}buf[101*101];
int data[101][101];
bool mark[101][101];
int T,N,M;
bool checkRow(int x,int y)
{
    bool flag=true;
    for(int i=0;i<M;i++)
    {
        if(data[x][i]>data[x][y]&&mark[x][i]==false)flag=false;

    }
    return flag;
}
bool checkCol(int x,int y)
{
    bool flag=true;
    for(int i=0;i<N;i++)
    {
        if(data[i][y]>data[x][y]&&mark[i][y]==false)flag=false;
    }
    return flag;
}
int main()
{
    freopen("A-small-practice.in", "r", stdin);
    freopen("A-small-practice.out", "w", stdout);
    //int min,minn,minm;
    while(scanf("%d",&T)!=EOF)
    {
        for(int i=1;i<=T;i++)
        {
            int cnt=0;
            memset(mark,false,sizeof(mark));
            scanf("%d%d",&N,&M);
            for(int n=0;n<N;n++)
                for(int m=0;m<M;m++)
                {scanf("%d",&data[n][m]);buf[cnt].value=data[n][m];buf[cnt].x=n;buf[cnt].y=m;cnt++;}
            bool flag=true;
            int total=N*M;
            sort(buf,buf+total);
            for(int j=0;j<total;j++)
            {
                int _x=buf[j].x;
                int _y=buf[j].y;
                int _v=buf[j].value;
                if(mark[_x][_y])continue;
                mark[_x][_y]=true;
                if(checkRow(_x,_y)||checkCol(_x,_y));
                else {flag=false;break;}
            }
            printf("Case #%d: ",i);
            if(flag)printf("YES\n");
            else printf("NO\n");

        }
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
