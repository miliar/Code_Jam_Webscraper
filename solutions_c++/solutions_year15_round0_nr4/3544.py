#include<stdio.h>
#include<string.h>
using namespace std;
int a[10][10][10];
void cal()
{
    int i,j;
    for(i=1;i<=4;i++)
    {
        for(j=1;j<=4;j++)
        {
            a[i][j][1]=1;
            if(i%2==1&&j%2==1)a[i][j][2]=0;
            else a[i][j][2]=1;
            if(i%3==0||j%3==0)
            {
                if(i>1&&j>1)a[i][j][3]=1;
            }
            if(i%4==0||j%4==0)
            {
                if(i>2&&j>2)a[i][j][4]=1;
            }
        }
    }
}
int main()
{
//    freopen("D-small-attempt2.in","r",stdin);
//    freopen("D-small-attempt2.out","w",stdout);
//    freopen("in.txt","r",stdin);
    memset(a,0,sizeof(a));
    cal();
    int i,j,k,l,t,c,r,x;
    scanf("%d",&t);
    for(i=1;i<=t;i++)
    {
        scanf("%d %d %d",&x,&r,&c);
        if(a[r][c][x]==1)printf("Case #%d: GABRIEL\n",i);
        else printf("Case #%d: RICHARD\n",i);
    }
    return 0;
}
