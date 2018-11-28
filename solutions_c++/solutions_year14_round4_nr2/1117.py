#include <cstdlib>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <cstring>
#include <set>

using namespace std;

int N,M;
int val[15];
int tt;
const int inf = 999999;
int nbG, nbD;
int gauche[15];
int droite[15];
int tv[15];

void attribuePos()
{
    for(int i = 0; i < nbG; i++)
    {
        int nb=0;
        for(int j = 0; j < nbG; j++)
        {
            if(val[gauche[j]]<val[gauche[i]])
                nb++;
        }
        tv[gauche[i]]=nb;
    }
    for(int i = 0; i < nbD; i++)
    {
        int nb=0;
        for(int j = 0; j < nbD; j++)
        {
            if(val[droite[j]] > val[droite[i]])
                nb++;
        }
        tv[droite[i]]=nb+nbG;
    }
}

int compte_inv1()
{
    int nb=0;
    for(int i = 0; i < N; i++)
    {
        for(int j = 0; j < i; j++)
            if(tv[j]>tv[i])
                nb++;
    }
    return nb;
}

void compute_best(int id)
{
    if(id == N)
    {
        attribuePos();
        int nm = compte_inv1();
        if(nm < tt) tt = nm;
        return;
    }

    gauche[nbG++]=id;
    compute_best(id+1);
    nbG--;
    droite[nbD++]=id;
    compute_best(id+1);
    nbD--;
}

int main()
{
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("B-small-attempt0.out", "w", stdout);

    int T;
    scanf("%d", &T);

    for(int t = 1; t <= T; t++)
    {
        scanf("%d", &N);
        tt=inf;

        for(int i = 0; i < N; i++)
        {
            scanf("%d", &val[i]);
        }

        compute_best(0);

        printf("Case #%d: %d\n",t, tt);
    }

    return 0;
}
