#include <stdlib.h>
#include <stdio.h>
#include <math.h>

int a,b,k,kk,kkk,nb;
long int answer, locans, cop;
int t;
FILE *f, *g;

int min(int x, int y)
{
    if (x<y) return x;
    return y;
}
int main()
{
    f = fopen("Bin.txt","r");
    g = fopen("Bout.txt","w");

    fscanf(f,"%d",&t);

    for (int test=1;test<=t;test++)
    {
        fscanf(f,"%d%d%d\n",&a,&b,&k);

        answer = 0;

        for (int i=0;i<a;i++)
            for (int j=0;j<b;j++)
                if ((i & j) < k) answer++;
/*
        aa = floor(log2(a))+1;
        bb = floor(log2(b))+1;
        answer =0;

        for (kk=k-1;kk>=0;kk--)
        {
            kkk = floor(log2(k-1))+1;
            locans = floor(pow(3,min(a,b)-kkk));

            if (locans==1)

             printf("++%d-%d\n",test,locans);
            cop = kk;
            nb = floor(log2(k-1))+1;

            while (cop!=0) {
                if (cop%2 != 0) nb--;
                cop = cop/2;
            }

            locans *= floor(pow(3,nb));
             printf("-%d-%d\n",test,locans);
            answer+= locans;
        }
*/
        fprintf(g,"Case #%d: %ld\n",test,answer);
    }

    fclose(f);
    fclose(g);
}
