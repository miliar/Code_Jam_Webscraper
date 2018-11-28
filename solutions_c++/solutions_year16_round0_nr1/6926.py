#include <cstdio>

using namespace std;

long long int res, temp, n;

int digchecker = 1023;

void updatedig()
{
    temp = res;
    while(temp > 0)
    {
        digchecker &= ~(1<<(temp%10));
        temp /= 10;
    }
    return;
}

int main(void)
{

    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int t;
    scanf("%d", &t);

    for (int i = 0; i < t; ++i)
    {
        scanf("%lld", &n);
        printf("Case #%d: ", i+1);

        if(n==0)
            printf("INSOMNIA\n");
        else
        {
            digchecker = 1023;
            res = n;
            while(digchecker != 0)
            {
                updatedig();
                res += n;
            }
            printf("%lld\n", res-n);
        }
    }
    return 0;
}