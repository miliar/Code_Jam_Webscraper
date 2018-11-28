#include <iostream>
#include <cstdio>
using namespace std;

int t, a, d, odp, wynik;
int tab[1001];
int war[1001][1001];
int main()
{
    for(int i=1;i<=1000;i++)
        for(int j=1;j<=i;j++)
            war[i][j]=(i+j-1)/j-1;
    scanf("%d", &t);
    while(t--)
    {
        a++;
        odp=1000;
        scanf("%d", &d);
        for(int i=1;i<=1000;i++)
            tab[i]=0;
        for(int i=1;i<=d;i++)
        {
            int x;
            scanf("%d", &tab[i]);
        }
        for(int i=1;i<=1000;i++)
        {
            wynik=i;
            for(int j=1;j<=d;j++)
                wynik+=war[tab[j]][i];
            odp=min(odp, wynik);
        }
        printf("Case #%d: %d\n", a, odp);
    }
    return 0;
}
