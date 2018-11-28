#include <cstdlib>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <string>
#include <queue>

using namespace std;
int N,M;
int T;
int maxiLig[101], maxiCol[101];
//const int inf = 200;
int tab[101][101];

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);

    scanf("%d", &T);

    for(int i = 0; i < T; i++)
    {
        scanf("%d%d", &N, &M);
        bool pos = true;

        for(int j = 0; j < N; j++)
            maxiLig[j]=0;
        for(int k = 0; k < M; k++)
            maxiCol[k]=0;

        for(int j = 0; j < N; j++)
        {
            for(int k = 0; k < M; k++)
            {
                scanf("%d", &tab[j][k]);
                maxiLig[j] = max(maxiLig[j], tab[j][k]);
                maxiCol[k] = max(maxiCol[k], tab[j][k]);
            }
        }

        for(int j = 0; j < N; j++)
        {
            for(int k = 0; k < M; k++)
            {
                if(tab[j][k] != min(maxiLig[j], maxiCol[k]))
                    pos=false;
            }
        }

        printf("Case #%d: ", i+1);
        if(pos) printf("YES\n");
        else printf("NO\n");
    }

    return 0;
}
