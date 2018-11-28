#include<stdio.h>
#include<string.h>
int main()
{
    int t;
    int a[5][5],b[5][5];
    int s,d;
    freopen("E:\\A-small-attempt3.in","r",stdin);
    freopen("E:\\A-small-attempt3.out","w",stdout);
    scanf("%d",&t);
    for(int l=1;l<=t;l++)
    {
        scanf("%d",&s);
        int i,j;
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                scanf("%d",&a[i][j]);
            }
        }
        scanf("%d",&d);
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                scanf("%d",&b[i][j]);
            }
        }
        int cout=0,sum;
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                if(a[s-1][i]==b[d-1][j])
                {
                    cout++;
                    sum=a[s-1][i];
                }
            }
        }
        if(cout==1)
        {
            printf("Case #%d: %d\n",l,sum);
        }
        else if(cout==0)
        {
            printf("Case #%d: Volunteer cheated!\n",l);
        }
        else
        printf("Case #%d: Bad magician!\n",l);
    }
    return 0;
}
