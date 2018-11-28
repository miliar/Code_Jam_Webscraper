#include <cstdio>
#include <queue>
using namespace std;

void main2()
{
    int nb_lin, nb_col;
    scanf("%d%d", &nb_lin, &nb_col);
    
    queue<pair<int, int> > en_cours;
    int grille[nb_lin][nb_col];
    bool vu[nb_lin][nb_col];
    
    int max_lin[nb_lin];
    int max_col[nb_col];
    for (int i=0; i<nb_lin; i++) max_lin[i] = 0;
    for (int j=0; j<nb_col; j++) max_col[j] = 0;
    
    for (int i=0; i<nb_lin; i++)
    for (int j=0; j<nb_col; j++)
    {
        scanf("%d", &grille[i][j]);
        max_lin[i] = max(max_lin[i], grille[i][j]);
        max_col[j] = max(max_col[j], grille[i][j]);
    }
     
    for (int i=0; i<nb_lin; i++)
    for (int j=0; j<nb_col; j++)
    {
        if (grille[i][j] < max_lin[i] && grille[i][j] < max_col[j])
        {
            printf("NO\n");
            return;
        }
    }
    
    printf("YES\n");
}

int main()
{
    int T;
    scanf("%d", &T);
    
    for (int i=0; i<T; i++)
    {
        printf("Case #%d: ", i+1);
        main2();
    }
}
