#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <cstring>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

#define pb push_back
#define clean(a,b) memset(a,b,sizeof(a))
#define oo 1<<20
#define dd double
#define ll long long
#define ull unsigned long long
#define ff float
#define EPS 10E-6
#define fr first
#define sc second
#define MAXX 100100
#define PRIME_N 1000000
#define INFI 1<<30
#define SZ(a) ((int)a.size())
#define all(a) a.begin(),a.end()
#define MODD 1000000007

//int rx[] = {0,-1,0,1,1,-1,-1,0,1}; //four direction x
//int ry[] = {0,1,1,1,0,0,-1,-1,-1};   //four direction y
//int rep[] = {1,1,4,4,2,1,1,4,4,2}; //repet cycle for mod
//void ullpr(){printf("range unsigned long long : %llu\n",-1U);} //for ull
//void ulpr(){printf("range unsigned long : %lu\n",-1U);} //for ull
//void upr(){printf("range unsigned : %u\n",-1U);} //for ull

namespace matching
{
    typedef int val_t;
    const int SIZE = 10000;
    int v1, v2;
    vector<int> graph[SIZE];
    int mx[SIZE], my[SIZE];
    int total_matching;
    int dist[SIZE];
    int inf_dist;
    void reset()
    {
        for(int i = 0  ; i<SIZE ; i++)
            graph[i].clear();
    }
    bool bfs()
    {
        int x, y;
        queue<int> q;
        for (x = 0 ; x < v1 ; x++)
        {
            if (mx[x] == -1)
            {
                dist[x] = 0;
                q.push(x);
            }
            else
                dist[x] = -1;
        }
        bool flg = false;
        while (!q.empty())
        {
            x = q.front();
            q.pop();
            for (int i = 0 ; i < graph[x].size() ; i++)
            {
                y = graph[x][i];
                if (my[y] == -1)
                {
                    inf_dist = dist[x] + 1;
                    flg = true;
                }
                else if (dist[my[y]] == -1)
                {
                    dist[my[y]] = dist[x] + 1;
                    q.push(my[y]);
                }
            }
        }
        return flg;
    }
    bool dfs(int x)
    {
        if (x == -1) return true;
        for (int i = 0 ; i < graph[x].size() ; i++)
        {
            int y = graph[x][i];
            int tmp = (my[y] == -1) ? inf_dist : dist[my[y]];
            if (tmp == dist[x] + 1 && dfs(my[y]))
            {
                mx[x] = y;
                my[y] = x;
                return true;
            }
        }
        dist[x] = -1;
        return false;
    }
    int hopcroft()
    {
        memset(mx, -1, sizeof(mx));
        memset(my, -1, sizeof(my));
        total_matching = 0;
        while (bfs())
        {
            for (int x = 0 ; x < v1 ; x++)
                if (mx[x] == -1 && dfs(x))
                    total_matching++;
        }
        return total_matching;
    }
} // namespace matching


vector<dd>vWeightNeomi,vWeightKen;
vector<dd>vFlagNeomi,vFlagKen;

int PlayDecitefulWar()
{
    matching::reset();
    matching::v1= SZ(vWeightKen);
    matching::v2 = SZ(vWeightKen);

    for(int i = 0 ; i<SZ(vWeightNeomi) ; i++)
    {
        for(int j = 0; j<SZ(vWeightKen) ; j++)
        {
            if(vWeightKen[j]<vWeightNeomi[i])
                matching::graph[i].pb(j);
            else break;
        }
    }

    int maxmatching = matching::hopcroft();

    return maxmatching;
}


int PlayWar(void)
{
    int neomival = 0;

    for(int i = 0 ; i<SZ(vWeightNeomi) ; i++)
    {
        int ok = 0;
        for(int j = 0 ; j<SZ(vWeightKen) ; j++)
        {
            if(vFlagKen[j]==0 && vWeightKen[j]>vWeightNeomi[i])
            {
                vFlagKen[j] = 1;
                ok =1;
                break;
            }
        }

        for(int j = 0 ; j<SZ(vWeightKen) && !ok ; j++)
        {
            if(vFlagKen[j]==0)
            {
                vFlagKen[j] = 1;
                break;
            }
        }

        neomival += !ok;
    }
    return neomival;
}

int main()
{

    freopen("inpDL.txt" , "r+" , stdin);
    freopen("outDL.txt" , "w+" , stdout);

    int tcase,cas=1;
    scanf(" %d" ,&tcase);
    while(tcase--)
    {
        int n;
        vWeightKen.clear();
        vWeightNeomi.clear();

        vFlagKen.clear();
        vFlagNeomi.clear();

        scanf(" %d" , &n);

        for(int i = 0;  i<n ; i++)
        {
            dd val;
            scanf(" %lf",&val);
            vWeightNeomi.pb(val);
            vFlagNeomi.pb(0);
        }

        for(int i = 0; i<n ; i++)
        {
            dd val;
            scanf(" %lf" ,&val);
            vWeightKen.pb(val);
            vFlagKen.pb(0);
        }

        sort(all(vWeightKen));
        sort(all(vWeightNeomi));

        int warval = PlayWar();
        int decval = PlayDecitefulWar();
        printf("Case #%d: %d %d\n",cas++,decval, warval);

    }

    fclose(stdin);
    fclose(stdout);

    return 0;
}
