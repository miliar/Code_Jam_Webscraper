#include <cstdio>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <string>
#include <memory.h>
#include <sstream>
#include <complex>
#include <cassert>

#define REP(i,n) for(int i = 0, _n = (n); i < _n; i++)
#define REPD(i,n) for(int i = (n) - 1; i >= 0; i--)
#define FOR(i,a,b) for (int i = (a), _b = (b); i <= _b; i++)
#define FORD(i,a,b) for (int i = (a), _b = (b); i >= _b; i--)
#define FORN(i,a,b) for(int i=a;i<b;i++)
#define FOREACH(it,c) for (__typeof((c).begin()) it=(c).begin();it!=(c).end();it++)
#define RESET(c,x) memset (c, x, sizeof (c))

#define PI acos(-1)
#define sqr(x) ((x) * (x))
#define PB push_back
#define MP make_pair
#define F first
#define S second
#define Aint(c) (c).begin(), (c).end()
#define SIZE(c) (c).size()

#define DEBUG(x) { cerr << #x << " = " << x << endl; }
#define PR(a,n) {cerr<<#a<<" = "; FOR(_,1,n) cerr << a[_] << ' '; cerr <<endl;}
#define PR0(a,n) {cerr<<#a<<" = ";REP(_,n) cerr << a[_] << ' '; cerr << endl;}
#define LL long long

using namespace std;

int n, k;

int main() {
    freopen("A-small-attempt0.in", "rb", stdin); freopen("a.out", "wb", stdout);
    int ntest;
    cin >> ntest;
    for (int test = 1; test <= ntest; test++) {
        printf("Case #%d: ", test);

        int firstAns, secondAns;
        int cnt[100];
        memset(cnt, 0, sizeof(cnt));

        cin >> firstAns;
        for (int i = 1; i <= 4; i++)
        for (int j = 1; j <= 4; j++) {
            int x;
            cin >> x;
            if (i == firstAns) cnt[x]++;
        }

        cin >> secondAns;
        for (int i = 1; i <= 4; i++)
        for (int j = 1; j <= 4; j++) {
            int x;
            cin >> x;
            if (i == secondAns) cnt[x]++;
        }

        int num = 0, res = -1;
        for (int i = 1; i <= 16; i++)
        if (cnt[i] == 2) {
            res = i;
            num ++;
        }

        if (num == 0) printf("Volunteer cheated!");
        else if (num > 1) printf("Bad magician!");
        else printf("%d", res);

        if (test < ntest) printf("\n");
    }

    return 0;
}
