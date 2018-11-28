#include<bits/stdc++.h>
#define two(a) (1<<(a))
#define LINF (1ll<<61)
#define EPS (1e-14)
#define Lshift(a,b) (a<<b)
#define Rshift(a,b) (a>>b)
#define rep(a,b) for(a=0 ; a<b ; a++)
#define xrep(a,b,c) for(a=b ; a<c ; a++)
#define INF (1<<29)
#define swap(a,b) ( (a^=b) , (b^=a) , (a^=b) )
#define min(a,b) ( a < b ? a : b )
#define max(a,b) ( a > b ? a : b )
#define GET(x) (mark[x>>5]>>(x&31)&1)
#define SET(x) (mark[x>>5]|=1<<(x&31))
#define maxL (10000000>>5)+1
#define mod 1000000007
typedef long long ll;
using namespace std;

char in[150][150];
int dir[4][2]={0, 1, 0, -1, 1, 0, -1, 0};
int r, c;

int go(int x, int y, int ind) {
    int i, j;
    for (i = x+dir[ind][0], j=y+dir[ind][1]; i >=0 && i < r && j >= 0 && j < c; i+=dir[ind][0], j+=dir[ind][1]) {
        if (in[i][j] != '.') {
            return 1;
        }
    }
    return 0;
}

int find_path(int i, int j) {
    char now = in[i][j];
    int ii;
    if (now == '>') {
        if (go(i, j, 0)) { return 0; }
        rep(ii, 4) {
            if (go(i, j, ii)) { return 1; }
        }
        return -1;
    }
    if (now == '<') {
        if (go(i, j, 1)) { return 0; }
        rep(ii, 4) {
            if (go(i, j, ii)) { return 1; }
        }
        return -1;
    }
    if (now == '^') {
        if (go(i, j, 3)) { return 0; }
        rep(ii, 4) {
            if (go(i, j, ii)) { return 1; }
        }
        return -1;
    }
    if (now == 'v') {
        if (go(i, j, 2)) { return 0; }
        rep(ii, 4) {
            if (go(i, j, ii)) { return 1; }
        }
        return -1;
    }

}

int main() {
    int t, tt, i, j, k;
    int ans, temp;
    char x;

    cin >> tt;
    for (t = 1; t <= tt; t++) {
        ans = 0;
        cin >> r >> c;
        rep(i, r) rep(j, c) { cin >> in[i][j]; }
        rep(i, r) {
            rep(j, c) {
                if (in[i][j] != '.') {
                    temp = find_path(i, j);
                    if (temp == -1) {
                        break;
                    }
                    else ans += temp;
                }
            }
            if (j < c) break;
        }
        if (i < r) cout << "Case #" << t << ": IMPOSSIBLE" << endl;
        else cout << "Case #" << t << ": " << ans << endl;

    }
}
