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
typedef long double ld;

int r, c;
bool g[16][16];

int dx[] = {-1, 1, 0, 0};
int dy[] = {0, 0, -1, 1};

bool valid(int x, int y) {
    if (x<0 || y<0) return false;
    if (x>=r || y >=c) return false;
    return true;
}

int score() {
    int x, y, ret=0;
    FOR(i,0,r) FOR(j,0,c) {
        if (!g[i][j]) continue;
        FOR(k,0,4) {
            x = i+dx[k];
            y = j+dy[k];
            if (valid(x,y) && g[x][y]) ret++;
        }
    }
    return ret;
}

int main() {
    freopen("B-small-attempt1.in", "r", stdin);
    freopen("B-small-attempt1.out", "w", stdout);

    int T;
    int rc, n, ans;
    int p[16];

    scanf("%d", &T);
    for(int ncase=1; ncase<=T; ncase++) {
        scanf("%d%d%d", &r, &c, &n); rc = r*c;
        /*if (n <= rc/2) {
            printf("Case #%d: 0\n", ncase);
            continue;
        }*/

        ans = INF;
        FOR(i,0,rc) p[i] = 1;
        FOR(i,0,rc-n) p[i] = 0;
        do {
            memset(g, false, sizeof(g));
            FOR(i,0,rc) if (p[i]) g[ i/c ][ i%c ] = true;

            /*FOR(i,0,rc) printf("%d ", p[i]); putchar(10);
            FOR(i,0,r) {
                FOR(j,0,c) printf("%d ", g[i][j]);
                printf("\n");
            } printf("%d\n\n", score()); system("pause");*/

            ans = min(ans, score());
        } while(next_permutation(p, p+rc));

        printf("Case #%d: %d\n", ncase, ans/2);
    }

    return 0;
}
