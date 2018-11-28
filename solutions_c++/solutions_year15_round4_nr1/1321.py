#include <iostream>
#include <cassert>
#include <cstdio>
#include <map>
#include <vector>
#include <deque>
#include <queue>
#include <stack>
#include <set>
#include <cstring>
#include <cstdlib>
#include <cctype>
#include <sstream>
#include <fstream>
#include <string>
#include <cmath>
#include <algorithm>
#define REP(i, a, b) for (int i = (a); i <= (b); ++i)
#define PER(i, a, b) for (int i = (a); i >= (b); --i)
#define RVC(i, c) fot (int i = 0; i < (c).size(); ++i)
#define RSQ(i, a, b) for (int i = (a); 1LL * i * i <= (LL)(b); ++i)
#define RED(k, u) for (int k = head[(u)]; k; k = edge[k].next)
#define REE(k, u, h) for (int k = h[(u)]; k; k = edge[k].next)
#define lowbit(x) ((x) & (-(x)))
#define CL(x, v) memset(x, v, sizeof x)
#define ITER(ta, tb) ta<tb>::iterator
#define RCN(k, ta, tb, a) for (ITER(ta, tb) k = a.begin(); k != a.end(); ++k)
#define PLM(x, a, c) x = ((x + (a) % (c)) % (c))
#define MLM(x, a, c) x = (((x - (a) % (c)) % (c) + (c)) % (c))
#define MUM(x, a, c) x = (x * ((a) % (c))) % (c)
#define MP make_pair
#define PB push_back
#define FR first
#define SC second
#define SZ size()
#define rank rankk
#define next nextt
#define link linkk
#define index indexx
#define abs(x) ((x) > 0 ? (x) : (-(x)))
#define FILEIN(s)\
	FILENAME = s;\
	freopen((FILENAME + ".in").c_str(), "r", stdin);
#define FILEOUT(s)\
	FILENAME = s;\
	freopen((FILENAME + ".out").c_str(), "w", stdout);
#define FILEIO(s)\
	FILENAME = s;\
	freopen((FILENAME + ".in").c_str(), "r", stdin);\
	freopen((FILENAME + ".out").c_str(), "w", stdout);

using namespace std;
string FILENAME;
typedef long long LL;
typedef pair<int, int> PII;
typedef pair<PII, int> PIII;
typedef pair<LL, int> PLI;
typedef pair<LL, int> PLL;
typedef pair<int, LL> PIL;
typedef pair<int, string> PIS;
typedef pair<string, int> PSI;
typedef pair<double, int> PDI;
typedef pair<int, double> PID;
typedef pair<double, double> PDD;


template<class T> inline
void getmin(T &a, const T &b)
{
	if (b < a) a = b;
}

template<class T> inline
void getmax(T &a, const T &b)
{
	if (b > a) a = b;
}

template<class T> inline
void read(T &a)
{
    char c;
    while (isspace(c = getchar()));
    bool flag = 0;
    if (c == '-') flag = 1, a = 0;
    else a = c - 48;
    while (isdigit(c = getchar())) a = a * 10 + c - 48;
    if (flag) a = -a;
}
#define OPTIM __attribute__((optimize("-O2")))
/*======================= TEMPLATE =======================*/

const int N = 200;
int a[N][N];
int dirx[] = {0, -1, 1, 0, 0};
int diry[] = {0, 0, 0, -1, 1};
int n, m;
bool pd(int x, int y)
{
    return x <= n && x > 0 && y > 0 && y <= m;
}
bool run(int x, int y, int d)
{
    while (pd(x, y)) {
        x += dirx[d];
        y += diry[d];
        if (a[x][y]) return 1;
    }
    return 0;
}
int check(int x, int y, int d)
{
    if (run(x, y, d)) return 0;
    REP(i, 1, 4) if (i != d && run(x, y, i)) return 1;
    return -1;
}
int main()
{
    int T = 0;
    cin >> T;
    REP(ca, 1, T) {
        cin >> n >> m;
        CL(a, 0);
        REP(i, 1, n) REP(j, 1, m) {
            char c;
            while(isspace(c = getchar()));
            if (c == '^') a[i][j] = 1;
            if (c == 'v') a[i][j] = 2;
            if (c == '<') a[i][j] = 3;
            if (c == '>') a[i][j] = 4;
        }
        int ans = 0;
        REP(i, 1, n) REP(j, 1, m) if (a[i][j]){
            int x = check(i, j, a[i][j]);
            if (x == -1) {ans = -1; break;}
            ans += x;
        }
        if (ans != -1)
        cout <<"Case #"<<ca<<": "<<ans <<endl;
        else
        cout <<"Case #"<<ca<<": IMPOSSIBLE"<<endl;
    }
}
