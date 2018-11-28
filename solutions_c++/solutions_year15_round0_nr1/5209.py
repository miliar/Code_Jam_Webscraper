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
int a[N];
int main()
{
    int n, T;
    cin >> T;
    REP(ca, 1, T) {
        printf("Case #%d: ", ca);
        read(n);
        REP(i, 0, n) {
            char c;
            while (isspace(c = getchar()));
            a[i] = c - '0';
        }
        int sum = 0, ans = 0;
        REP(i, 0, n) {
            if (sum < i) getmax(ans, i - sum);
            sum += a[i];
        }
        printf("%d\n", ans);
    }
    return 0;
}
