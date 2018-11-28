/*
 * Author: stormdpzh
 * Created Time:  Saturday, April 13, 2013 PM02:15:23 HKT
 * File Name: b.cpp
 */
#include <iostream>
#include <cstdio>
#include <sstream>
#include <cstring>
#include <string>
#include <cmath>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <list>
#include <algorithm>
#include <functional>

#define sz(v) ((int)(v).size())
#define rep(i, n) for(int i = 0; i < n; i++)
#define repf(i, a, b) for(int i = a; i <= b; i++)
#define repd(i, a, b) for(int i = a; i >= b; i--)
#define out(n) printf("%d\n", n)
#define mset(a, b) memset(a, b, sizeof(a))
#define lint long long

using namespace std;

const int INF = 1 << 30;
const int MaxN = 105;

int in[MaxN][MaxN];
int tmp[MaxN][MaxN];
bool did[MaxN];
int n, m;

bool gao()
{
    repf(i, 1, n) {
        int maxv = -1;
        repf(j, 1, m) maxv = max(maxv, in[i][j]);
        repf(j, 1, m) tmp[i][j] = maxv;
    }
    mset(did, false);
    repf(i, 1, n) {
        repf(j, 1, m) {
            if(tmp[i][j] > in[i][j]) {
                if(did[j]) return false;
                did[j] = true;
                repf(k, 1, n) tmp[k][j] = in[i][j];
            }
        }
    }
    repf(i, 1, n) repf(j, 1, m) {
        if(tmp[i][j] != in[i][j])
            return false;
    }
    return true;
}

int main()
{
    int t;
    scanf("%d", &t);
//    freopen("b.out", "w", stdout);
    repf(i, 1, t) {
        scanf("%d%d", &n, &m);
        repf(j, 1, n) repf(k, 1, m) scanf("%d", &in[j][k]);
        printf("Case #%d: ", i);
        if(gao()) puts("YES");
        else puts("NO");
    }
    return 0;
}

