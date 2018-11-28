#include <cstdio>
#include <queue.h>
#include <algorithm>
using namespace std;

struct Dvojice
{
    int cislo;
    int pocet;
};

inline int Prevrat(int N)
{
    int cislo = N;
    int vysledek = 0;
    while(cislo > 0)
    {
        vysledek = vysledek*10 + cislo%10;
        cislo /= 10;
    }
    return vysledek;
}

const int limit = 1000000;
int pole[limit+5];

void Run(int index, int N)
{
    //--printf("Run(%d)\n", N);

    Dvojice akt, novy;
    akt.cislo = 1;
    akt.pocet = 1;

    queue<Dvojice> fronta;
    fronta.push(akt);

    //int maximum = 1;

    while(true)
    {
        akt = fronta.front();
        fronta.pop();
        //if(akt.cislo <= limit)
        //    pole[akt.cislo] = index;
        //if(akt.cislo > maximum)
        //    maximum = akt.cislo;
        //----printf("--%d\n", akt.cislo);
        /*
        for(int i=1; i<=10; i++)
        {
            printf("%d ", pole[i]);
        }
        */
        //---getchar();

        if(akt.cislo == N)
        {
            printf("Case #%d: %d\n", index, akt.pocet);
            return;
        }

        novy.cislo = akt.cislo+1;
        novy.pocet = akt.pocet+1;
        //if(novy.cislo > maximum)
        if(pole[novy.cislo] < index) // pridano
        {
            fronta.push(novy);
            pole[novy.cislo] = index;
        }

        novy.cislo = Prevrat(akt.cislo);
        /*
        //if(novy.cislo > akt.cislo)
        //{
            if(novy.cislo < 100000000)
            {
                if(novy.cislo > limit || (novy.cislo <= limit && pole[novy.cislo] < index))
                    fronta.push(novy);
            }
        //}
        */
        if(/*novy.cislo > akt.cislo &&*/ novy.cislo <= N && pole[novy.cislo] < index)
        {
            fronta.push(novy);
            pole[novy.cislo] = index;
        }
    }
}

int main()
{
    int T, N;
    scanf("%d", &T);

    for(int i=1; i<=limit; i++)
    {
        pole[i] = 0;
    }

    for(int i=1; i<=T; i++)
    {
        scanf("%d", &N);
        Run(i, N);
    }
    return 0;
}
