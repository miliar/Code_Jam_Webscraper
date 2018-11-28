#include <cstdio>
#include <algorithm>

using namespace std;

int mini, N;
int tab[100];

void recurcive(int id, int taille, int actuel)
{
    if (actuel >= mini) return;
    
    if (id >= N)
    {
        mini = min(mini, actuel);
        return;
    }
    
    if (tab[id] < taille) return recurcive(id+1, taille + tab[id], actuel);
    
    if (taille > 1)
    recurcive(id, 2*taille-1, actuel+1);
    recurcive(id+1, taille, actuel+1);
}

void main2()
{
    int debut;
    scanf("%d%d", &debut, &N);
    
    for (int i=0; i<N; i++)
        scanf("%d", &tab[i]);
        
    sort(tab, tab + N);
    mini = N;
    
    recurcive(0, debut, 0);
    
    printf("%d", mini);
}

int main()
{
    int T;
    scanf("%d", &T);
    
    for (int i=0; i<T; i++)
    {
        printf("Case #%d: ", i+1);
        main2();
        printf("\n");
    }
}
