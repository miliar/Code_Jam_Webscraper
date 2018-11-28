#include<iostream>
#include<cstdio>

using namespace std;

int main()
{
    int l,t;
    scanf("%d",&t);
    for(l=1;l<=t;l++)
    {
        int a[4][4],b[4],c[4],i,j,r;
        scanf("%d",&r);
        for(i=0;i<4;i++)
            for(j=0;j<4;j++)
                scanf("%d",&a[i][j]);
        for(j=0;j<4;j++)
            b[j]=a[r-1][j];
        scanf("%d",&r);
        for(i=0;i<4;i++)
            for(j=0;j<4;j++)
                scanf("%d",&a[i][j]);
        for(j=0;j<4;j++)
            c[j]=a[r-1][j];
        int C=0,n;
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                if(b[i]==c[j])
                {
                    n=b[i];
                    C++;
                }
            }
        }
        printf("Case #%d: ",l);
        if(C==0)
            printf("Volunteer cheated!\n");
        else if(C==1)
            printf("%d\n",n);
        else
            printf("Bad magician!\n");
    }

    return 0;
}
