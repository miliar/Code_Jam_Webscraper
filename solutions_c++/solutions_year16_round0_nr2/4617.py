#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

int t;
char tmp[150];
long long numberOfSteps;

bool full()
{
    for (int i=0; i<strlen(tmp); i++)
    {
        if (tmp[i] == '-')
            return false;
    }

    return true;
}

void changeFrom(int poz)
{
    for (int i=poz; i>=0; i--)
    {
        if (tmp[i] == '-')
            tmp[i] = '+';
        else if (tmp[i] == '+')
            tmp[i] = '-';
    }
}

void solve()
{
    while(!full())
    {
        for (int i=strlen(tmp)-1; i>=0; i--)
        {
            if (tmp[i] == '-')
            {
                numberOfSteps++;
                changeFrom(i);
                break;
            }
        }
    }

}

int main()
{
    freopen("data.in", "r", stdin);
    freopen("data.out", "w", stdout);
    scanf("%d\n", &t);
    for (int i=1; i<=t; i++)
    {
        gets(tmp);
        solve();
        printf("Case #%d: %lld\n", i, numberOfSteps);
        numberOfSteps = 0;
    }
    return 0;
}
