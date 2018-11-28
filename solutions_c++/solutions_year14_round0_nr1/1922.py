#include<stdio.h>
using namespace std;

int main()
{
    FILE *fp,*fp1;
    fp = fopen("A-small-attempt0.in","r");
    fp1 = fopen("file3.txt","w");
    int a[5][5],b[5][5];
    bool ab[17],bc[17];
    int t,first,second,i,j,k;
    fscanf(fp,"%d",&t);
    for(k=1;k<=t;k++)
    {
        fscanf(fp,"%d",&first);
        for(i=1;i<=16;i++)
        {
            ab[i]=0;
            bc[i]=0;
        }
        for(i=1;i<=4;i++)
        {
            for(j=1;j<=4;j++)
            {
                fscanf(fp,"%d",&a[i][j]);
            }
        }
        fscanf(fp,"%d",&second);
        for(i=1;i<=4;i++)
        {
            for(j=1;j<=4;j++)
            {
                fscanf(fp,"%d",&b[i][j]);
            }
        }
        for(i=1;i<=4;i++)
        {
            ab[a[first][i]]=1;
            bc[b[second][i]]=1;
        }
        int ans=0,val=0;
        for(i=1;i<=16;i++)
        {
            if(ab[i]==1 && bc[i]==1)
            {
                ans++;
                val=i;
            }
        }
        if(ans==1)
        {
            fprintf(fp1,"Case #%d: %d\n",k,val);
        }
        else if(ans>1)
        {
            fprintf(fp1,"Case #%d: Bad magician!\n",k);
        }
        else
            fprintf(fp1,"Case #%d: Volunteer cheated!\n",k);


    }
    return 0;
}
