#include<stdio.h>
int main()
{
    FILE * fr, *fw;
    fr=fopen("A-small-attempt0.in","r");
    fw=fopen("oup.txt","w");
    int t;
    fscanf(fr,"%d",&t);
    int a,b,ar1[4][4],ar2[4][4],i,j,k, sum=0, var;
    for(k=0;k<t;k++)
    {
        sum=0;
        fscanf(fr,"%d",&a);
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
                fscanf(fr,"%d",&ar1[i][j]);
        }
        fscanf(fr,"%d",&b);
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
                fscanf(fr,"%d",&ar2[i][j]);
        }
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                if(ar1[a-1][i]==ar2[b-1][j]){
                    sum=sum+1;
                    var=ar1[a-1][i];
                }
            }
        }
        fprintf(fw,"Case #%d: ",k+1);
        if(sum==0)
            fprintf(fw,"Volunteer cheated!");
        else if(sum>1)
            fprintf(fw,"Bad magician!");
        else
            fprintf(fw,"%d",var);
        if(k!=t-1)
            fprintf(fw,"\n");
    }
    fclose(fr);
    fclose(fw);
}
