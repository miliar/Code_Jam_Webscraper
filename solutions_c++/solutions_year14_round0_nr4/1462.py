#include <stdio.h>
#include <set>

using namespace std;

int playWar(set<float>naomi,set<float>ken,int n)
{
    set<float>::iterator n_it= naomi.end();
    set<float>::iterator k_it= ken.end();

    k_it--;
    int score=0;
    
    for(int i=0;i<n;i++)
    {
        n_it--;
        if(*n_it>*k_it)
            score++;
        else
            k_it--;
    }
    return score;
}

int playDWar(set<float>naomi,set<float>ken, int n)
{
    set<float>::iterator n_it= naomi.end();
    set<float>::iterator k_it= ken.end();

    n_it--;
    int score=0;

    for(int i=0;i<n;i++)
    {
        k_it--;
        if(*n_it>*k_it)
        {
            score++;
            n_it--;
        }
    }
    return score;
}

int main()
{
    int cases;
    char garbage[81];
    scanf("%d",&cases);
    fgets(garbage,80,stdin);
    for(int k = 0; k< cases; k++)
    {
        set<float> naomi;
        set<float> ken;
        int n;
        float tmp;
        scanf("%d",&n);
        fgets(garbage,80,stdin);
        for(int i =0; i<n;i++)
        {
            scanf("%f",&tmp);
            naomi.insert(tmp);
        }
        fgets(garbage,80,stdin);

        for(int i =0; i<n;i++)
        {
            scanf("%f",&tmp);
            ken.insert(tmp);
        }
        fgets(garbage,80,stdin);

        printf("Case #%d: %d %d\n",k+1,playDWar(naomi,ken,n),playWar(naomi,ken,n));
    }
    return 0;
}
