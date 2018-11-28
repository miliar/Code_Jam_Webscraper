#include <cstdio>
#include <algorithm>
#include <list>
#include <map>
#include <queue>
using namespace std;

struct Deplacement
{
    int depart, arrivee, nb;
    
    void lire()
    {
        scanf("%d%d%d", &depart, &arrivee, &nb);
    }
    
    bool operator<(const Deplacement &autre) const
    {
        return depart < autre.depart;
    }
};

int calcul(int a, int b)
{
    return a * (a+1) / 2 - (a-b) * (a-b+1) / 2;
}

void main2()
{
    int N, M;
    scanf("%d%d", &N, &M);
    list<int> station;
    map<int, int> t;
    
    int prix = 0;
    Deplacement tab[M+1];
    for (int i=0; i<M; i++)
    {
        tab[i].lire();
        station.push_back(tab[i].depart);
        station.push_back(tab[i].arrivee);
        prix += tab[i].nb * calcul(N, tab[i].arrivee - tab[i].depart);
    }
    tab[M].depart = 1000000001;
    tab[M].arrivee = 1000000001;
    tab[M].nb = 0;
    
    station.sort();
    station.unique();
    sort(tab, tab + M);
    
    int i = 0;
    int j = 0;
    //printf("%d\n", prix);
    
    priority_queue<pair<int, int> > temp;
    temp.push(make_pair(-1000000001, M));
    
    for (list<int>::iterator it=station.begin(); it!=station.end(); it++)
    {
        //printf("\n%d", *it);
        
        while (tab[i].depart == *it)
        {
            //printf("\n+%d", tab[i].nb);
            temp.push(make_pair(-tab[i].arrivee, i));
            t[*it] = t[*it] + tab[i].nb;
            i++;
        }
        
        while (tab[temp.top().second].arrivee == *it)
        {
            j = temp.top().second;
            temp.pop();
            
            //printf("\n-%d", tab[j].nb);
            while (tab[j].nb > 0)
            {
                map<int, int>::reverse_iterator s = t.rbegin();
                if (s->second > tab[j].nb)
                {
                    //printf("-> %d ", tab[j].nb * calcul(N, *it - s->first));
                    prix -= tab[j].nb * calcul(N, *it - s->first);
                    s->second -= tab[j].nb;
                    tab[j].nb = 0;
                }
                else
                {
                    //printf("-> %d ", s->second * calcul(N, *it - s->first));
                    prix -= s->second * calcul(N, *it - s->first);
                    tab[j].nb -= s->second;
                    t.erase(s->first);
                }
            }
            j++;
        }
    }
    
    //printf("%d %d\n", i, j);
    
    printf("%d", prix % 1000002013);
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
