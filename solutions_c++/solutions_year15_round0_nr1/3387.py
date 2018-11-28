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

int n; char s[100100];

int main()
{
    freopen("d:\\A-large.in", "r", stdin);
    freopen("d:\\a.out", "w", stdout);
    int oo;
    scanf("%d", &oo);
    for(int o = 0; o < oo; o++)
    {
        scanf("%d", &n);
        scanf("%s", &s);
        n++;
        int res = 0;
        int sum = 0;
        for(int i = 0; i < n; i++)
        {
            sum += s[i] - '0';
            if(sum < i + 1)
                res++, sum++;
        }
        printf("Case #%d: %d\n", o + 1, res);
    }
}
