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
#define biton(mask, bit) (mask | (((uint64)(1)) << bit))
#define bitoff(mask, bit) (mask & (~(((uint64)(1)) << bit)))
#define bitputon(mask, bit) (mask |= (((uint64)(1)) << bit))
#define bitputoff(mask, bit) (mask &= (~(((uint64)(1)) << bit)))
#define FAIL() (*((int*)(0)))++
#define INF ((int)(1e9) + 1337)
#define LINF ((int64)(1e18))
#define EPS (1e-14)
#define PI (3.1415926535897932384626433832795)
#define y1 yy1
#define y0 yy0
#define j0 jj0
#define MOD 1000000007LL
#define HMOD 1234567913LL
#define HBASE 1000009

//#define HMOD ((int64)(1e18) + 3LL)
//#ifdef _MY_DEBUG
//#define HMOD 1000000007
//#endii
#define MAX 2000000000
mt19937 ggen;

#define BMOD (10000000LL)
#define BSZ (7)

struct bigint
{
    vector<int64> d;
    int64 stub;
    bigint()
    {
        stub = 0;
        d.assign(1, 0);
    }
    bigint(int a)
    {
        stub = 0;
        d.assign(1, a);
    }
    int64& operator[](int k)
    {
        if (k >= d.size())
        {
            stub = 0;
            return stub;
        }
        else
            return d[k];
    }

    int64 operator[](int k) const
    {
        if (k >= d.size())
            return 0;
        else
            return d[k];
    }

    int size() const
    {
        return d.size();
    }

    void norm()
    {
        while (d.back() == 0 && d.size() > 1)
            d.pop_back();
    }
};

bigint operator+(const bigint &a, const bigint &b)
{
    bigint res;
    res.d.assign(max(a.size(), b.size()) + 2, 0);
    int64 ost = 0;
    for (int i = 0; i < res.size(); i++)
    {
        res[i] = ost + a[i] + b[i];
        ost = res[i] / BMOD;
        res[i] %= BMOD;
    }
    res.norm();
    return res;
}

bigint operator*(const bigint &a, int64 b)
{
    bigint res;
    res.d.assign(a.size() + 2, 0);
    int64 ost = 0;
    for (int i = 0; i < res.size(); i++)
    {
        res[i] = a[i] * b + ost;
        ost = res[i] / BMOD;
        res[i] %= BMOD;
    }
    res.norm();
    return res;
}

void init_from_str(bigint &a, const char s[], int base)
{
    a = 0;
    for (int i = 0; s[i] != 0; i++)
        a = a * base + (s[i] - '0');
}

bool is_divisible(const bigint &a, int64 b)
{
    bigint res;
    res.d.assign(a.size() + 2, 0);
    int64 ost = 0;
    for (int i = a.size() - 1; i >= 0; i--)
    {
        res[i] = ost * BMOD + a[i];
        ost = res[i] % b;
        res[i] /= b;
    }
    res.norm();
    return (ost == 0);
}

int n;
char s[50];
int dv[50];

void sinc()
{
    for (int i = 0; i < n; i++)
    {
        s[i]++;
        if (s[i] == '2')
            s[i] = '0';
        else
            break;
    }
}

inline int find_div(bigint &d)
{
    for (int i = 2; i < 1000; i++)
    {
        if (is_divisible(d, i))
            return i;
    }
    return -1;
}

void solve()
{
    int j;
    scanf("%*d%d%d", &n, &j);
    s[0] = '1';
    for (int i = 1; i < n - 1; i++)
        s[i] = '0';
    s[n - 1] = '1';
    s[n] = 0;
    int ctr = 0;
    printf("Case #1:\n");
    bigint a;
    while (ctr != j)
    {
        bool fail = false;
        for (int i = 2; i <= 10 && !fail; i++)
        {
            init_from_str(a, s, i);
            dv[i] = find_div(a);
            if (dv[i] == -1)
                fail = true;
        }
        if (!fail)
        {
            printf("%s ", s);
            for (int i = 2; i <= 10; i++)
                printf("%d ", dv[i]);
            printf("\n");
            ctr++;
        }
        sinc();
        sinc();
    }
}

int main()
{
    //stresstest(50, 100, 70); return 0;
    //testgen(6);// return 0;
    //ios_base::sync_with_stdio(false); cin.tie(0);
#ifdef _MY_DEBUG
    freopen("input.txt", "rt", stdin); freopen("output.txt", "wt", stdout);
#else
    //freopen(TASK ".in", "rt", stdin); freopen(TASK ".out", "wt", stdout);
#endif
    //stresstest(); return 0;
    srand(1313);
    ggen = mt19937(13);

    //init();
    solve();

    return 0;
}