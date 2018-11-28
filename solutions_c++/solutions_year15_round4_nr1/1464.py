#ifdef __clang__
#include "stdc++.h"
#else
#include <bits/stdc++.h>
#endif

using namespace std;

using LL    = long long;
using VI    = vector<int>;
using VII   = vector<vector<int>>;
using PII   = pair<int, int>;

const int INF  = numeric_limits<int>::max();
const LL  LINF = numeric_limits<long long>::max();

#define     FOR(a,b,c)      for(int a = b; a < c; ++a)
#define     REP(a,n)        FOR(a, 0, n)
#define     ITER(it, a)     for(auto it = a.begin(); it != a.end(); ++it)
#define     SET(a, v)       memset(a, v, sizeof(a))
#define     ALL(a)          a.begin(), a.end()
#define     P(v)            FOR(i, 0, v.size()) {cout << v[i] << " ";} cout << endl;
#define     SS              ({int x;scanf("%d",&x);x;})

int R, C;
vector<string> m;
int visited[102][102];
int wayout[102][102];

void get_didj(char c, int& di, int& dj)
{
    di = dj = 0;
    
    if (c == '^')
        di = -1;
    else if (c == '<')
        dj = -1;
    else if (c == '>')
        dj = 1;
    else if (c == 'v')
        di = 1;
}

void visit(int i, int j, int pi, int pj, int di, int dj)
{
    if (i < 0 || j < 0 || i >= R || j >= C)
    {
        wayout[pi][pj] = 1;
        return;
    }
    
    if (m[i][j] == '.')
    {
        visit(i + di, j + dj, pi, pj, di, dj);
    }
    else
    {
        if (visited[i][j])
            return;
        
        visited[i][j] = true;
        
        int new_di, new_dj;
        get_didj(m[i][j], new_di, new_dj);
        
        visit(i + new_di, j + new_dj, i, j, new_di, new_dj);
    }
}

void solve()
{
    R = SS, C = SS;

    m.clear();
    SET(visited, 0);
    SET(wayout, 0);

    REP(i, R)
    {
        string str;
        cin >> str;
        m.push_back(str);
    }
    
    bool invalid = false;
    
    REP(i, R)
    {
        REP(j, C)
        {
            if (m[i][j] != '.')
            {
                int cnt = 0;
                
                REP(k, R)
                {
                    if (k == i)
                        continue;
                    
                    cnt += (m[k][j] != '.');
                }
                
                REP(k, C)
                {
                    if (k == j)
                        continue;
                    
                    cnt += (m[i][k] != '.');
                }
                
                if (cnt == 0)
                    invalid = true;
            }
        }
    }
    
    if (invalid)
    {
        cout << "IMPOSSIBLE";
    }
    else
    {
        REP(i, R)
        {
            REP(j, C)
            {
                if (m[i][j] != '.')
                    visit(i, j, i, j, 0, 0);
            }
        }
        
        int ans = 0;
        
        REP(i, R)
        {
            REP(j, C)
            {
                ans += wayout[i][j];
            }
        }
        
        cout << ans;
    }
}

int main()
{
    FILE *fp = freopen("/Users/-RooneY-/Desktop/src/input", "r", stdin); assert(fp);
    FILE *fp2 = freopen("/Users/-RooneY-/Desktop/src/output", "w", stdout); assert(fp2);
    
    int t = SS;
    
    REP(i, t)
    {
        cout << "Case #" << i+1 << ": ";
        solve();
        cout << endl;
    }
    return 0;
}