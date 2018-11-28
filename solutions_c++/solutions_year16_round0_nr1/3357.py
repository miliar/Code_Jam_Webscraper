#include <iostream>
#include <cstdio>
using namespace std;

int main()
{
    int t;
    scanf("%d",&t);
    for (int tt=1;tt<=t;tt++)
    {
        int n;
        scanf("%d",&n);
        printf("Case #%d: ",tt);
        if (n==0)
        {
            printf("INSOMNIA\n");
            continue;
        }
        int flag = 0;
        for (int i=1; ; i++)
        {
            long long tmp = (long long)n * i;
            while (tmp > 0)
            {
                flag |= (1 << (tmp%10));
                tmp /= 10;
            }
            if (flag == 0x03ff)
            {
                printf("%lld\n",(long long)n*i);
                break;
            }
        }
    }
    return 0;
}
