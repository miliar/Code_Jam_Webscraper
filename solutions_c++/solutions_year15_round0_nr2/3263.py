#include <algorithm>
#include <bitset>
#include <complex>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <limits>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
#include <cassert>
#include <cctype>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <math.h>

#define FR(i, a, b)   for(int i = a; i < b; i++)
#define FOR(i, a, b)  for(int i = a; i <= b; i++)
#define LFOR(i, a, b) for(int i = a; i >= b; i--)
#define FRSZ(i, x)    for(int i = 0; i < (int)x.size(); i++)
#define RP(i, n)      for(int i = 0; i < n; i++)
#define repeat        do
#define until(x)      while(!(x))
#define _ve vector
#define _pa pair
#define _tu tuple
#define _mp make_pair
#define _mt make_tuple
#define _pb push_back
#define _fi first
#define _sc second
#define sz(a) ((int)(a).size())

using namespace std;

template <class T> T min3(T a, T b, T c){ return min(a, min(b, c));};
template <class T> T max3(T a, T b, T c){ return max(a, max(b, c));};

typedef long long int64;
typedef unsigned long long qword;
typedef long double ldouble;

void openFile(){freopen("/home/khaihanhdk/devplace/a.inp", "r", stdin);}

int a[100100];

int main()
{
    freopen("d:\\B-large.in", "r", stdin);
    freopen("d:\\a.out", "w", stdout);
    int oo;
    scanf("%d", &oo);
    for(int o = 0; o < oo; o++)
    {
        int n;
        scanf("%d", &n);
        for(int i = 0; i < n; i++)
            scanf("%d", &a[i]);
        int res = 1000000000;
        for(int i = 1; i <= 1000; i++)
        {
            int rr = 0;
            for(int j = 0; j < n; j++)
            {
                int k;
                if(a[j] % i == 0)
                    k = a[j] / i;
                else k = a[j] / i + 1;
                rr += k - 1;
            }
            res = min(res, i + rr);
        }
        printf("Case #%d: %d\n", o + 1, res);
    }
}
