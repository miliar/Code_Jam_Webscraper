#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>


using namespace std;

int t;
int n, j;
char tmp[40];
long long vec[11];

void aduna()
{
    for (int i=strlen(tmp)-2; i>=0; i--)
    {
        if (tmp[i] == '1')
            tmp[i] = '0';
        else if (tmp[i] == '0')
        {
            tmp[i] = '1';
            return;
        }
    }
}

void print()
{
    printf("%s ", tmp);
    for (int i=0; i<10; i++)
        for (long long k=2; k<vec[i]; k++)
            if (vec[i] % k == 0)
            {
                printf("%lld ", k);
                break;
            }
    printf("\n");
}

bool prim(long long nr)
{
    if (nr <=2 || nr > 2 && nr % 2 == 0)
        return false;
    for (long long p=3; p * p <= nr; p+=2)
        if (nr % p == 0)
            return false;
    return true;
}

long long putere(int nr, int puterea)
{
    long long toReturn = 1;
    for (int i=1; i<=puterea; i++)
    {
        toReturn = toReturn * nr;
    }

    return toReturn;
}
bool isValid()
{
    int l = 0;
    int p = 0;
    for (int i=2; i<=10; i++)
    {
        long long goesIn = 0;
        for (int k=strlen(tmp)-1; k>=0; k--)
        {
            goesIn = goesIn + (tmp[k]-'0') * putere(i, p++);
        }

        if (prim(goesIn))
            return false;
        p = 0;
        vec[l++] = goesIn;
    }

    return true;
}

bool full()
{
    for (int i=0; i<strlen(tmp); i++)
    {
        if (tmp[i] == '0')
            return false;
    }

    return true;
}

void solve()
{
    tmp[0] = '1';
    tmp[n-1] = '1';
    for (int i=1; i<n-1; i++)
        tmp[i] = '0';
    int stop = 0;

    while(stop < j)
    {
        if (isValid())
        {
            print();
            stop++;
        }

        if (full())
            return;

        aduna();

        memset(vec, 0, sizeof(vec));
    }
}

int main()
{
    freopen("data.in", "r", stdin);
    freopen("data.out", "w", stdout);
    scanf("%d\n", &t);
    printf("Case #%d:\n", t);
    for (int i=1; i<=t; i++)
    {
        scanf("%d %d\n", &n, &j);
        solve();
    }
    return 0;
}
