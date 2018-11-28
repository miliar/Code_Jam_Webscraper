#include <cstdio>
#include <vector>
#include <stack>
#include <map>
using namespace std;

class Building
{
public:
    int x0, y0, x1, y1;
    
    Building(int x0, int y0, int x1, int y1)
    {
        this->x0 = x0;
        this->y0 = y0;
        this->x1 = x1;
        this->y1 = y1;
    }
};

int w, h, b;
vector<Building> hise;

vector<vector<pair<int, int> > > sos; // graph

bool grid[100][500];

void fill(bool g[100][500], Building b, bool val)
{
    for (int i=b.x0; i<=b.x1; i++)
        for (int j=b.y0; j<=b.y1; j++)
        {
            g[i][j] = val;
        }
}

int dx[] = {0, 1, 0, -1};
int dy[] = {1, 0, -1, 0};

bool path_exists(int s, int t, vector<int> &p)
{
    stack<int> q;
    map<int, bool> seen;
    map<int, int> parent;
    bool koniec = false;
    int u, v;
    
    p.clear();
    while (!q.empty()) q.pop();
    seen.clear();
    seen[s] = true;
    
    parent[s] = -666;
    q.push(s);
    while (!q.empty())
    {
        int u = q.top(); q.pop();
        for (int i=0; i<sos[u].size(); i++)
        {
            v = sos[u][i].first;
            if (seen[v]) continue;
            seen[v] = true;
            q.push(v);
            parent[v] = u;
            if (v == t) { koniec = true; break; }
        }
        if (koniec) break;
    }
    
    if (!koniec) return false;
    
    while (t != -666)
    {
        p.push_back(t);
        t = parent[t];
    }
    
    return true;
}

int max_flow()
{
    int flow = 0;
    vector <int> p;
    int u, v;
    
    while (path_exists(2*w*h, 2*w*h+1, p))
    {
        // Augment
        // p is in contra direction
        /*
         * for (int i=0; i<p.size(); i++)
        {
            printf("%d ", p[i]);
        }
        printf("\n\n");
        */
        
        for (int i=p.size()-1; i>0; i--)
        {
            // remove edge p[i] --> p[i-1]
            u = p[i];
            v = p[i-1];
            for (int i=0; i<sos[u].size(); i++)
            {
                if (sos[u][i].first == v)
                {
                    sos[u].erase(sos[u].begin()+i);
                    break;
                }
            }
        }
        for (int i=0; i<p.size()-1; i++)
        {
            // add edge p[i] --> p[i+1]
            u = p[i];
            v = p[i+1];
            sos[u].push_back(make_pair(v, 1));
        }
        flow++;
        
    }
    
    return flow;
}

int solve()
{
    for (int i=0; i<w; i++)
        for (int j=0; j<h; j++)
        {
            grid[i][j] = true;
        }
    for (int i=0; i<hise.size(); i++)
    {
        fill(grid, hise[i], false);
    }
    
    // Debug
    /*
    for (int i=h-1; i>=0; i--)
    {
        for (int j=0; j<w; j++)
        {
            printf("%d", grid[j][i]);
        }
        printf("\n");
    }
    */
    
    // Make graph
    // Incoming vertices are labelled: x + w * y
    // Outgoing vertices are labelled: w*h + x + w * y
    
    // incoming: 0 .. w*h-1, outgoing: w*h .. 2*w*h-1
    sos.clear();
    for (int i=0; i<w*h; i++) sos.push_back(vector<pair<int, int> >());
    for (int i=0; i<w*h; i++) sos.push_back(vector<pair<int, int> >());
    sos.push_back(vector<pair<int, int> >());
    sos.push_back(vector<pair<int, int> >());
    // Add edges
    int i2, j2;
    int u, v;
    for (int i=0; i<w; i++)
    {
        for (int j=0; j<h; j++)
        {
            u = w * h + i + w * j;
            v = i + w * j;
            sos[v].push_back(make_pair(u, 1));
            for (int k=0; k<4; k++)
            {
                i2 = i + dx[k];
                j2 = j + dy[k];
                if ((i2 < 0) || (j2 < 0)) continue;
                if ((i2 >= w) || (j2 >= h)) continue;
                if (!grid[i2][j2]) continue;
                // u=(i, j) -> v=(i2, j2)    
                v = i2 + w * j2;
                sos[u].push_back(make_pair(v, 1));
            }
        }
    }
    // Source (2*w*h) and sink (2*w*h+1)
    for (int i=0; i<w; i++)
    {
        if (!grid[i][0]) continue;
        v = i;
        sos[2*w*h].push_back(make_pair(v, 1));
    }
    for (int i=0; i<w; i++)
    {
        if (!grid[i][h-1]) continue;
        u = w*h + i + w * (h-1);
        sos[u].push_back(make_pair(2*w*h+1, 1));
    }
    //printf("%d %d\n", 2*w*h, 2*w*h+1);
    
    return max_flow();
}

int main()
{
    int t;
    int x0, y0, x1, y1;
        
    scanf("%d", &t);
    for (int test_case=1; test_case<=t; test_case++)
    {
        scanf("%d %d %d", &w, &h, &b);
        hise.clear();
        for (int i=1; i<=b; i++)
        {
            scanf("%d %d %d %d", &x0, &y0, &x1, &y1);
            hise.push_back(Building(x0, y0, x1, y1));
        }
        printf("Case #%d: %d\n", test_case, solve());
    }
    return 0;
}
