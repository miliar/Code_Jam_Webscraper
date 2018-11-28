#pragma comment(linker, "/STACK:1677721600")
#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <stack>
#include <vector>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <climits>
#include <cassert>
#include <iostream>
#include <algorithm>
#define pb push_back
#define mp make_pair
#define LL long long
#define lson lo,mi,rt<<1
#define rson mi+1,hi,rt<<1|1
#define Min(a,b) ((a)<(b)?(a):(b))
#define Max(a,b) ((a)>(b)?(a):(b))
#define mem(a,b) memset(a,b,sizeof(a))
#define FIN freopen("in.in", "r", stdin)
#define FOUT freopen("C-small-attempt6.out", "w", stdout)
#define rep(i,a,b) for(int i=(a); i<=(b); i++)
#define dec(i,a,b) for(int i=(a); i>=(b); i--)

using namespace std;
const int mod = 1e9 + 7;
const double eps = 1e-8;
const double ee = exp(1.0);
const int maxn = 1e6 + 10;
const double pi = acos(-1.0);

int readT()
{
    char c;
    int ret = 0,flg = 0;
    while(c = getchar(), (c < '0' || c > '9') && c != '-');
    if(c == '-') flg = 1; else ret = c ^ 48;
    while( c = getchar(), c >= '0' && c <= '9') ret = ret * 10 + (c ^ 48);
    return flg ? - ret : ret;
}

LL readTL()
{
    char c;
    int flg = 0;
    LL ret = 0;
    while(c = getchar(), (c < '0' || c > '9') && c != '-');
    if(c == '-') flg = 1; else ret = c ^ 48;
    while( c = getchar(), c >= '0' && c <= '9') ret = ret * 10 + (c ^ 48);
    return flg ? - ret : ret;
}

const int Times = 10;
LL multi(LL a, LL b, LL m)
{
    LL ans = 0;
    a %= m;
    while(b)
    {
        if(b & 1)
        {
            ans = (ans + a) % m;
            b--;
        }
        b >>= 1;
        a = (a + a) % m;
    }
    return ans;
}

LL quick_mod(LL a, LL b, LL m)
{
    LL ans = 1;
    a %= m;
    while(b)
    {
        if(b & 1)
        {
            ans = multi(ans, a, m);
            b--;
        }
        b >>= 1;
        a = multi(a, a, m);
    }
    return ans;
}

bool Miller_Rabin(LL n)
{
    if(n == 2) return true;
    if(n < 2 || !(n & 1)) return false;
    LL m = n - 1;
    int k = 0;
    while((m & 1) == 0)
    {
        k++;
        m >>= 1;
    }
    for(int i=0; i<Times; i++)
    {
        LL a = rand() % (n - 1) + 1;
        LL x = quick_mod(a, m, n);
        LL y = 0;
        for(int j=0; j<k; j++)
        {
            y = multi(x, x, n);
            if(y == 1 && x != 1 && x != n - 1) return false;
            x = y;
        }
        if(y != 1) return false;
    }
    return true;
}

int N, J;
int binum[50];

LL trans(int base)
{
    LL res = 0;
    rep(i, 1, N)
    {
        res = res * base + binum[i];
    }
    return res;
}

int get_divs(LL x)
{
    int sx = sqrt(x);
    for (int i = 2; i < sx; ++i)
    {
        if (x % i == 0)
        {
            return i;
        }
    }
}

void dfs(int dep)
{
    if (J <= 0)
    {
        return ;
    }
    if (dep == 1)
    {
        bool flg = true;
        int divs[20];
        mem(divs, 0);
        rep(i, 2, 10)
        {
            LL t = trans(i);
//            cout << t << " prime:"  << Miller_Rabin(t) << "  ";
                if (Miller_Rabin(t))
                {
                    flg = false;
                    break;
                }
            divs[i] = get_divs(t);
        }

//        puts("");
        if (flg)
        {
            rep(i, 1, N)
            {
                printf("%d", binum[i]);
            }
            rep(i, 2, 10)
            {
                printf(" %d", divs[i]);
            }
            J--;
            puts("");
        }
        return ;
    }
    binum[dep] = 0;
    dfs(dep - 1);
    binum[dep] = 1;
    dfs(dep - 1);
}

int main()
{
    #ifdef LOCAL
    FIN;
    FOUT;
    #endif // LOCAL
    int ca = 1;
    int ncase;
    cin >> ncase;
    while (ncase--)
    {
//        N = readT();
//        J = readT();
        cin >> N >> J;
        mem(binum, 0);
        binum[1] = 1;
        binum[N] = 1;
        printf("Case #%d:\n", ca++);
        dfs(N - 1);
    }
    return 0;
}
