#include<stdio.h>
#include<algorithm>
using namespace std;

FILE *out;


int main()
{
    int t,k;
    double c,f,x,n,ans,res = 0.0,temp1,temp2,last;

    FILE *fp = fopen("B-large.in", "r");
    out = fopen("B-large.out", "w");

    fscanf(fp, "%d", &t);
    for (k = 1; (k <= t) && !feof(fp) ; k++)
    {
        //printf("case: %d\n",k);
        fscanf(fp,"%lf %lf %lf",&c, &f, &x);
        n = 1;
        res = x/2;
        last = x/2;
        while(1)
        {
            temp1 = x/(2.0 + (n - 1) * f);
            temp2 = c/(2.0 + (n - 1) * f) + x/(2.0 + n * f);
            if(temp1 > temp2)
            {
                res = res + temp2 - last;
                last = x/(2.0 + n * f);
                n++;
            }
            else
            {
                break;
            }
            //printf("%lf ",res);
        }
        fprintf(out,"Case #%d: ",k);
        fprintf(out,"%lf\n",res);

    }

    return 0;
}
