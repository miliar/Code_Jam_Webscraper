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
static const int N = 10;
static const int M = 10010;
static const int LEN = 210;
static const int MAX = 0x7fffffff;
static const int GMAX = 0x3f3f3f3f;
static const ll LGMAX = 0x3f3f3f3f3f3f3f3f;
static const int MIN = ~MAX;
static const double EPS = 1e-9;
static const ll BASE = 1000000007;
static const int CH = 27;

int mm[M][M];
int trans[5][5] = { {1, 'i', 'j', 'k'}, {'i', -1, 'k', -'j'},
    {'j', -'k', -1, 'i'}, {'k', 'j', -'i', -1}
};
char str[M];
int hash[250];

void inline update(int& n1, int& n2)
{
    if (n1 < 0) {
        n1 = -n1;
        n2 = -n2;
    }
}

void init(int len)
{
    for (int i = 0; i < len; ++i) {
        int mul_one = 1;
        int tmp = 1;
        for (int j = i; j < len; ++j) {
            tmp = trans[hash[tmp]][hash[str[j]]];
            update(tmp, mul_one);
            mm[i][j] = tmp * mul_one;
        }
    }
}

bool solve(int len, int period)
{
    char str_main[M];
    int st = 0;
    for (int i = 0; i < period; ++i) {
        for (int j = 0; j < len; ++j) {
            str_main[st++] = str[j];
        }
    }
    str_main[st] = '\0';

    for (int i = 0; i < period * len; ++i) {
        int mul_one = 1;
        int tmp = 1;
        for (int j = i; j < period * len; ++j) {
            tmp = trans[hash[tmp]][hash[str_main[j]]];
            update(tmp, mul_one);
            mm[i][j] = tmp * mul_one;
        }
    }

    int mul1 = 1;
    int tmp1 = 1;
    for (int i = 0; i < period * len; ++i) {
        tmp1 = trans[hash[tmp1]][hash[str_main[i]]];
        update(tmp1, mul1);
        if (tmp1 * mul1 == 'i') {
            int mul2 = 1;
            int tmp2 = 1;
            for (int j = i + 1; j < period * len; ++j) {
                tmp2 = trans[hash[tmp2]][hash[str_main[j]]];
                update(tmp2, mul2);
                if (tmp2 * mul2 == 'j') {
                    int k = j + 1;
                    if (k <= period * len - 1) {
                        if (mm[k][period * len - 1] == 'k') {
                            return true;
                        }
                    }
                }
            }
        }
    }

    return false;
}


int main()
{
    FINPUT("in.txt");
    FOUTPUT("out.txt");

    hash[1] = 0;
    hash['i'] = 1;
    hash['j'] = 2;
    hash['k'] = 3;
    int t;
    while (scanf("%d", &t) != EOF) {
        for (int i = 0; i < t; ++i) {
            int x, l;
            scanf("%d %d", &x, &l);
            scanf("%s", str);

            printf("Case #%d: %s\n", i + 1, solve(x, l) == true? "YES" : "NO");
        }
    }

    return 0;
}
