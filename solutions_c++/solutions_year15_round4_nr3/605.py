#include <iostream>
#include <string.h>
#include <stdlib.h>
#include <stdio.h>
#include<algorithm>
#include<map>
#include<vector>
#include<sstream>
using namespace std;
typedef long long LL;
typedef long double LD;
const LD eps=1e-13;
const int maxm=200100;
const int maxn=20000;
#define INF 0x5fffffff
map<string, int> ddd;
vector<int> zz[2010];
struct sap
{
    struct edge
    {
        int to, cap, next;
    } EE[maxm * 2];
    
    int p, dd[maxn], asdf[maxn], eqwqe[maxn];
    int n, m, s, t, maxFlow;
    
    inline int min(int a, int b)
    {
        return a < b ? a : b;
    }
    inline void Add(int a, int b, int c)
    {
        EE[p].to = b, EE[p].cap = c, EE[p].next = dd[a], dd[a] = p++;
        EE[p].to = a, EE[p].cap = 0, EE[p].next = dd[b], dd[b] = p++;
    }
    int dfs(int u, int pre)
    {
        if (u == t)
            return pre;
        int now, aug, mh = n + 10, to, tmp = pre;
        for (now = dd[u]; now; now = EE[now].next)
        {
            to = EE[now].to;
            if (EE[now].cap)
            {
                if (pre && asdf[u] == asdf[to] + 1)
                {
                    aug = dfs(to, min(pre, EE[now].cap));
                    pre -= aug;
                    EE[now].cap -= aug;
                    EE[now ^ 1].cap += aug;
                    if (asdf[s] >= n)
                        return tmp - pre;
                }
                mh = min(mh, asdf[to]);
            }
        }
        if (tmp - pre > 0)
            return tmp - pre;
        --eqwqe[asdf[u]];
        if (!eqwqe[asdf[u]])
        {
            asdf[s] = n;
            return 0;
        }
        ++eqwqe[asdf[u] = mh + 1];
        return 0;
    }
    void pre(int nn, int ss = -1, int tt = -1)
    {
        p = 2;
        memset(dd, 0, sizeof(dd));
        n = nn;
        if(ss == -1) s = 0;
        else s = ss;
        if (tt == -1) t = n - 1;
        else t = tt;
    }
    void INIT()
    {
        maxFlow = 0;
        memset(asdf, 0, sizeof(asdf));
        memset(eqwqe, 0, sizeof(eqwqe));
        eqwqe[0] = n;
    }
    void SSSPA()
    {
        INIT();
        while (asdf[s] < n)
            maxFlow += dfs(s, INF);
    }
    
} wwwww;

int main()
{
    freopen("/Users/ZZ/Desktop/in.txt","r",stdin);
    freopen("/Users/ZZ/Desktop/out.txt","w",stdout);
    int t, ca=1;
    scanf("%d", &t);
    while(t--){
        int n;
        scanf("%d",&n);
        string str;
        getline(cin, str);
        ddd.clear();
        int cnt = 2;
        for(int i = 0; i < n; i++){
            getline(cin, str);
            istringstream is(str);
            string t;
            int arr[2000], larr = 0;
            while(is >> t){
                map<string, int>::iterator it = ddd.find(t);
                if(it == ddd.end())
                    ddd[t] = cnt++;
                arr[larr++] = ddd[t];
            }
            sort(arr, arr + larr);
            larr = unique(arr, arr + larr) - arr;
            
            zz[i].clear();
            for(int j = 0; j < larr; j++){
                zz[i].push_back(arr[j]);
            }
        }
        printf("Case #%d: ", ca++);
        int src = 0, sink = 1;
        wwwww.pre(cnt + n, src, sink);
        wwwww.Add(src, cnt, INF);
        wwwww.Add(cnt + 1, sink, INF);
        
        for(int i = 0; i < n; i++)
            for(int j = 0; j < (int)zz[i].size(); j++)
            {
                wwwww.Add(cnt + i, zz[i][j], 1);
                wwwww.Add(zz[i][j], cnt + i , 1);
            }
        wwwww.SSSPA();
        printf("%d\n", wwwww.maxFlow);
    }
    return 0;
}