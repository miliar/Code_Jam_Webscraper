#define _CRT_SECURE_NO_WARNINGS

#include <cstdio>

#include <set>

using namespace std;

typedef set<double> TDoubleSet;

void ReadSet(TDoubleSet* result, int n) 
{
    result->clear();
    for (int i = 0; i < n; ++i)
    {
        double w;
        scanf("%lf", &w);
        result->insert(w);
    }
}

int main()
{
    freopen("D-large.in", "r", stdin);
    freopen("D-large.out", "w", stdout);
    // freopen("input.txt", "r", stdin);
    // freopen("output.txt", "w", stdout);
    
    int nTests;
    scanf("%d", &nTests);
    for (int iTest = 0; iTest < nTests; ++iTest)
    {
        int n;
        scanf("%d", &n);
        TDoubleSet naomi0;
        ReadSet(&naomi0, n);
        TDoubleSet ken0;
        ReadSet(&ken0, n);

        int war = 0;
        {
            TDoubleSet naomi = naomi0;
            TDoubleSet ken = ken0;
            for (int i = 0; i < n; ++i)
            {
                double w = *(naomi.begin());
                naomi.erase(naomi.begin());
                TDoubleSet::iterator toKen = ken.upper_bound(w);
                if (toKen != ken.end())
                {
                    ken.erase(toKen);
                }
                else
                {
                    ken.erase(ken.begin());
                    ++war;
                }
            }
        }

        int dwar = 0;
        {
            TDoubleSet naomi = naomi0;
            TDoubleSet ken = ken0;
            for (int i = 0; i < n; ++i)
            {
                TDoubleSet::iterator maxKen = ken.end();
                --maxKen;
                if (*(naomi.begin()) > *(ken.begin()))
                {
                    ++dwar;
                    naomi.erase(naomi.begin());
                    ken.erase(ken.begin());
                }
                else
                {
                    naomi.erase(naomi.begin());
                    ken.erase(maxKen);
                }
            }
        }

        printf("Case #%d: %d %d\n", iTest + 1, dwar, war);
    }

    return 0;
}