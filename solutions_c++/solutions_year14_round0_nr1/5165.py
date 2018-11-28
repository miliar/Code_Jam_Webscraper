#include <iostream>
#include<stdio.h>
using namespace std;
int main()
{
    int t;
    scanf("%d",&t);
    for(int w=1;w<=t;w++)
    {
        int a[4][4],b[4][4],n,c=0,d;
        scanf("%d",&n);
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            {
                scanf("%d",&a[i][j]);
            }
        }
        int m;
        scanf("%d",&m);
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            {
                scanf("%d",&b[i][j]);
            }
        }
            for(int i=0;i<4;i++)
            {
            for(int j=0;j<4;j++)
            {
                if(a[n-1][i]==b[m-1][j])
                {
                  c++; d=a[n-1][i];
                }
            }
            }
            if(c==1)
                printf("Case #%d: %d\n",w,d);
            else if(c==0)
                printf("Case #%d: Volunteer cheated!",w);
            else
                printf("Case #%d: Bad magician!\n",w);
    }
    return 0;
}
