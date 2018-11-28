#include<stdio.h>
int main()
{
int t,i,j,k;
scanf("%d",&t);
for(k=0;k<t;k++)
{
    int c1=0,c2=0,c3=0,c4=0,n1,n2,d1=0,d2=0,d3=0,d4=0,x1=0,x2=0,x3=0,x4=0,a[4][4]={0},b[4][4]={0};
    scanf("%d",&n1);
    for(i=0;i<4;i++)
    {
        for(j=0;j<4;j++)
        {
            scanf("%d",&a[i][j]);
        }
    }
    c1=a[n1-1][0];
    c2=a[n1-1][1];
    c3=a[n1-1][2];
    c4=a[n1-1][3];


     scanf("%d",&n2);
    for(i=0;i<4;i++)
    {
        for(j=0;j<4;j++)
        {
            scanf("%d",&b[i][j]);
        }
    }
    for(i=0;i<4;i++)
    {
        if(b[n2-1][i]==c1 )
        {
            d1++;
            x1=b[n2-1][i];
        }
        if(b[n2-1][i]==c2)
        {
            d2++;
            x2=b[n2-1][i];
        }
        if(b[n2-1][i]==c3)
        {
            d3++;
            x3=b[n2-1][i];
        }
        if(b[n2-1][i]==c4)
        {
            d4++;
            x4=b[n2-1][i];
        }
    }
    if(d1+d2+d3+d4==1)
    {
        if(d1==1)
        printf("Case #%d: %d\n",k+1,x1);
        if(d2==1)
        printf("Case #%d: %d\n",k+1,x2);
        if(d3==1)
        printf("Case #%d: %d\n",k+1,x3);
        if(d4==1)
        printf("Case #%d: %d\n",k+1,x4);
    }
    else if(d1+d2+d3+d4>1)
    {
        printf("Case #%d: Bad magician!\n",k+1);
    }
    else
    {
        printf("Case #%d: Volunteer cheated!\n",k+1);
    }
}
return 0;
}
