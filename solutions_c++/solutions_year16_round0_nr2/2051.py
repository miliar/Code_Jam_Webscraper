#include <bits/stdc++.h>
using namespace std;

int t;

int n;

char wcz[107];
int tab[107];

int co;

int wyn;

int main()
{
    scanf("%d", &t);
    for (int tt=1; tt<=t; tt++)
    {
        scanf("%s", wcz+1);
        for (int i=1; 1; i++)
        {
            if (!wcz[i])
            {
                n=i-1;
                break;
            }
            tab[i]=(wcz[i]=='+');
        }
        co=1;
        wyn=0;
        for (int i=n; i; i--)
        {
            if (tab[i]==co)
            continue;
            co^=1;
            wyn++;
        }
        printf("Case #%d: %d\n", tt, wyn);
    }
    return 0;
}
