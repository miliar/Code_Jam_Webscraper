#pragma comment (linker, "/STACK:256000000")

#define _USE_MATH_DEFINES
#define _CRT_NO_DEPRECEATE
#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <iomanip>
#include <fstream>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <cstring>
#include <vector>
#include <utility>
#include <algorithm>
#include <functional>
#include <set>
#include <unordered_set>
#include <map>
#include <unordered_map>
#include <cmath>
#include <queue>
#include <memory.h>
#include <sstream>
#include <cassert>
#include <ctime>
#include <complex>
#include <random>

using namespace std;

typedef unsigned int uint32;
typedef long long int64;
typedef unsigned long long uint64;
typedef long double ldouble;
typedef pair<int, int> pii;
typedef pair<int64, int64> pll;
typedef pair<pii, pii> piiii;

#define pb push_back
#define sq(x) ((x)*(x))
#define tmin(x,y,z) (min(min((x),(y)),(z)))
#define rand32() (((unsigned int)(rand()) << 16) | (unsigned int)(rand()))
#define rand64() (((unsigned int64)(rand32()) << 16) | (unsigned int64)(rand32()))
#define bit(mask, b) ((mask >> b) & 1)
#define biton(mask, bit) (mask | (((uint32)(1)) << bit))
#define bitoff(mask, bit) (mask & (~(((uint32)(1)) << bit)))
#define bitputon(mask, bit) (mask |= (((uint32)(1)) << bit))
#define bitputoff(mask, bit) (mask &= (~(((uint32)(1)) << bit)))
#define FAIL() (*((int*)(0)))++
#define INF ((int)(1e9) + 1337)
#define LINF ((int64)(1e18))
#define EPS 1e-9
#define PI (3.1415926535897932384626433832795)
#define y1 yy1
#define y0 yy0
#define j0 jj0
#define MOD 1000000007LL
#define HMOD 1234567913LL
#define HBASE 1000003

//#define HMOD ((int64)(1e18) + 3LL)
//#ifdef _MY_DEBUG
//#define HMOD 1000000007
//#endif
#define MAX 2000000000
mt19937 ggen;

int n, k;
double p[1000][2];
int btc[100000];

void precalc()
{
    for (int i = 0; i < 100000; i++)
    {
        int ti = i;
        while (ti)
        {
            btc[i]++;
            ti &= (ti - 1);
        }
    }
}

void init()
{
    cin >> n >> k;
    for (int i = 0; i < n; i++)
    {
        cin >> p[i][1];
        p[i][0] = 1.0 - p[i][1];
    }
}

double trivia()
{
    double res = 0;
    int k2 = k / 2;
    for (int i = 0; i < (1 << n); i++)
    {
        if (btc[i] != k)
            continue;
        double ires = 0;
        for (int j = i; j != 0; j = (j - 1) & i)
        {
            if (btc[j] != k2)
                continue;
            double tres = 1;
            int mask = i;
            int mask2 = j;
            for (int ii = 0; ii < n; ii++)
            {
                if (mask & 1)
                {
                    tres *= p[ii][mask2 & 1];
                }
                mask >>= 1;
                mask2 >>= 1;
            }
            ires += tres;
        }
        res = max(res, ires);
    }
    return res;
}

double solve()
{
    return 0;
}

void testgen(int n)
{
    ofstream ofs("input.txt", ios_base::out | ios_base::trunc);
    mt19937 gen(1337);
    vector<pii> res;
    for (int i = 0; i <= (1 << n); i++)
        for (int j = 0; j <= (1 << n) - i; j++)
            res.push_back(pii(i, j));
    ofs << res.size() << '\n';
    for (int i = 0; i < (int)res.size(); i++)
        ofs << n << ' ' << res[i].first << ' ' << res[i].second << ' ' << (1 << n) - res[i].first - res[i].second << '\n';
}

#define TASK "substr"
int main()
{
    //testgen(1);// return 0;
    ios_base::sync_with_stdio(false); cin.tie(0);
#ifdef _MY_DEBUG
    freopen("input.txt", "rt", stdin); freopen("output.txt", "wt", stdout);
#else
    //freopen(TASK ".in", "rt", stdin); freopen(TASK ".out", "wt", stdout);
#endif
    //stresstest(10); return 0;
    srand(1313);
    ggen = mt19937(13);

    precalc();
    int ts;
    cin >> ts;
    cout.precision(15);
    for (int i = 0; i < ts; i++)
    {
        cout << "Case #" << i + 1 << ": ";
        init();
        cout << fixed << trivia();
        cout << '\n';
    }

    return 0;
}