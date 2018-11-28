/*
	Time : 0610Z 20160409
	Task : Codejam 16 QR B
	Tags : idiot
	Stat : Coding
*/
#include <cstdio>
#include <cstring>
#include <iostream>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <utility>
#include <queue>
#include <functional>
#include <map>
#include <set>
#include <cmath>
#include <numeric>

#define fi first
#define se second
#define fo(i,a,b) for (int i = a; i <= b; i ++)
#define fd(i,a,b) for (int i = a; i >= b; i --)
#define fe(i,x,y) for (int i = x, y = lnk[i]; i; i = nxt[i], y = lnk[i])
#define mkp make_pair
#define pb push_back
#define Fill(x,y) memset(x,y,sizeof(x))
#define Cpy(x,y) memcpy(x,y,sizeof(x))
#define Bit(x,y) ((((x) >> (y)) & 1))
#define mit map<int,SI>::iterator
#define sit SI::iterator

using namespace std;
 
typedef long long LL;
typedef long double LD;
typedef pair <double, double> PD;
typedef pair <LL, LL> PLI;
typedef pair <PD, int> PDI;
typedef pair <int, int> PI;
typedef pair <int, PI> PII;
typedef pair <PI, PI> PIII;
typedef set <PI> SI;
typedef vector <int> VI;
typedef vector <PI> VII;
 
int Read()
{
    char c; while (c = getchar(), (c != '-') && (c < '0' || c > '9'));
    bool neg = (c == '-'); LL ret = (neg ? 0 : c - 48);
    while (c = getchar(), c >= '0' && c <= '9') ret = ret * 10 + c - 48;
    return neg ? -ret : ret;
}

const int LIM = 1000;

int N, M;
LL b[11], c[11];

int Findco(LL x)
{
    fo (i, 2, LIM)
        if (x % i == 0) return i;
    return 0;
}

void DFS(int d)
{
    if (d == N - 1)
    {
        fo (i, 2, 10) b[i] *= i, b[i] ++;
        bool ok = 1;
        fo (i, 2, 10)
            if (!(c[i] = Findco(b[i])))
            {
                ok = 0; break;
            }
        if (ok)
        {
            cout << b[10];
            fo (i, 2, 10) cout << " " << c[i];
            puts("");
            if ((-- M) == 0) exit(0);
        }
        fo (i, 2, 10) b[i] /= i;
        return;
    }
    fo (i, 2, 10) b[i] *= i;
    DFS(d + 1);
    fo (i, 2, 10) b[i] ++;
    DFS(d + 1);
    fo (i, 2, 10) b[i] /= i;
}

int main()
{
    freopen("c.in", "r", stdin), freopen("c.out", "w", stdout);
    int T;
    scanf("%d%d%d", &T, &N, &M);
    printf("Case #1:\n");
    fo (i, 2, 10) b[i] = 1;
    DFS(1);
    return 0;
}