#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<ctype.h>
#include<conio.h>
int main()
{
    FILE *fr, *fw;
    fr=fopen("B-small-attempt0.in","r");
    fw=fopen("bout.txt","w");
    long int t, a, b, k, i, j, l, c, d;
    fscanf(fr,"%ld",&t);
    for(i=0;i<t;i++)
    {
        c=0;
        fscanf(fr,"%ld%ld%ld",&a,&b,&k);
        for(j=0;j<a;j++)
        {
            for(l=0;l<b;l++)
            {
                d=j&l;
                if(d<k)
                    c++;
            }
        }
        fprintf(fw,"Case #%ld: %ld",i+1,c);
        if(i!=t-1)
            fprintf(fw,"\n");
    }
    fclose(fr);
    fclose(fw);
    return 0;
}
