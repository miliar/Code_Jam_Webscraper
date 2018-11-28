#include <cstdio>
#include <cstring>
#include <cmath>
#include <iostream>
#include <algorithm>
#include <vector>
#include <set>

using namespace std;

#define push_back pb
#define make_pair mp

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> pii;

#define MAXN 1010
int a[MAXN];
int n, tc, best;

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    scanf("%i", &tc);
    for(int tt=1; tt<=tc; ++tt) {
        scanf("%i", &n);
        for(int i=0; i<n; ++i) scanf("%i", &a[i]);

        best = MAXN;
        for(int k=1; k<=MAXN; ++k) {
            int tmp = 0;
            for(int i=0; i<n; ++i) {
                tmp += (a[i] - 1) / k;
            }
            best = min(best, tmp + k);
        }    
        printf("Case #%i: %i\n", tt, best);
    }
    return 0;
}