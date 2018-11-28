#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
using namespace std;

#define Nmax 110

int N, M, MaxLin[Nmax], MaxCol[Nmax], Mat[Nmax][Nmax];
int T, TestCase, i, j;

int main()
{
    freopen("test.in", "r", stdin);
    freopen("test.out", "w", stdout);
    scanf("%i", &T);
    for(TestCase = 1; TestCase <= T; ++ TestCase)
    {
        memset(MaxLin, 0, sizeof(MaxLin));
        memset(MaxCol, 0, sizeof(MaxCol));
        scanf("%i %i", &N, &M);
        for(i = 1; i <= N; ++ i)
            for(j = 1; j <= M; ++ j)
            {
                scanf("%i", &Mat[i][j]);
                MaxLin[i] = max(MaxLin[i], Mat[i][j]);
                MaxCol[j] = max(MaxCol[j], Mat[i][j]);
            }
        bool OK = 1;
        for(i = 1; i <= N; ++ i)
            for(j = 1; j <= M; ++ j)
                if(MaxLin[i] > Mat[i][j] && MaxCol[j] > Mat[i][j])
                    OK = 0;
        if(OK) printf("Case #%i: YES\n", TestCase);
        else printf("Case #%i: NO\n", TestCase);
    }
    return 0;
}
