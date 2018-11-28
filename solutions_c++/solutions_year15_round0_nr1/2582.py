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
            int smax;
            char audience[N];
            scanf("%d %s", &smax, audience);

            int sum = 0;
            int add = 0;
            for (int j = 0; j < smax + 1; ++j) {
                if (audience[j] == '0')
                    continue;

                if (j > sum) {
                    add += j - sum;
                    sum = j;
                }
                sum += audience[j] - '0';
            }

            printf("Case #%d: %d\n", i + 1, add);
        }
    }

    return 0;
}
