#include<stdio.h>
int main()
{
    int t;
    scanf("%d",&t);
    int x=0;
    while(t--)
    {
        x++;
        int i,j,n,a[4][4],b[17]={0};
        scanf("%d",&n);
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                scanf("%d",&a[i][j]);
                if(i==n-1)b[a[i][j]]++;
            }
        }
        scanf("%d",&n);
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                scanf("%d",&a[i][j]);
                if(i==n-1)b[a[i][j]]++;
            }
        }
        int c=0,c2;
        for(i=0;i<17;i++)
            {
                if(b[i]==2){c++;c2=i;}
            }
        if(c==0)
            printf("Case #%d: Volunteer cheated!\n",x);
        if(c==1)
            printf("Case #%d: %d\n",x,c2);
        if(c>1)
            printf("Case #%d: Bad magician!\n",x);
    }
    return 0;
}
