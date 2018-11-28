#include <stdio.h>
int main()
{
    FILE *fp,*fo;
	fp=fopen("B-large.in","r");
	fo=fopen("secondlargeans.o","w");
    int test,i,k;
    double c, f, x,time,sum,ans,max;
    fscanf(fp,"%d", &test);
    for (i = 1; i <= test; i++)
    {
        fscanf(fp,"%lf %lf %lf", &c, &f, &x);
        max = x+10;
        time = 0;
        sum = 0;
        ans = -1;
        for (k = 0; k <= max; k++)
        {
            if (k > 0)
            time = time + (c/(f*(k-1) + 2));
            sum = time + (x / (f*k + 2));
            if (ans == -1 || sum < ans)
            ans = sum;
        }
        fprintf(fo,"Case #%d: %.7f\n", i, ans);
    }
    return 0;
}
