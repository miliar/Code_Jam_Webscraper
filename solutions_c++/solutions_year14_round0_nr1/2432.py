#include<stdio.h>
#include<iostream>
using namespace std;
int a[5][5],b[5][5];
int x,y;
int main()
{
   // freopen("out.txt","w",stdout);
    int t,i,j;
    scanf("%d",&t);
    int cas=1;
    while(t--)
    {
        scanf("%d",&x);
        for(i=1;i<=4;i++)
        {
            for(j=1;j<=4;j++)
            {
                scanf("%d",&a[i][j]);
            }
        }
        scanf("%d",&y);
        for(i=1;i<=4;i++)
        {
            for(j=1;j<=4;j++)
            {
                scanf("%d",&b[i][j]);
            }
        }
        int ans,num=0;
        for(i=1;i<=4;i++)
        {
            for(j=1;j<=4;j++)
            {
                if(a[x][i]==b[y][j])
                {
                    num++;
                    ans=a[x][i];
                }
            }
        }
        printf("Case #%d: ",cas++);
        if(num==0)
        {
            puts("Volunteer cheated!");
        }
        else if(num>1)
        {
            puts("Bad magician!");
        }
        else
        {
            printf("%d\n",ans);
        }
    }
    return 0;
}
