#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <math.h>
#include <iostream>
#include <vector>
#include <stack>
#include <queue>
#include <algorithm>
#include <bitset>
#include <map>
#define FOR(i,k,n) for(int i=k; i<n; i++)
#define pb push_back
#define mp make_pair
#define EPS 1.0e-8
#define INF 1000000000

using namespace std;

typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef long long ll;

int n, m[1005];

bool isEnough(int x) {
    FOR(i,1,n) if (m[i-1] - m[i] > x) return false;
    return true;
}

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);

    int T;
    int ans1, ans2, ans3;
    int lo, hi, mid;

    scanf("%d", &T);
    for(int ncase=1; ncase<=T; ncase++) {
        scanf("%d", &n);
        FOR(i,0,n) scanf("%d", &m[i]);

        ans1 = 0;
        FOR(i,1,n) if (m[i] - m[i-1] < 0) ans1 += m[i-1] - m[i];

        lo = 0; hi = 10000;
        while(hi - lo > 1) {
            mid = (hi + lo) / 2;
            if (isEnough(mid)) hi = mid;
            else lo = mid;
        }
        if (isEnough(lo)) ans2 = lo;
        else ans2 = hi;

        ans3 = 0;
        FOR(i,0,n-1) ans3 += min(m[i], ans2);

        printf("Case #%d: %d %d\n", ncase, ans1, ans3);
    }

    return 0;
}
