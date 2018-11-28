#include<iostream>
#include<cstring>
#include<cstdio>
using namespace std;
int x,y;
void print(int x,int y)
{
    if(x>0)
    {
        for(int i=0;i<x;i++)
        {
            printf("W");
            printf("E");
        }
    }
    else if(x<0)
    {
        for(int i=0;i<-x;i++)
        {
            printf("E");
            printf("W");
        }
    }
    if(y>0)
    {
        for(int i=0;i<y;i++)
        {
            printf("S");
            printf("N");
        }

    }
    else if(y<0)
    {
        for(int i=0;i<-y;i++)
        {
            printf("N");
            printf("S");
        }
    }
}
int main()
{
    freopen("D:\\B-small-attempt0.in","r",stdin);
    freopen("D:\\out.txt","w",stdout);
    int t;
    scanf("%d",&t);
    for(int cas=1;t--;cas++)
    {
        scanf("%d%d",&x,&y);
        printf("Case #%d: ",cas);
        print(x,y);
        printf("\n");
    }
}
