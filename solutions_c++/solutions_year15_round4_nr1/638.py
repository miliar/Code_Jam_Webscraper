#include <iostream>
using namespace std;

char T[200][200];
int G[200], L[200], P[200], D[200];

int main()
{
    int te;
    cin>>te;
    for(int testy = 1; testy <= te; testy++)
    {
        for(int i=0; i<200; i++)
        {
            G[i] = L[i] = P[i] = D[i] = 0;
        }
        int R, C;
        cin>>R>>C;
        for(int i=1; i<=R; i++)
        {
            for(int j=1; j<=C; j++)
            {
                cin>>T[i][j];
                if (T[i][j] != '.')
                {
                    P[i] = max(P[i], j);
                    if (L[i] == 0 || L[i] > j)
                        L[i] = j;
                    D[j] = max(D[j], i);
                    if (G[j] == 0 || G[j] > i)
                        G[j] = i;
                }
            }
        }
        int ile = 0;
        for(int i=1; i<=R; i++)
        {
            for(int j=1; j<=C; j++)
            {
                if (T[i][j] == '.')
                    continue;
                if (P[i] == j && L[i] == j && G[j] == i && D[j] == i)
                    ile -= 1000000;
                if (T[i][j] == '^')
                    if (G[j] == i)
                        ile ++;
                if (T[i][j] == 'v')
                    if (D[j] == i)
                        ile ++;
                if (T[i][j] == '>')
                    if (P[i] == j)
                        ile ++;
                if (T[i][j] == '<')
                    if (L[i] == j)
                        ile ++;
            }
        }
        if (ile < 0)
            printf("Case #%d: IMPOSSIBLE\n", testy);
        else
            printf("Case #%d: %d\n", testy, ile);
    }
    
    
   // system("PAUSE");    
    return 0;
}
