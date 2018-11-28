#include "iostream"
#include "algorithm"
#include "vector"
#include "set"
#include "map"
#include "cstring"
#include "string"
#include "vector"
#include "cassert"
#include "queue"
#include "cstdio"
#include "cstdlib"
#include "ctime"
#include "cmath"
#include "bitset"

using namespace std;

typedef long long ll;
typedef pair < ll, ll > ii;

const int N = 1000 + 5;

int n;
int x[N], y[N], z[N];
bool h[N];
double dist[N];

double sq(double x) {
    return x * x;
}

double d(int i, int j) {
    return sqrt(sq(x[i] - x[j]) + sq(y[i] - y[j]) + sq(z[i] - z[j]));
}

void solve() {
    int grb;
    scanf("%d %d", &n, &grb);
    for(int i = 1; i <= n; i++) {
        scanf("%d %d %d %d %d %d", x + i, y + i, z + i, &grb, &grb, &grb);
    }
    memset(h, 0, sizeof(h));
    for(int i = 2; i <= n; i++)
        dist[i] = 1e20;
    int x = 1;
    for(int it = 0; it < n - 1; it++) {
        h[x] = 1;
        for(int i = 1; i <= n; i++)
            if(!h[i])
                dist[i] = min(dist[i], max(dist[x], d(x, i)));
        int mn = -1;
        for(int i = 1; i <= n; i++)
            if(!h[i] and (mn == -1 or dist[i] < dist[mn]))
                mn = i;
        x = mn;
    }
    printf("%.12lf\n", dist[2]);
}

int main () {
    
    freopen("in.txt", "r", stdin);
    freopen("small.txt", "w", stdout);
    
    int tt;
    
    scanf("%d", &tt);
    
    for(int t = 1; t <= tt; t++) {
        printf("Case #%d: ", t);
        solve();
    }
    
    return 0;
    
}