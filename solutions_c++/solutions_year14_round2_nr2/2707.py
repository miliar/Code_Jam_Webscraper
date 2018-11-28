#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>

#define MAXA 1005
#define MAXB 1005
#define MAXK 1005

int main(void)
{
    int i, j;
    int T, Case, result;
    int A, B, K;
    
    FILE *fp1,*fp2;
    if((fp1=fopen("B-small-attempt0.in","r"))==NULL)exit(0);
    if((fp2=fopen("B-small-attempt0.out","w"))==NULL)exit(0);
    
    fscanf(fp1,"%d", &T);
    
    Case = 1;
    while(Case <= T)
    {
        fscanf(fp1,"%d %d %d", &A, &B, &K);
        result = 0;
        for(i = 0; i < A; i++)
        {
            for(j = 0; j < B; j++)
            {
                if((i & j) < K)
                {
                     result++;
                }
            }
        }
        fprintf(fp2,"Case #%d: %d\n", Case, result);
        Case++;
    }
}
