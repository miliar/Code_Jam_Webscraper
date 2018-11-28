#define _USE_MATH_DEFINES

#ifdef ONLINE_JUDGE
#define FINPUT(file) 0
#define FOUTPUT(file) 0
#else
#define FINPUT(file) freopen(file,"r",stdin)
#define FOUTPUT(file) freopen(file,"w",stdout)
#endif

#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <set>
#include <stack>
#include <string>
#include <map>
#include <vector>
#include <queue>
#include <algorithm>
#include <functional>
#include <bitset>

typedef long long ll;
typedef long double ld;
static const int N = 1010;
static const int M = 19;
static const int LEN = 210;
static const int MAX = 0x7fffffff;
static const int GMAX = 0x3f3f3f3f;
static const ll LGMAX = 0x3f3f3f3f3f3f3f3f;
static const int MIN = ~MAX;
static const double EPS = 1e-9;
static const ll BASE = 1000000007;
static const int CH = 27;


int main()
{
    FINPUT("in.txt");
    FOUTPUT("out.txt");

    int t;
    while (scanf("%d", &t) != EOF) {
        for (int i = 0; i < t; ++i) {
            int d;
            int p[N];

            scanf("%d", &d);
            int max = MIN;
            for (int i = 0; i < d; ++i) {
                scanf("%d", &p[i]);
                max = std::max(max, p[i]);
            }

            int ncount = MAX;
            for (int i = 1; i <= max; ++i) {
                int tmp = 0;
                for (int j = 0; j < d; ++j) {
                    if (p[j] > tmp)
                        tmp += (p[j] - 1) / i;
                }
                tmp += i;
                ncount = std::min(tmp, ncount);
            }
            printf("Case #%d: %d\n", i + 1, ncount);
        }
    }

    return 0;
}
