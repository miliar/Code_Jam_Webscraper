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

int n, r, p, s;
char g[256][256];

void init()
{
    cin >> n >> r >> p >> s;
    g['P']['R'] = 1;
    g['R']['S'] = 1;
    g['S']['P'] = 1;
}

bool tournament(string res)
{
    string nres = "";
    for (int i = 0; i < (int)res.size(); i += 2)
    {
        if (res[i] == res[i + 1])
            return false;
        else if (g[res[i]][res[i + 1]])
            nres += res[i];
        else
            nres += res[i + 1];
    }
    if (nres.size() != 1)
        return tournament(nres);
    return true;
}

string trivia()
{
    string res = "";
    for (int i = 0; i < p; i++)
        res += 'P';
    for (int i = 0; i < r; i++)
        res += 'R';
    for (int i = 0; i < s; i++)
        res += 'S';
    do
    {
        if (tournament(res))
        {
            return res;
        }
    } while (next_permutation(res.begin(), res.end()));
    return "IMPOSSIBLE";
}

int val[15][10000];

string solve()
{
    string base[3] = { "P", "R", "S" };
    string tbase[3];
    for (int i = 0; i < n; i++)
    {
        sort(base, base + 3);
        tbase[0] = base[0] + base[1];
        tbase[1] = base[1] + base[2];
        tbase[2] = base[0] + base[2];
        for (int j = 0; j < 3; j++)
            base[j] = tbase[j];
    }
    for (int i = 0; i < 3; i++)
    {
        int tr = 0, tp = 0, ts = 0;
        for (int j = 0; j < (int)base[i].size(); j++)
        {
            if (base[i][j] == 'R')
                tr++;
            if (base[i][j] == 'P')
                tp++;
            if (base[i][j] == 'S')
                ts++;
        }
        if (tr == r && tp == p && ts == s)
            return base[i];
    }
    return "IMPOSSIBLE";
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

    int ts;
    cin >> ts;
    for (int i = 0; i < ts; i++)
    {
        cout << "Case #" << i + 1 << ": ";
        init();
        cout << solve();
        cout << '\n';
    }

    return 0;
}