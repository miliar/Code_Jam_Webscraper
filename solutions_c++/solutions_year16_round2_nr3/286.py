
#include<bits/stdc++.h>
using namespace std;
#define D(x)        cout<<#x " = "<<(x)<<endl
#define un(x)       x.erase(unique(x.begin(),x.end()), x.end())
#define sf(n)       scanf("%d", &n)
#define sff(a,b)    scanf("%d %d", &a, &b)
#define sfff(a,b,c) scanf("%d %d %d", &a, &b, &c)
#define pb          push_back
#define mp          make_pair
#define xx          first
#define yy          second
#define hp          (LL) 999983
#define MAX         1000
typedef long long int LL;
typedef pair<int,int> pii;


// bipartite matching using dfs [ 1 indexing ]

int Left[MAX+10], Right[MAX+10];
bool vis[MAX+10];
vector<int> edge[MAX+10]; // Left side Graph

bool dfs(int idx)
{
    if(vis[idx]) return false;
    vis[idx] = 1;

    int i, nw, len = edge[idx].size();
    for(i = 0; i < len; i++)
    {
        nw = edge[idx][i];
        if(Right[nw] == -1)
        {
            Right[nw] = idx;
            Left[idx] = nw;
            return true;
        }
    }

    for(i = 0; i < len; i++)
    {
        nw = edge[idx][i];
        if(dfs(Right[nw]))
        {
            Left[idx] = nw;
            Right[nw] = idx;
            return true;
        }
    }

    return false;
}

int match(int can) // can = cardinality of left half
{
    int i, ret = 0;
    bool done;

    memset(Left, -1, sizeof(Left));
    memset(Right, -1, sizeof(Right));
    do{
        done = true;
        memset(vis, false, sizeof(vis));
        for(i = 1; i <= can; i++)
            if(Left[i] == -1 && dfs(i))
                done = false;
    }while(!done);

    for(i = 1; i <= can; i++) ret += (Left[i] != -1);
    return ret;
}

map<string,int> Lm, Rm;
string w1, w2;

int main()
{
    freopen("c:\\Users\\User\\Desktop\\C.in", "r", stdin);
    freopen("c:\\Users\\User\\Desktop\\out.txt", "w", stdout);

    int i, j, k, t, cs;
    int n, Lidx, Ridx;
    int edgeCnt;

    sf(t);
    for(cs = 1; cs <= t; cs++)
    {
        Lm.clear();
        Rm.clear();

        Lidx = Ridx = 0;

        sf(n);

        edgeCnt = n;
        for(i =1; i <= n ; i++)
        {
            cin >> w1 >> w2;
            if(Lm.find(w1) == Lm.end())
                Lm[w1] = ++Lidx;

            if(Rm.find(w2) == Rm.end())
                Rm[w2] = ++Ridx;

            edge[Lm[w1]].pb(Rm[w2]);
        }

        edgeCnt -= match(Lidx);

        for(i = 1; i <= Lidx; i++)
            if(Left[i] == -1)
                edgeCnt--;

        for(i = 1; i <= Ridx; i++)
            if(Right[i] == -1)
                edgeCnt--;

        printf("Case #%d: %d\n", cs, edgeCnt);
        for(i = 1; i <= Lidx; i++)
            edge[i].clear();
    }
    return 0;
}




