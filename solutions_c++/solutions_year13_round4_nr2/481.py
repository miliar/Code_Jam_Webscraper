#include <cstdio>
#include <fstream>
#include <iostream>

#include <set>
#include <map>
#include <queue>
#include <deque>
#include <cmath>
#include <vector>
#include <bitset>
#include <string>
#include <cstring>
#include <algorithm>

#include <ctime>
#include <cstdlib>
#include <cassert>

#define pb push_back
#define mp make_pair
#define sz(A) (int) (A).size()

#define eprintf(...) fprintf(stderr, __VA_ARGS__)
#define eputs(A) fputs((A), stderr)

#define sqr(A) ((A) * (A))
#define x first
#define y second
  
using namespace std;

typedef long long LL;
typedef unsigned long long ULL;
typedef long double LD;
typedef pair <int, int> pii;

const int N = (int) 0;

int t, n;
LL p;

bool BestTest (LL val)
{
    LL cnt_lower = (((LL) 1) << n) - val - 1;
    LL res = 0;

    for (int i = 0; i < n; i++) {
        if (cnt_lower) {
            res = res << 1;                     
            cnt_lower--;            
        }
        else
            res = (res << 1) ^ 1;

        cnt_lower /= 2;
    }

    return res < p;
}

bool BedTest (LL val)
{
    LL res = 0;
    LL cnt_upper = val;

    for (int i = 0; i < n; i++) {
        if (cnt_upper) {
            cnt_upper--;
            res = (res << 1) ^ 1;
        }
        else
            res = res << 1;

        cnt_upper /= 2;
    }

    return res < p;
}

int main () 
{
    #ifdef DEBUG
    freopen(".in", "r", stdin);
    freopen(".out", "w", stdout);
    #endif

    scanf("%d", &t);
    for (int T = 0; T < t; T++) {
        cerr << T << endl;

        scanf("%d%I64d", &n, &p);
        printf("Case #%d: ", T + 1);
        LL l = 0, r = ((LL) 1) << (LL) n;
        while (l + 1 < r)
        {
            LL m = (l + r) / 2;
            if (BedTest(m))
                l = m;
            else
                r = m;
        }
        printf("%I64d ", l);

        l = 0, r = ((LL) 1) << n;
        while (l + 1 < r)
        {
            LL m = (l + r) / 2;
            if (BestTest(m))
                l = m;
            else
                r = m;                
        }

        printf("%I64d\n", l);
    }
    
    return 0; 
}

