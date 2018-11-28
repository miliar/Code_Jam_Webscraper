#include <iostream>
#include<stdio.h>

using namespace std;

int main()
{
    int t=0,i=0,j=0,ans1=0,ans2=0,x=0,y;
    int a[4][4],d[4][4];
    int b[4],c[4];
    freopen( "A-small-attempt0.in", "r", stdin );
    scanf("%d",&t);
    y = t;
    int *s = new int[t];
    int *cnt = new int[t];
    do
    {
        cnt[x] = 0;
        scanf("%d",&ans1);
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                scanf("%d",&a[i][j]);
            }
        }
    for(i=0;i<4;i++)
    {
        b[i]=a[ans1-1][i];
    }
    scanf("%d",&ans2);
    for(i=0;i<4;i++)
    {
        for(j=0;j<4;j++)
        {
            scanf("%d",&a[i][j]);
        }
    }
    for(i=0;i<4;i++)
    {
        c[i]=a[ans2-1][i];
    }
    for(i=0;i<4;i++)
    {
        for(j=0;j<4;j++)
        {
            if(b[i]==c[j])
            {
                cnt[x]++;
                s[x]=b[i];
            }
        }
    }

    x++;
    t--;
    }while(t!=0);
    freopen ("myfile.txt","w",stdout);
    for(i =0;i<y;i++)
    {
        if(cnt[i]==1)
            printf("\nCase #%d: %d",i+1,s[i]);
        else if(cnt[i]>1)
            printf("\nCase #%d: Bad magician!",i+1);
        else
            printf("\nCase #%d: Volunteer cheated!",i+1);
    }
    delete []s;
    delete []cnt;
    return 0;
}
