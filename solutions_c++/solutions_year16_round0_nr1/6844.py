#include<cstdio>
using namespace std;

int num[10];

bool found()
{
    for(int i=0; i<10; i++)
    {
        if(num[i] == 0)
            return false;
    }
    return true;
}

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("output.out", "w", stdout);

    int t, c=0, n;

    scanf("%d", &t);
    while(t--)
    {
        scanf("%d", &n);

        for(int i=0; i<10; i++)
            num[i] = 0;

        if(n == 0)
            printf("Case #%d: INSOMNIA\n", ++c);
        else
        {
            for(int i=1; ; i++)
            {
                long tmp1 = n*i;
                long l = tmp1;
                while(tmp1>0)
                {
                    long tmp2 = tmp1%10;
                    num[tmp2] = 1;
                    tmp1 /= 10;
                }

                if(found())
                {
                    printf("Case #%d: %ld\n", ++c, l);
                    break;
                }
            }
        }
    }

    return 0;
}
