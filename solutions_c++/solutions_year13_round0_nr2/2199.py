//Przemysław Jakub Kozłowski
#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;
const int N = 103, M = 103;

int t;
int n,m;
int tab[N][M];
int wie[N], kol[M];

int main()
{
    scanf("%d", &t);
    for(int ti = 1;ti <= t;ti++)
    {
        scanf("%d%d", &n, &m);

        for(int i = 1;i <= n;i++)
            wie[i] = 0;
        for(int i = 1;i <= m;i++)
            kol[i] = 0;

        for(int i = 1;i <= n;i++)
            for(int j = 1;j <= m;j++)
            {
                scanf("%d", &tab[i][j]);
                wie[i] = max(wie[i],tab[i][j]);
                kol[j] = max(kol[j],tab[i][j]);
            }

        bool wyn = 1;

        for(int i = 1;i <= n;i++)
            for(int j = 1;j <= m;j++)
                if(tab[i][j] != min(wie[i],kol[j]))
                {
                    wyn = 0;
                    break;
                }

        printf("Case #%d: %s\n", ti, (wyn ? "YES" : "NO"));
    }
    return 0;
}