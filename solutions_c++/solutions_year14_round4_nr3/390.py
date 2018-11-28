#include <bits/stdc++.h>
#include <ext/rope>
#define clr(x) memset((x), 0, sizeof(x))
#define all(x) (x).begin(), (x).end()
#define pb push_back
#define mp make_pair
#define For(i, st, en) for(int i=(st); i<=(int)(en); i++)
#define Ford(i, st, en) for(int i=(st); i>=(int)(en); i--)
#define forn(i, n) for(int i=0; i<(int)(n); i++)
#define ford(i, n) for(int i=(n)-1; i>=0; i--)
#define fori(it, x) for (__typeof((x).begin()) it = (x).begin(); it != (x).end(); it++)
#define in(x) int (x); input((x));
#define x first
#define y second
#define less(a,b) ((a) < (b) - EPS)
#define more(a,b) ((a) > (b) + EPS)
#define eq(a,b) (fabs((a) - (b)) < EPS)
#define remax(a, b) ((a) = (b) > (a) ? (b) : (a))
#define remin(a, b) ((a) = (b) < (a) ? (b) : (a))

using namespace std;

using namespace __gnu_cxx;

template <typename T>
T gcd(T a, T b) {
    while (b > 0) {
        a %= b;
        swap(a, b);
    }
    return a;
}
typedef long double ld; template <class _T> inline _T sqr(const _T& x) {return x * x;} template <class _T> inline string tostr(const _T& a) {ostringstream os(""); os << a; return os.str();} const ld PI = 3.1415926535897932384626433832795L; const double EPS = 1e-9; char TEMPORARY_CHAR; typedef long long ll; typedef unsigned long long ull; typedef set < int > SI; typedef vector < int > VI; typedef vector < vector < int > > VVI; typedef map < string, int > MSI; typedef pair < int, int > PII; const int INF = 1e9; inline void input(int &a) {a = 0; while (((TEMPORARY_CHAR = getchar()) > '9' || TEMPORARY_CHAR < '0') && (TEMPORARY_CHAR != '-')){} char neg = 0; if (TEMPORARY_CHAR == '-') {neg = 1; TEMPORARY_CHAR = getchar();} while (TEMPORARY_CHAR <= '9' && TEMPORARY_CHAR >= '0') {a = 10 * a + TEMPORARY_CHAR - '0'; TEMPORARY_CHAR = getchar();} if (neg) a = -a;} inline void out(long long a) {if (!a) putchar('0'); if (a < 0) {putchar('-'); a = -a;} char s[20]; int i; for(i = 0; a; ++i) {s[i] = '0' + a % 10; a /= 10;} ford(j, i) putchar(s[j]);} inline int nxt() {in(ret); return ret;}

class Solution {
public:
    Solution(string problemName) {
        freopen((problemName + ".in").c_str(), "r", stdin);
        freopen((problemName + ".out").c_str(), "w", stdout);
    }

    void solveAllTestCases() {
        cin >> testNumber;
        for (int test = 1; test <= testNumber; ++test) {
            cout << "Case #" << test << ": ";
            solveOneTestCase();
        }
    }

private:
    int testNumber;
    void solveOneTestCase();
};


void print(vector <int> a) {
    for (int v : a) {
        cout << v << " ";
    }
}


vector <int> read(int n) {
    vector <int> res(n);
    for (int i = 0; i < n; ++i) {
        cin >> res[i];
    }
    return res;
}

const int MAXN = 2 * 1000 * 1000 + 2;        // ����� ������

struct edge {
    int a, b, cap, flow;
};

int n, s, t, d[MAXN], ptr[MAXN], q[MAXN];
vector<edge> e;
vector<int> g[MAXN];

void add_edge (int a, int b, int cap)
{
    edge e1 = { a, b, cap, 0 };
    edge e2 = { b, a, 0, 0 };
    g[a].push_back ((int) e.size());
    e.push_back (e1);
    g[b].push_back ((int) e.size());
    e.push_back (e2);
}

bool bfs()
{
    int qh=0, qt=0;
    q[qt++] = s;
    memset (d, 255, n * sizeof(int));
    d[s] = 0;
    while (qh < qt && d[t] == -1)
    {
        int v = q[qh++];
        for (size_t i=0; i<g[v].size(); ++i)
        {
            int id = g[v][i],
                to = e[id].b;
            if (d[to] == -1 && e[id].flow < e[id].cap)
            {
                q[qt++] = to;
                d[to] = d[v] + 1;
            }
        }
    }
    return d[t] != -1;
}

int dfs (int v, int flow)
{
    if (!flow)  return 0;
    if (v == t)  return flow;
    for (; ptr[v]<(int)g[v].size(); ++ptr[v])
    {
        int id = g[v][ptr[v]],
            to = e[id].b;

        if (d[to] != d[v] + 1)  continue;

        int pushed = dfs (to, min (flow, e[id].cap - e[id].flow));
        if (pushed)
        {
            e[id].flow += pushed;
            e[id^1].flow -= pushed;
            return pushed;
        }
    }
    return 0;
}

int dinic()
{
    int flow = 0;
    while(1)
    {
        if (!bfs())  break;
        memset(ptr, 0, n * sizeof(int));
        while (int pushed = dfs (s, INF))
            flow += pushed;
    }
    return flow;
}

int dx[] = {-1, 1, 0, 0};
int dy[] = {0, 0, -1, 1};

void Solution::solveOneTestCase() {
    in(w); in(h); in(b);
    char used[w][h];
    clr(used);
    for (int i = 0; i < b; ++i) {
        int x1 = nxt(), y1 = nxt();
        int x2 = nxt(), y2 = nxt();
        if (x1 > x2) {
            swap(x1, x2);
        }
        if (y1 > y2) {
            swap(y1, y2);
        }
        for (int j = x1; j <= x2; ++j) {
            for (int k = y1; k <= y2; ++k) {
                used[j][k] = 1;
            }
        }
    }
    n = w * h * 2 + 2;
    for (int i = 0; i < n; ++i) {
        g[i].clear();
    }
    s = n - 2;
    t = n - 1;
    e.clear();
    for (int i = 0; i < w; ++i) {
        for (int j = 0; j < h; ++j) {
            if (used[i][j]) continue;
            if (j == 0) {
                add_edge(s, 2 * (i * h + j), 1);
            }
            if (j == h - 1) {
                add_edge(2 * (i * h + j) + 1, t, 1);
            }
            add_edge(2 * (i * h + j), 2 * (i * h + j) + 1, 1);
            for (int k = 0; k < 4; ++k) {
                int x = i + dx[k];
                int y = j + dy[k];
                if (x >= w || x < 0 || y >= h || y < 0 || used[x][y]) {
                    continue;
                }
                add_edge(2 * (i * h + j) + 1, 2 * (x * h + y), 1);
            }
        }
    }
    cout << dinic() << endl;
}


int main()
{
#ifdef LOCAL
    //freopen ("in.txt", "r", stdin);
    //freopen ("out.txt", "w", stdout);
#else
    //freopen("trie.in", "r", stdin);
    //freopen("trie.out", "w", stdout);
#endif
    Solution solution("C-small0");
    solution.solveAllTestCases();
    //ios_base::sync_with_stdio(false);

    return 0;
}
