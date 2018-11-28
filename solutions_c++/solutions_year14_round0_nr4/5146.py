#include <stdio.h>
#include <stdlib.h>

int main()
{
    FILE *inp, *outp;
    int t, i, j, k, n, p, sw, sw2, decepwar, war;
    float *naomi, *ken, *naomi2, *ken2;
    float temp;
    inp=fopen("D-small-attempt3.in","r");
    outp=fopen("output.txt","w");
    fscanf(inp,"%d",&t);
    for(j=1;j<=t;j++)
    {
        decepwar=0;
        war=0;
        fscanf(inp,"%d",&n);
        naomi=new float [n];
        ken=new float [n];
        naomi2= new float [n];
        ken2=new float [n];
        for(i=0;i<n;i++)
        {
            fscanf(inp,"%f",&naomi[i]);
            //fprintf(outp,"%f ",naomi[i]); //debug
        }
        //fprintf(outp,"\n");
        for(i=0;i<n;i++)
        {
            fscanf(inp,"%f",&ken[i]);
            //fprintf(outp,"%f ",ken[i]); //debug
        }
        //fprintf(outp,"\n");
        sw=0;
        while(sw==0)
        {
            sw=1;
            i=0;
            while(i<(n-1))
            {
                if(naomi[i+1]<naomi[i])
                {
                    temp=naomi[i+1];
                    naomi[i+1]=naomi[i];
                    naomi[i]=temp;
                    sw=0;
                }
                i++;
            }
        }
        sw=0;
        while(sw==0)
        {
            sw=1;
            i=0;
            while(i<(n-1))
            {
                if(ken[i+1]<ken[i])
                {
                    temp=ken[i+1];
                    ken[i+1]=ken[i];
                    ken[i]=temp;
                    sw=0;
                }
                i++;
            }
        }
        //debug
        for(i=0;i<n;i++)
        {
            //fprintf(outp,"%.3f ",naomi[i]);
            naomi2[i]=naomi[i];
        }
        //fprintf(outp,"\n");
        for(i=0;i<n;i++)
        {
            //fprintf(outp,"%.3f ",ken[i]);
            ken2[i]=ken[i];
        }
        //fprintf(outp,"\n");
        if(n==1)
        {
            if(naomi[0]>ken[0])
            {
                decepwar++;
                war++;
            }
        }
        else
        {
            for(i=0;i<n;i++)
            {
                for(k=0;k<n;k++)
                {
                    if(naomi[i]>ken[k]&&ken[k]!=0)
                    {
                        naomi[i]=0;
                        ken[k]=0;
                        decepwar++;
                    }
                    if(naomi[i]<ken[k]&&naomi[i]!=0)
                    {
                        naomi[i]=0;
                        sw2=0;
                        p=n-1;
                        while(sw2==0&&p>=0)
                        {
                            if(ken[p]!=0)
                            {
                                ken[p]=0;
                                sw2=1;
                            }
                            p--;
                        }
                    }
                }
            }
            for(i=0;i<n;i++)
            {
                k=0;
                while(ken2[k]<naomi2[i]&&k<n)
                {
                k++;
                }
                if(ken2[k]>naomi2[i]&&naomi2[i]!=0)
                {
                    ken2[k]=0;
                    naomi2[i]=0;
                }
            }
            for(i=0;i<n;i++)
            {
                if(naomi2[i]!=0)
                    war++;
            }
        }
        fprintf(outp,"Case #%d: %d %d\n",j,decepwar,war);
        //debug
        delete naomi;
        delete ken;
        delete naomi2;
        delete ken2;
    }
    fclose(inp);
    fclose(outp);
    return 0;
}
