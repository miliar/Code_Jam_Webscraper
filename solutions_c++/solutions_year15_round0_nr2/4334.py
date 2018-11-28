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
const int N = 2000;
int f[N][N], dp[N][N];
int n;
const int lim = 100;
int main()
{
    int CA;
    REP(i, 0, lim) f[i][0] = i;
    REP(i, 0, lim) REP(j, 1, lim) {
        f[i][j] = i;
        REP(k, 1, i - 1) REP(p, 0, j - 1) getmin(f[i][j], max(f[k][p], f[i - k][j - 1- p]));
    }
    read(CA);
    REP(T, 1, CA) {
        read(n);
        int ans = N;
        dp[0][0] = 0;
        REP(i, 1, n) {
            int x;
            read(x);
            REP(j, 0, lim) {
                dp[i][j] = N;
                REP(k, 0, j) getmin(dp[i][j], max(dp[i - 1][j - k], f[x][k]));
            }
        }
        REP(i, 0, lim) getmin(ans, dp[n][i] + i);
        printf("Case #%d: ", T);
        printf("%d\n", ans);
    }
    return 0;
}


