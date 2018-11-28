//Przemysław Jakub KOzłowski
#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;
const int N = 103, M = 103, INF = 1000000009;

int n,m;
char tab[N][M];
int wyn[N][M];
char zmien[N][M];

int main()
{
    int t;
    scanf("%d", &t);
    for(int ti = 1;ti <= t;ti++)
    {
        scanf("%d%d", &n, &m);
        for(int i = 1;i <= n;i++)
            for(int j = 1;j <= m;j++)
                scanf(" %c", &tab[i][j]);
        
        for(int i = 1;i <= n;i++)
            for(int j = 1;j <= m;j++)
                zmien[i][j] = wyn[i][j] = 0;
        
        // Lewy bok
        for(int i = 1;i <= n;i++)
        {
            int num = 0;
            for(int j = 1;j <= m;j++)
                if(tab[i][j] != '.')
                {
                    num = j;
                    break;
                }
            if(num)
            {
                wyn[i][num]++;
                if(tab[i][num] == '<') zmien[i][num] = 1;
            }
        }
        
        // Prawy bok
        for(int i = 1;i <= n;i++)
        {
            int num = 0;
            for(int j = m;j >= 1;j--)
                if(tab[i][j] != '.')
                {
                    num = j;
                    break;
                }
            if(num)
            {
                wyn[i][num]++;
                if(tab[i][num] == '>') zmien[i][num] = 1;
            }
        }
        
        // Górny bok
        for(int j = 1;j <= m;j++)
        {
            int num = 0;
            for(int i = 1;i <= n;i++)
                if(tab[i][j] != '.')
                {
                    num = i;
                    break;
                }
            if(num)
            {
                wyn[num][j]++;
                if(tab[num][j] == '^') zmien[num][j] = 1;
            }
        }
        
        // Dolny bok
        for(int j = 1;j <= m;j++)
        {
            int num = 0;
            for(int i = n;i >= 1;i--)
                if(tab[i][j] != '.')
                {
                    num = i;
                    break;
                }
            if(num)
            {
                wyn[num][j]++;
                if(tab[num][j] == 'v') zmien[num][j] = 1;
            }
        }
        
        int Wyn = 0;
        for(int i = 1;i <= n;i++)
            for(int j = 1;j <= m;j++)
                if(zmien[i][j])
                {
                    if(wyn[i][j] == 4) Wyn = INF;
                    Wyn++;
                }
        
        printf("Case #%d: ", ti);
        if(Wyn < INF) printf("%d\n", Wyn);
        else printf("IMPOSSIBLE\n");
    }
    return 0;
}
