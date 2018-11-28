#include <cstdio>
#include <cmath>

bool estPalindrome(int nb)
{
    int taille = 0;
    int tab[20];
    
    while (nb > 0)
    {
        tab[taille++] = nb % 10;
        nb /= 10;
    }
    
    for (int i=0; i<taille; i++)
        if (tab[i] != tab[taille-1-i]) return false;
    
    return true;
}

void main2()
{
    int A, B;
    scanf("%d%d", &A, &B);
    
    int nb = 0;
    int i = (int)sqrt(A);
    
    while (i*i < A) i++;
    while (i*i <= B)
    {
        if (estPalindrome(i) && estPalindrome(i*i)) nb++;
        i++;
    }
    
    printf("%d\n", nb);
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
