#include<stdio.h>
#include<iostream>
#include<vector>
#include<cmath>
using namespace std;
int a[5][5],b[5][5];
main()
{

    int i,j,k,n,m,count1=0,r1,r2,t,ans;
    FILE *fin  = fopen ("input.in", "r");
    FILE *fout = fopen ("output.txt", "w");
    fscanf(fin,"%d",&t);
    for(k=1;k<=t;k++)
    {
        count1=0;
        fscanf(fin,"%d",&r1);
        for(i=0;i<4;i++)
        for(j=0;j<4;j++)
        fscanf(fin,"%d",&a[i][j]);
        fscanf(fin,"%d",&r2);
        for(i=0;i<4;i++)
        for(j=0;j<4;j++)
        fscanf(fin,"%d",&b[i][j]);
        r1--;
        r2--;
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                if(a[r1][i]==b[r2][j])
                {
                    count1++;
                    ans=a[r1][i];
                }
            }
        }
        if(count1==1)
        fprintf(fout,"Case #%d: %d\n",k,ans);
        else if(count1>1)
        fprintf(fout,"Case #%d: Bad magician!\n",k);
        else
        fprintf(fout,"Case #%d: Volunteer cheated!\n",k);

    }
    return 0;
}
