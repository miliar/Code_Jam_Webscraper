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
#include <map>
#include <cmath>
#include <queue>
#include <memory.h>
#include <sstream>
#include <cassert>
#include <ctime>
#include <complex>
//#include <random>

using namespace std;

typedef unsigned int uint32;
typedef long long int64;
typedef unsigned long long uint64;
typedef long double ldouble;
typedef pair<int, int> pii;
typedef pair<int64, int64> pll;
typedef pair<pii, pii> piiii;
typedef pair<int64, int> pli;

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
#define EPS (1e-14)
#define y1 yy1
#define y0 yy0
#define j0 jj0

//#define HMOD (1000000000000000003LL)
//#ifdef _MY_DEBUG
//#define HMOD 1000000007
//#endif
//#define HBASE 524287

//mt19937 ggen;

bool u[10];

void solve(int64 n)
{
    if (n == 0)
    {
        cout << "INSOMNIA";
        return;
    }
    int ctr = 0;
    memset(u, 0, sizeof u);
    for (int64 i = n; ; i += n)
    {
        int64 ti = i;
        while (ti)
        {
            int d = ti % 10;
            ti /= 10;
            if (!u[d])
            {
                u[d] = 1;
                ctr++;
            }
        }
        if (ctr == 10)
        {
            cout << i;
            break;
        }
    }
}

void testgen(int n)
{
    ofstream ofs("input.txt", ios_base::out);
    ofs << n << '\n';
    for (int i = 0; i < n; i++)
        ofs << i << '\n';
    ofs.close();
}

int main()
{
    //testgen(10);
    //ios_base::sync_with_stdio(false); cin.tie(0);
#ifdef _MY_DEBUG
    freopen("input.txt", "rt", stdin); freopen("output.txt", "wt", stdout);
#else
    //freopen(TASK ".in", "rt", stdin); freopen(TASK ".out", "wt", stdout);
#endif
    srand(1313);

    int ts;
    cin >> ts;
    for (int i = 0; i < ts; i++)
    {
        int64 n;
        cin >> n;
        cout << "Case #" << i + 1 << ": ";
        solve(n);
        cout << '\n';
    }

    return 0;
}