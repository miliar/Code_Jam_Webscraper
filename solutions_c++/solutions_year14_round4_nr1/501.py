#ifdef DEBUG_OUTPUT
#include "debug_output.h"
#else
#define PRINT(x)
#define PRINT_CONT(x)
#define PRINT_MSG(x)
#endif

#include <iostream>
#include <cmath>
#include <vector>
#include <string>
#include <cstring>
#include <sstream>
#include <algorithm>
#include <memory.h>
#include <set>
#include <map>
#include <cstdio>
#include <cassert>
using namespace std;


// Enlarge MSVS stack size
#pragma comment(linker, "/STACK:16777216")

#define pb push_back
#define all(c) c.begin(), c.end()
#define mp(x, y) make_pair(x, y)
#define sz(x) static_cast<int>(x.size())
typedef long long int64;

template<class T> T sqr(const T& t) {return t * t;}
template<class T> T abs(const T& t) {return ((t > 0) ? (t) : (-t));}

void initialize()
{
    freopen("large.in", "r", stdin);
    freopen("large.out", "w", stdout);
}

int main()
{
    initialize();

    int T;
    cin >>T;
    for (int tt = 1; tt <= T; ++tt) {
        int n, S;
        cin >> n >> S;

        vector<int> size;
        for (int i = 0; i < n; ++i) {
            int num;
            cin >>num;
            size.pb(num);
        }
        sort(all(size));

        int res = 0;
        int l = 0, r = n - 1;
        while (l <= r) {
            res += 1;
            if (size[r] + size[l] <= S) {
                l += 1;
            }
            r -= 1;
        }

        cout << "Case #" << tt << ": " << res << endl;
    }
    
    return 0;
}
