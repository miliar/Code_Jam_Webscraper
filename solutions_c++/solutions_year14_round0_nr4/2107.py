#include<stdio.h>

int main()
{
    int T,i;
    int blok,j,k,kondisi,hasil;
    int na,ke;
    double naomi[1000],ken[1000],temp;
    
    scanf("%i",&T);
    for(i=1;i<=T;i++)
    {
        na=0,ke=0,hasil=0;
        kondisi=1;             
        printf("Case #%i: ",i);
        scanf("%i",&blok);
        for(j=0;j<blok;j++) scanf("%lf",&naomi[j]);
        for(j=0;j<blok;j++) scanf("%lf",&ken[j]);
        for(j=0;j<blok;j++) {for(k=0;k<blok;k++)
        {
            if(naomi[j]<naomi[k])
            {
                temp=naomi[j];
                naomi[j]=naomi[k];
                naomi[k]=temp;
            }
        }}
        for(j=0;j<blok;j++) {for(k=0;k<blok;k++)
        {
            if(ken[j]<ken[k])
            {
                temp=ken[j];
                ken[j]=ken[k];
                ken[k]=temp;
            }
        }}
        /*
        //tes
        printf("\n");
        for(j=0;j<blok;j++) printf("%lf ",naomi[j]);
        printf("\n");
        for(j=0;j<blok;j++) printf("%lf ",ken[j]);
        printf("\n");
        */
        while(kondisi)
        {
             if(ken[ke]>naomi[na])
             {
                  na+=1;
             }
             else if(ken[ke]<naomi[na])
             {
                  ke+=1;
                  na+=1;
                  hasil+=1;
             }
             if(na==blok || ke==blok)
             {
                 kondisi=0;
                 printf("%i ",hasil);
             }
        }
        kondisi=1;
        hasil=blok;
        na=0,ke=0;
        while(kondisi)
        {
             if(naomi[na]>ken[ke])
             {
                  ke+=1;
             }
             else if(naomi[na]<ken[ke])
             {
                  na+=1;
                  ke+=1;
                  hasil-=1;
             }
             if(na==blok || ke==blok)
             {
                 kondisi=0;
                 printf("%i\n",hasil);
             }
        }
        
    }
}
