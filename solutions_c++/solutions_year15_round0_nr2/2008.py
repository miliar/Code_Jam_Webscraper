#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <vector>
using namespace std;

void Testuj_old(int poradi)
{
    int D;
    scanf("%d", &D);

    vector<int> halda;
    int cislo;
    int vysledek = 0;
    for(int i=0; i<D; i++)
    {
        scanf("%d", &cislo);
        halda.push_back(cislo);
        if(cislo > vysledek)
            vysledek = cislo;
    }
    make_heap(halda.begin(), halda.end());

    int cas = 0;
    while(/*halda.size() > 0 &&*/ halda.at(0) >= halda.size()) // teoreticky staci ">"
    {
        //printf("while\n");
        // vyprazdneni
        /*
        while(halda.size() > 0 && halda.at(0) <= cas+1)
        {
            //printf("pop: %d\n", halda.at(0));
            pop_heap(halda.begin(), halda.end());
            halda.pop_back();
        }
        if(halda.size() == 0)
            break;
        */

        //printf("while...\n");

        cislo = halda.at(0);
        pop_heap(halda.begin(), halda.end());
        halda.pop_back();
        /*
        if(cislo >= cas+1)
        {
            //printf("cislo = %d\n", cislo);
            halda.push_back(cas+1 + ((cislo-cas)/2));
            //printf("insert(%d)\n", cas+1 + (cislo/2));
            push_heap(halda.begin(), halda.end());
            halda.push_back(cas+1 + ((cislo-cas+1)/2));
            //printf("insert(%d)\n", cas+1 + ((cislo+1)/2));
            push_heap(halda.begin(), halda.end());
        }*/
        halda.push_back(cislo/2);
        push_heap(halda.begin(), halda.end());
        halda.push_back((cislo+1)/2);
        push_heap(halda.begin(), halda.end());

        cas++;

        //printf("testing... %d+%d < %d\n", cas, halda.at(0), vysledek);
        if(cas+halda.at(0) < vysledek)
            vysledek = cas+halda.at(0);

        /*
        printf("t=%d:", cas);
        for(int i=0; i<halda.size(); i++)
            printf(" %d", halda.at(i));
        printf("\n");
        */
    }
    printf("Case #%d: %d\n", poradi, vysledek);
}

/*
int pole[1005];
void Testuj(int cislo)
{
    int D;
    scanf("%d", &D);

    for(int i=0; i<=1000; i++)
        pole[i] = 0;
    int cislo;
    int vysledek = 0;
    for(int i=0; i<P; i++)
    {
        scanf("%d", &cislo);
        pole[cislo]++;
        if(cislo > vysledek)
            vysledek = cislo;
    }

}
*/

int pole[10005];
int pole2[10005][2];

int cmp(const void *a, const void *b)
{
    return (*(int*)b) - (*(int*)a);
}

void Testuj(int poradi)
{
    int D;
    scanf("%d", &D);

    for(int i=0; i<D; i++)
    {
        scanf("%d", &pole[i]);
    }

    qsort(pole, D, sizeof(int), cmp);

    /*
    for(int i=0; i<D; i++)
    {
        printf("-%d\n", pole[i]);
    }
    */

    pole2[0][0] = pole[0];
    pole2[0][1] = 1;
    int index = 0;
    for(int i=1; i<D; i++)
    {
        if(pole2[index][0] == pole[i])
            pole2[index][1]++;
        else
        {
            index++;
            pole2[index][0] = pole[i];
            pole2[index][1] = 1;
        }
    }

    /*
    for(int i=0; i<=index; i++)
    {
        printf("--%d %d\n", pole2[i][0], pole2[i][1]);
    }
    */

    int vysledek = pole2[0][0];
    int pocet;
    //for(int i=(pole2[0][0]+1)/2; i>=2; i--)
    for(int i=pole2[0][0]; i>=1; i--)
    {
        pocet = 0;
        for(int j=0; j<=index; j++)
        {
            if(pole2[j][0] > i)
                pocet += ((pole2[j][0]-1)/i) * pole2[j][1];
            else
                j = index+1; // break;
        }
        //printf("testing (%d): %d+%d\n", i, i, pocet);
        if(i+pocet < vysledek)
        {
            vysledek = i+pocet;
        }
    }

    printf("Case #%d: %d\n", poradi, vysledek);
}

int main()
{
    //vector<int> halda;
    /*
    for(int i=1; i<=10; i++)
    {
        halda.push_back((i*i)%50);
    }
    make_heap(halda.begin(), halda.end());
    for(int i=0; i<halda.size(); i++)
    {
        printf("...%d\n", halda.at(i));
    }
    */
    /*
    for(int i=1; i<=10; i++)
    {
        halda.push_back((i*i)%10);
        push_heap(halda.begin(), halda.end());
    }
    while(halda.size() > 0)
    {
        printf("...%d\n", halda.at(0));
        pop_heap(halda.begin(), halda.end());
        halda.pop_back();
    }
    */

    int T;
    scanf("%d", &T);

    for(int i=1; i<=T; i++)
    {
        Testuj(i);
    }

    return 0;
}
