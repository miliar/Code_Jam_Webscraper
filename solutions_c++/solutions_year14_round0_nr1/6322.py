# include <stdio.h>
main()
{

    FILE *IN=fopen("a.in","r");
    FILE *OUT=fopen("Output.txt","w");
    int t,k,a,b,x[4][4],y[4][4],i,j,ans[4];
    fscanf(IN,"%d",&t);
    for(k=1;k<=t;k++)
    {

        fscanf(IN,"%d",&a);
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                fscanf(IN,"%d",&x[i][j]);
            }
        }
        fscanf(IN,"%d",&b);
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                fscanf(IN,"%d",&y[i][j]);
            }
        }
        a--;b--;int z=0;
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                if(x[a][i]==y[b][j]){ans[z++]=x[a][i];y[b][j]=-1;}
            }
        }
        fprintf(OUT,"Case #%d: ",k);
        if(z==1)fprintf(OUT,"%d\n",ans[0]);
        else if(z==0)fprintf(OUT,"Volunteer cheated!\n");
        else fprintf(OUT,"Bad magician!\n");
    }
}
