#define _USE_MATH_DEFINES
#define _CRT_SECURE_NO_DEPRECATE
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <sstream>
#include <string>
#include <map>
#include <set>
#include <algorithm>
#include <iomanip>
#include <functional>
#include <bitset>
#include <cassert>
#include <cmath>
#include <ctime>
#include <queue>
#include <list>
#include <memory.h>
#include <complex>
#include <numeric>
using namespace std;
#pragma comment(linker, "/STACK:256000000")
#define mp make_pair
#define pb push_back
#define all(C) (C).begin(), (C).end()
#define sz(C) (int)(C).size()
#define PRIME 1103
#define PRIME1 31415
#define INF ((1ll << 30) - 1)
#define MOD 1000000007
#define FAIL ++*(int*)0
#define EPS 1e-8
template<class T> T sqr(T a) {return a * a;}
typedef long long int64;
typedef unsigned long long uint64;
typedef pair<int, int> pii;
typedef pair<int64, int64> pi64;
typedef pair<int, pii> piii;
typedef vector<int> vi;
typedef vector<int64> vi64;
typedef vector<vi64> vvi64;
typedef vector<pi64> vpi64;
typedef vector<vpi64 > vvpi64;
typedef vector<pii> vpii;
typedef vector<vector<int> > vvi;
typedef vector<vvi> vvvi;
typedef vector<vector<pair<int, int > > > vvpii;
typedef vector<vector<vector<pair<int, int > > > > vvvpii;
typedef complex<double> cd;
#define TASK "test"
//------------------------------------------------------------


int rec(vi p, int h)
{
    if(!h || !sz(p))
        return sz(p) ? INF : 0;

    sort(all(p));

    int res = INF;
    int k = p.back();

    if(k != 1)
    {
        p.pb(0);

        for(int i = 1; i < (k >> 1) + 1; ++i)
        {
            p[sz(p) - 2] = k - i;
            p.back() = i;

            res = min(res, rec(p, h - 1) + 1);
        }

        p.pop_back();

        // for(int i = 0; i < sz(p) - 1; ++i)
        // {
        //     for(int j = 1; j < k; ++j)
        //     {
        //         if(p[i] + j < k - 1)
        //         {
        //             p[i] += j;
        //             p.back() = k - j;
        //             res = min(res, rec(p, h - 1) + 1);
        //             p[i] -= j;
        //         }
        //     }
        // }

        p.back() = k;
    }

    for(int i = 0; i < sz(p); ++i)
        --p[i];

    reverse(all(p));

    while(sz(p) && !p.back())
        p.pop_back();

    res = min(res, rec(p, h - 1) + 1);

    return res;
}

int main()
{
#ifdef __APPLE__
    freopen(TASK ".in", "r", stdin);
    freopen(TASK ".out", "w", stdout);
#endif
    int t;
    cin >> t;

    for(int test = 0; test < t; ++test)
    {
        cerr << "test = " << test << endl;

        int d;
        scanf("%d", &d);
        vi p(d);

        for(int i = 0; i < d; ++i)
            scanf("%d", &p[i]);

        // int res = rec(p, 9);
        int res = rec(p, 9);

        // if(res != res1)
        // {
        //     cerr << "error" << endl;
        //     for(int i = 0; i < d; ++i)
        //         cerr << p[i] << " ";
        //     cerr << endl;
        //     cerr << "----------------" << endl;
        // }

        printf("Case #%d: %d\n", test + 1, res);
    }   

    return 0;
}







