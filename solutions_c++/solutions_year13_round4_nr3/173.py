#include <iostream>
#include <sstream>

#include <vector>
#include <set>
#include <bitset>
#include <map>
#include <string>

#include <cstdio>
#include <cmath>
#include <cstring>
#include <cstdlib>
#include <cassert>
#include <ctime>

#include <algorithm>
#include <numeric>

#define foreach(i, x) for (__typeof((x).begin()) i = (x).begin(); i != (x).end(); ++i)
#define sqr(x) ((x) * (x))
#define len(x) ((int) (x).size())
#define all(x) (x).begin(), (x).end()
#define pb push_back
#define pbk pop_back
#define mp make_pair
#define fs first
#define sc second
#define endl '\n'
#ifdef CUTEBMAING
#include "cutedebug.h"
#else
#define debug(x) ({})
#endif

using namespace std;

typedef long long int64;
typedef unsigned long long lint;
typedef long double ld;

const int inf = ((1 << 30) - 1);
const int64 linf = ((1ll << 62) - 1);
const int maxn = 21;

int n;
int a[maxn], b[maxn];
bool u[maxn];
int res[maxn];

inline bool good(int x){
    int val = 1;
    for (int i = 0; i < x; i++)
        if (res[i] < res[x] && val < a[i] + 1){
            val = a[i] + 1;
            if (val > a[x])
                return false;
        }
    return val == a[x];
}

inline bool check(){
    for (int i = n - 1; i >= 0; i--){
        int val = 1;
        for (int j = i + 1; j < n; j++)
            if (res[i] > res[j] && val < b[j] + 1){
                val = b[j] + 1;
                if (val > b[i])
                    return false;
            }
        if (val != b[i])
            return false;
    }
    return true;
}

int s[maxn][maxn];

inline bool make(int x){
    if (x == n)
        return check();
    for (int i = 0; i < n; i++){
        if (!u[i]){
            res[x] = i;
            if (!good(x))
                continue;
            u[i] = true, res[x] = i;
            if (make(x + 1))
                return true;
            u[i] = false;
        }
    }
    return false;
}

const int cmax = 100500;

int dp1[cmax], dp2[cmax];

inline bool coolCheck(){
    fill_n(dp1, n, 1);
    fill_n(dp2, n, 1);
    for (int i = 0; i < n; i++)
        for (int j = 0; j < i; j++)
            if (res[j] < res[i])
                dp1[i] = max(dp1[i], dp1[j] + 1);
    for (int i = n - 1; i >= 0; i--)
        for (int j = i + 1; j < n; j++)
            if (res[j] < res[i])
                dp2[i] = max(dp2[i], dp2[j] + 1);
    for (int i = 0; i < n; i++)
        if (a[i] != dp1[i] || b[i] != dp2[i])
            return false;
    return true;
}

void run(){
    assert(scanf("%d", &n));
    for (int i = 0; i < n; i++){
        for (int j = 0; j < n; j++)
            s[i][j] = j;
        //random_shuffle(s[i], s[i] + n);
    }
    for (int i = 0; i < n; i++)
        assert(scanf("%d", &a[i]));
    for (int i = 0; i < n; i++)
        assert(scanf("%d", &b[i]));
    memset(u, 0, sizeof(u));
    assert(make(0));
    assert(coolCheck());
    for (int i = 0; i < n; i++)
        printf("%d%c", res[i] + 1, " \n"[i == n - 1]);
}

int main(){
    #if defined CUTEBMAING && !defined STRESS
    assert(freopen("input.txt", "r", stdin));
    assert(freopen("output.txt", "w", stdout));
    #endif
    srand(-1);
    int t; assert(scanf("%d", &t));
    for (int i = 0; i < t; i++){
        double begin = clock();
        printf("Case #%d: ", i + 1);
        run();
        fprintf(stderr, "%d OK!\n", i);
        fprintf(stderr, "Time: %.5f\n", (clock() - begin) / CLOCKS_PER_SEC);
        fflush(stdout);
    }
    return 0;
}
