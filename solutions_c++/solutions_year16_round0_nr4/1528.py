#include <cstdio>
#include <cassert>
#include <algorithm>
#include <vector>
#include <iostream>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <cstring>
#include <cstdlib>
#include <cmath>
#define For(i, n) for (ll i = 0; i < (ll) n; ++i)
#define SIZE(x) ((int) (x).size())
#define mp(a, b) make_pair(a, b)
using namespace std;

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;

#ifndef DG
#define DG 0
#endif
#define LOG(...) (DG ? fprintf(stderr, __VA_ARGS__) : 0)

int main(){
    int t;
    cin >> t;
    For(cases, t) {
        ll k, c, s;
        cin >> k >> c >> s;
        ll totlen = 1;
        For(i, c) totlen *= k;
        printf("Case #%lld:", cases + 1);
        if (c == 1) {
            if (k > s) printf(" IMPOSSIBLE\n");
            else {
                For(i, k) printf(" %lld", i+1);
                printf("\n");
            }
        }
        else {
            if (2*s < k) printf(" IMPOSSIBLE\n");
            else {
                ll bigoffset = 0, littleoffset = 2;
                For(i, k/2) {
                    printf(" %lld", bigoffset + littleoffset);
                    bigoffset += totlen / k * 2;
                    littleoffset += 2;
                }
                if (k % 2 == 1) printf(" %lld", totlen);
                printf("\n");
            }
        }
    }
}
