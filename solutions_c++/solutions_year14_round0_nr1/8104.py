#include<iostream>
#include<stdio.h>
using namespace std;
int main()
{
    int a[4][4],b[4][4],m,n;
    int t;
    scanf("%d",&t);
    for(int y=1;y<=t;y++)
        {
            int k=0,h;
     scanf("%d",&m);
    for(int i=0;i<4;i++)
        for(int j=0;j<4;j++)
    {
        scanf("%d",&a[i][j]);
    }
     scanf("%d",&n);
    for(int i=0;i<4;i++)
        for(int j=0;j<4;j++)
    {
        scanf("%d",&b[i][j]);
    }
    for(int i=0;i<4;i++)
        for(int j=0;j<4;j++)
    {
        if(a[m-1][i]==b[n-1][j])
        {
            h=a[m-1][i];
            k++;
        }
    }

    if(k==1)
    {
        printf("Case #%d: %d\n",y,h);
    }
    if(k>1)
    {
        printf("Case #%d: Bad magician!\n",y);

    }
    if(k==0)
    {
        printf("Case #%d: Volunteer cheated!\n",y);
    }

    }
}
