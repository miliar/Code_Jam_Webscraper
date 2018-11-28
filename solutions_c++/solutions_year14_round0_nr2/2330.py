#include<stdio.h>

int main()
{
    double sum,banding1,banding2,pnjumlah;
    int T,i,kondisi;
    double C,F,X;
    
    scanf("%i",&T);
    for(i=1;i<=T;i++)
    {
        pnjumlah=2;
        scanf("%lf",&C);
        scanf("%lf",&F);
        scanf("%lf",&X);
        printf("Case #%i: ",i);
        
        banding1=X/pnjumlah;
        banding2=C/pnjumlah + X/(pnjumlah+F);
        if(banding1<banding2)
        {
            printf("%.7lf\n",banding1);
        }
        else
        {
            kondisi=1;
            while(kondisi)
            {
               pnjumlah+=F;
               sum=banding2;
               banding2=banding2-X/pnjumlah+C/pnjumlah+X/(pnjumlah+F);
               if(sum<banding2)
               {
                    printf("%.7lf\n",sum);
                    kondisi=0;
               }
            }
        }
        
    }
}
