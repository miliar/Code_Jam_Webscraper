#include<stdio.h>

int t, n;
int f[13];

int main ()
{
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);

    scanf("%d",&t);
    for(int i = 1; i <= t; i++)
    {
        scanf("%d",&n);
        if(!n)
        {
            printf("Case #%d: INSOMNIA\n",i);
            continue;
        }
        int cif = 0, initN = n;
        do
        {
            int cn = n;
            while(cn)
            {
                int last = cn % 10;
                if(!f[last])
                    cif++;
                f[last] = 1;
                cn /= 10;
            }
            if(cif == 10)
                break;
            n += initN;
        }while(1);
        printf("Case #%d: %d\n", i, n);
        for(int i = 0; i < 10; i++)
            f[i] = 0;
    }

    return 0;
}
