#include<cstdio>

int main(void)
{
    int t;
    scanf("%d", &t);
    int cs=1, i, nf;
    double c, f, x, p, time;
    while(cs<=t)
    {
        nf=0;
        p=2.0;
        time=0;

        scanf("%lf %lf %lf", &c, &f, &x);

       // nf = (x/c) - 1.0;
        //printf("%d\n", nf);

        while(1)
        {
            if((time+(x/p))>(time+(c/p)+(x/(p+f))))
            {
                time = time+c/p;
                p = p+f;
            }
            else
                break;
        }
        time = time+x/p;

        printf("Case #%d: %.7lf\n", cs, time);

        cs++;
    }
}
