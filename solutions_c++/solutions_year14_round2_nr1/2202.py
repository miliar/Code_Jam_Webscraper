#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int ri()
{
    int a;
    scanf("%i", &a);
    return a;
}

unsigned long long rl()
{
    unsigned long long a;
    scanf("%llu", &a);
    return a;
}

double rd()
{
    double a;
    scanf("%lf", &a);
    return a;
}

int main()
{
    int t, q=1;
    t = ri();
    while(t--)
    {
        int n = ri();
        char a[200];
        char b[200];
        int qtda[200];
        int qtdb[200];
        char ca[200];
        char cb[200];
        memset(qtda, 0, sizeof(qtda));
        memset(qtdb, 0, sizeof(qtdb));
        scanf("%*c%s", a);
        scanf("%*c%s", b);
        ca[0] = a[0];
        cb[0] = b[0];
        qtda[0] = 1;
        qtdb[0] = 1;
        int ia = 0;
        int ib = 0;
        int i, ta, tb;
        ta = strlen(a);
        tb = strlen(b);
        for(i=1;i<ta;i++)
        {
            if(a[i]==ca[ia])
            {
                qtda[ia]++;
            }
            else
            {
                ia++;
                qtda[ia] = 1;
                ca[ia] = a[i];
            }
        }
        for(i=1;i<tb;i++)
        {
            if(b[i]==cb[ib])
            {
                qtdb[ib]++;
            }
            else
            {
                ib++;
                qtdb[ib] = 1;
                cb[ib] = b[i];
            }
        }
        printf("Case #%i: ", q++);
        if(ia==ib)
        {
            int ok = 1;
            int qtd = 0;
            for(i=0;i<=ia;i++)
            {
                if(ca[i]==cb[i])
                {
                    if(qtda[i]<qtdb[i])
                        qtd+=qtdb[i]-qtda[i];
                    else
                        qtd+=qtda[i]-qtdb[i];
                }
                else
                {
                    ok=0;
                }
            }
            if(ok==1)
            {
                printf("%i\n", qtd);
            }
            else
            {
                printf("Fegla Won\n");
            }
        }
        else
        {
            printf("Fegla Won\n");
        }

    }
    return 0;
}
