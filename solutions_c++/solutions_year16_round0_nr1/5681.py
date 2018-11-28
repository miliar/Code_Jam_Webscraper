#include <algorithm>
#include <string.h>
#include <vector>
#include <cstdio>
#include <climits>
#include <iostream>
using namespace std;
typedef long long lld;

int UTFO[10], TFOkey;
int lft;

void RollBack()
{
    lft = 10;
    TFOkey++;
}

int GetLFT(lld num)
{
    do
    {
        int cur = num%10LL;
        if (UTFO[cur] != TFOkey)
        {
            lft--;
            UTFO[cur] = TFOkey;
        }
        num /= 10LL;
    }
    while (num>0);

    return lft;
}

int main ()
{
    freopen("input.txt", "r", stdin);
    freopen("otp.txt", "w", stdout);

    int tests;
    scanf("%d", &tests);
    for (int t=1; t<=tests; t++)
    {
        lld beg, cur = 0;
        scanf("%lld", &beg);
        if (beg == 0)
        {
            printf("Case #%d: INSOMNIA\n", t);
            continue;
        }

        RollBack();
        do
        {
            cur += beg;
            GetLFT(cur);
        }
        while (lft>0);

        printf("Case #%d: %lld\n", t, cur);
    }
}

