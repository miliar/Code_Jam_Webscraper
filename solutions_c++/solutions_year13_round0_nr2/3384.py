#include"stdio.h"
int a[120][120];
int n,m;
int vert(int x,int y)
{
    for(int i=0;i<m;i++)
        if(a[i][y]>a[x][y])
        return 0;
    return 1;
}
int hori(int x,int y)
{
    for(int j=0;j<n;j++)
        if(a[x][y]<a[x][j])
        return 0;
    return 1;
}
main()
{
    FILE * p1, * p2;
    int cas;
    int yes;
    p1=fopen("B-large.in","r");
    p2=fopen("largeee.in","w");

    fscanf(p1,"%d",&cas);
    for(int k=1;k<=cas;k++)
    {
        yes=1;
        fscanf(p1,"%d %d",&m,&n);

        for(int i=0;i<m;i++)
            for(int j=0;j<n;j++)
                fscanf(p1,"%d",&a[i][j]);

        for(int i=0;i<m;i++)
            for(int j=0;j<n;j++)
         {
             if(vert(i,j)==0&&hori(i,j)==0)
                yes=0;
         }

         if(yes==0)
            fprintf(p2,"Case #%d: NO\n",k);
        else
            fprintf(p2,"Case #%d: YES\n",k);
    }
}
