#include <bits/stdc++.h>

typedef long long ll;
using namespace std;

void mod(ll &a, ll b)
{
    a %= b;
    if(a < 0) a += b;
}

#define all(x) x.begin(), x.end()
#define f(i,a,b) for(int i = (a); i <= (b); i++)
#define fd(i,a,b) for(int i = (a); i >= (b); i--)
#define mp make_pair
#define faster_io() ios_base::sync_with_stdio(false)
#define pb push_back
#define pii pair<int,int>
#define SZ(x) ((int)x.size())
#define vii vector<pair<int,int>>

const int INF = 1000000005;
const ll INFLL = 1000000000000000002ll;
const ll MOD = 1000000007;

// ----------------------------------------------------------------------------------------------------------

struct NetworkFlowWithCost
{
    struct edge
    {
        int a,b,cap,cost;
        edge(int p1, int p2, int p3, int p4) : a(p1), b(p2), cap(p3), cost(p4) {};
    };

    const int INF = 2147483647;
    int s, t;
    vector<edge> edges;
    vector<int> best, from;
    vector<vector<int>> e;

    NetworkFlowWithCost(int sz)
    {
        best.resize(sz+1);
        e.resize(sz+1);
        from.resize(sz+1);
    }

    void setSource(int n){s=n;}
    void setSink(int n) {t=n;}

    void addEdge(int a, int b, int _cap, int _cost)
    {
        edges.pb(edge(a,b,_cap,_cost));
        e[a].pb(SZ(edges)-1);
        edges.pb(edge(b,a,0,-_cost));
        e[b].pb(SZ(edges)-1);
    }

    bool dijkstra()
    {
        fill(all(best),INF);
        priority_queue<pii,vii,greater<pii>> q;
        best[s] = 0, q.push({0,s});

        while(!q.empty())
        {
            pii p = q.top();
            q.pop();

            int n = p.second, c = p.first;
            if(best[n] < c) continue;
            if(n == t) return true;

            for(int idx : e[n])
            {
                edge &ed = edges[idx];
                if(ed.cap && c + ed.cost < best[ed.b])
                {
                    best[ed.b] = c + ed.cost;
                    from[ed.b] = idx;
                    q.push({best[ed.b],ed.b});
                }
            }
        }

        return best[t] < INF;
    }

    pii minCostMaxFlow()
    {
        int c = 0, f = 0;

        while(dijkstra())
        {
            int ff = INF, n = t, prev = c;

            while(n != s)
            {
                edge &ed = edges[from[n]];
                c += ed.cost;
                ff = min(ff, ed.cap);
                n = ed.a;
            }

            f += ff;
            n = t;

            while(n != s)
            {
                edge &ed = edges[from[n]];
                edge &rev = from[n]%2 ? edges[from[n]-1] : edges[from[n]+1];
                ed.cap -= ff, rev.cap += ff;
                n = ed.a;
            }
        }

        return {f,c};
    }
};

ifstream fin("A2.txt");
ofstream fout("A.out");

char B[105][105];
int T, H, W;

int left(int i, int j)
{
    return (i-1)*W+j;
}

int right(int i, int j)
{
    return 10000 + (i-1)*W + j;
}

int main()
{
    fin >> T;
    f(testie,1,T)
    {
        fin >> H >> W;
        f(i,1,H)
        {
            string s;
            fin >> s;
            f(j,1,W) B[i][j] = s[j-1];
        }

        int arrows = 0, s = 20002, t = 20003;
        NetworkFlowWithCost g(20005);
        g.setSource(s), g.setSink(t);

        f(i,1,H) f(j,1,W) if(B[i][j] != '.')
        {
            arrows++;

            g.addEdge(s,left(i,j),1,0);
            g.addEdge(right(i,j),t,999999,0);

            fd(j2,j-1,1) if(B[i][j2] != '.')
            {
                int c = B[i][j] == '<' ? 0 : 1;
                g.addEdge(left(i,j),right(i,j2),1,c);
                //if(testie == 5) cout << "Adding " << left(i,j) << "->" << right(i,j2) << " with cost " << c << "\n";
                break;
            }
            f(j2,j+1,W) if(B[i][j2] != '.')
            {
                int c = B[i][j] == '>' ? 0 : 1;
                g.addEdge(left(i,j),right(i,j2),1,c);
                //if(testie == 5) cout << "Adding " << left(i,j) << "->" << right(i,j2) << " with cost " << c << "\n";
                break;
            }
            fd(i2,i-1,1) if(B[i2][j] != '.')
            {
                int c = B[i][j] == '^' ? 0 : 1;
                g.addEdge(left(i,j),right(i2,j),1,c);
                //if(testie == 5) cout << "Adding " << left(i,j) << "->" << right(i2,j) << " with cost " << c << "\n";
                break;
            }
            f(i2,i+1,H) if(B[i2][j] != '.')
            {
                int c = B[i][j] == 'v' ? 0 : 1;
                g.addEdge(left(i,j),right(i2,j),1,c);
                //if(testie == 5) cout << "Adding " << left(i,j) << "->" << right(i2,j) << " with cost " << c << "\n";
                break;
            }
        }

        pii p = g.minCostMaxFlow();
        //if(testie == 5) cout << "Cost is " << p.second << "\n";
        if(p.first != arrows) fout << "Case #" << testie << ": IMPOSSIBLE\n";
        else fout << "Case #" << testie << ": " << p.second << "\n";
    }
}
