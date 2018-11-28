#include <cstdio>

void Testuj(int cislo)
{
    int S;
    scanf("%d ", &S);
    char znak;
    int index = 0;
    int akt;

    int soucet = 0;
    int pridat = 0;
    for(; index<=S; index++)
    {
        znak = getchar();
        akt = (int)znak-(int)'0';

        if(akt > 0 && soucet < index)
        {
            pridat += index-soucet;
            soucet = index;
        }
        soucet += akt;
    }
    printf("Case #%d: %d\n", cislo, pridat);
}

int main()
{
    int N;
    scanf("%d", &N);

    for(int i=0; i<N; i++)
    {
        Testuj(i+1);
    }

    return 0;
}
