#include <iostream>
#include <cstdio>

using namespace std;

int N, J;
int reprez[20];
long long a[12];
long long div[12];


void next()
{
    int i = 1;
    while(reprez[i] == 1 && i < N-1)
    {
        reprez[i] = 0;
        i++;
    }
    if(i < N-1)
        reprez[i] = 1;
}

void calc()
{
    long long aux[12];
    for(int i = 0; i < 12; i++)
        aux[i] = 1ll;
    for(int i = 2; i <= 10; i++)
        a[i] = 0;

    for(int i = 0; i < N; i++)
    {
        for(int j = 2; j <= 10; j++)
            a[j] += reprez[i] * aux[j];

        for(int j = 2; j <= 10; j++)
            aux[j] *= j;
    }
}

bool verif()
{
    for(int i = 2; i <= 10; i++)
    {
        int ok = 0;
        for(long long d = 2; d * d <= a[i] && !ok; d++)
            if(a[i] % d == 0)
            {
                    div[i] = d;
                    ok = 1;
            }
        if(ok == 0)
            return false;
    }
    return true;
}

void afisare()
{
    for(int i = N-1; i >= 0; i--)
        printf("%d", reprez[i]);
    for(int i = 2; i <= 10; i++)
        printf(" %d", div[i]);
    printf("\n");
}

int main()
{
    freopen("data.in", "r", stdin);
    freopen("data.out", "w", stdout);

    int T;
    scanf("%d%d%d", &T, &N, &J);

    reprez[0] = reprez[N-1] = 1;

    printf("Case #1:\n");
    while(J)
    {
        calc();
        if(verif())
        {
            afisare();
            J--;
        }
        next();
    }

    return 0;
}
