#include <cstdio>
#include <algorithm>

using namespace std;

#define MAXN 110
int a[MAXN][MAXN];
int h[MAXN];
int v[MAXN];
int x, y;

int main() {
    int tc;
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);

    scanf("%i", &tc);
    for(int tt=1; tt<=tc; ++tt) {
        scanf("%i %i", &y, &x);
        for(int i=0; i<y; ++i) 
            for(int j=0; j<x; ++j) scanf("%i", &a[i][j]);

        for(int i=0; i<y; ++i) {
            h[i] = a[i][0];
            for(int j=0; j<x; ++j) h[i] = max(h[i], a[i][j]);
        }

        for(int j=0; j<x; ++j) {
            v[j] = a[0][j];
            for(int i=0; i<y; ++i) v[j] = max(v[j], a[i][j]);
        }

        bool ok = true;
        for(int i=0; i<y; ++i)
            for(int j=0; j<x; ++j) ok = ok && a[i][j] == min(h[i], v[j]);

        printf("Case #%i: ", tt);
        if (ok) printf("YES\n"); else printf("NO\n");
    }

}