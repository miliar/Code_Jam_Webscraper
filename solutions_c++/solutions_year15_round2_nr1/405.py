#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <numeric>
#include <complex>

using namespace std;

typedef long long ll;

#define mp make_pair
#define pb push_back
#define PI 3.1415926535897932384626433832795
typedef pair<int, int>  pii;
typedef vector<int>     vi;
typedef vector< pii >   vpii;

#define MAXN 10000000

int f[MAXN];
int o[MAXN];
int n, tail, head, next;

int rev(int x) {
    int res = 0;
    while (x != 0) {
        res = res * 10 + x % 10;
        x = x / 10;
    }
    return res;
}

int main() {
    int tc;

    memset(f, 0xff, sizeof(f));
    f[1] = 1;
    o[0] = 1;
    tail = head = 0;

    while (tail <= head) {
        int x = o[tail++];

        next = x + 1;
        if (next < MAXN) {
            if (f[next] < 0) {
                f[next] = f[x] + 1;
                o[++head] = next;
            }
        }
        next = rev(x);
        if (next < MAXN) {
            if (f[next] < 0) {
                f[next] = f[x] + 1;
                o[++head] = next;
            }
        }
    }
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-small-attempt0.out", "w", stdout);
    scanf("%i", &tc);
    for(int tt=1; tt<=tc; ++tt) {
        scanf("%i", &n);
        printf("Case #%i: %i\n", tt, f[n]);
    }
    return 0;
}