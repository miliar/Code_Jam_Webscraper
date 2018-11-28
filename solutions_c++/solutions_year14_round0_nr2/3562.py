#include<stdio.h>
#include<math.h>
#include<string.h>
#include<stdlib.h>

int main(void)
{
    int T, Case, i, j;
    double C, F, X, res;
    double now_rate, remain_X;
    
    FILE *fp1,*fp2;
    if((fp1=fopen("B-large.in","r"))==NULL)exit(0);
    if((fp2=fopen("B-large.out","w"))==NULL)exit(0);
    
    fscanf(fp1,"%d", &T);
    Case = 1;
    while(Case <= T)
    {
        fscanf(fp1,"%lf %lf %lf", &C, &F, &X);
        
        if (C > X)
        {
              fprintf(fp2,"Case #%d: %.7lf\n", Case, X / 2);
              Case++;
              continue;
        }
        
        res = 0;
        now_rate = 2;
        //remain_X = X;
        res = C / now_rate;
        while((X - C) / now_rate >  X / (now_rate + F))
        {
            now_rate = now_rate + F;
            res += C / now_rate;
        }
        res += (X - C) / now_rate;
        //fprintf(fp2,"Case #%d: %d\n", Case, card);
        fprintf(fp2,"Case #%d: %.7lf\n", Case, res);
        Case++;
    }    
    return 0;
}
