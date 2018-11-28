#include <cstdio>

using namespace std;

long long int x;
bool cyfry[10];
int ileUz;

void SprawdzCyfry(long long int x)
{
    int ost;
    //int zap = x;
    while(x > 0)
    {
        ost = x % 10;
        if (!cyfry[ost])
        {
            cyfry[ost] = true;
            ++ileUz;
            //printf("# %d w %d\n", ost, zap);
        }
        x = x/10;
    }
}

int main()
{
    int T, N;

    scanf("%d", &T);

    long long int x;
    int czas;

    for (int i = 1; i <= T; ++i)
    {
        scanf("%d", &N);
        if (N == 0)
        {
            printf("Case #%d: INSOMNIA\n", i);
            continue;
        }
        x = 0;

        for (int j = 0; j < 10; ++j)
            cyfry[j] = false;
        ileUz = 0;

        czas = 0;
        while (ileUz < 10)
        {
            x+=N;
            SprawdzCyfry(x);
            ++czas;
            //printf("..%d\n", czas);
        }
        printf("Case #%d: %lld\n", i, x);
    }

    return 0;
}
