#include <cstdio>

using namespace std;

int nb, X, Y;
int tab[20];
int result;
int total;

double recurcive(int nb, int indice)
{
    if (nb == 0)
    {
        //for (int i=0; i<20; i++) printf("%d ", tab[i]);
        //printf("\n");
        
        if (X > -10 && X < 10)
        if (tab[10+X] >= Y)
            return 1;
        
        return 0;
    }
    
    if (tab[indice] < tab[indice-1] && tab[indice] < tab[indice+1])
    {
        tab[indice] += 2;
        double tmp = recurcive(nb-1, 10);
        tab[indice] -= 2;
        return tmp;
    }
    
    if (tab[indice] < tab[indice-1] && tab[indice] > tab[indice+1])
        return recurcive(nb, indice+1);
    
    if (tab[indice] > tab[indice-1] && tab[indice] < tab[indice+1])
        return recurcive(nb, indice-1);
        
    if (tab[indice] > tab[indice-1] && tab[indice] > tab[indice+1])
    {
        return 0.5*recurcive(nb, indice+1) + 0.5*recurcive(nb, indice-1);
    }
}

void main2()
{
    scanf("%d%d%d", &nb, &X, &Y);
    
    for (int i=0; i<20; i++)
        tab[i] = (i%2) ? -1 : -2;
    
    
    printf("%.9lf", recurcive(nb, 10));
    //printf("%d %d", result, total);
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
