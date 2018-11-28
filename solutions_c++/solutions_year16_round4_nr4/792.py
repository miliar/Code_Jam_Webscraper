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
#define GET(x) (mark[x>>5]>>(x&31)&1)
#define SET(x) (mark[x>>5]|=1<<(x&31))
#define maxL (10000000>>5)+1
#define mod 1000000007
typedef long long ll;
using namespace std;

char in[5][5];
int use[5];
int n;
int p[5];

int ch(int now) {
    if (now == n) {
        return 1;
    }
    int i,j, k;
    int flag = 0;
    rep(i, n) {
        if (!use[i] && in[p[now]][i] == '1') {
            flag = 1;
            use[i] = 1;
            if (!ch(now+1)) { return 0; }
            use[i] = 0;
        }
    }
    return flag;
}

int check() {
    for (int i = 0; i < n; i++) p[i]=i;
    memset(use, 0, sizeof(use));
    do {
        if (!ch(0)) return 0;
    } while (next_permutation(p, p+n));
    return 1;
}

int go(int x, int y, int now) {
    if (!now) { return check(); }
    int i, j, k;
    xrep(i, y+1, n) {
        if (in[x][i] == '1') continue;
        in[x][i] = '1';
        if (go(x, i, now-1)) { return 1; }
        in[x][i] = '0';
    }
    xrep(i, x+1, n) {
        rep(j, n) {
            if (in[i][j] == '1') continue;
            in[i][j] = '1';
            if (go(i, j, now-1)) { return 1; }
            in[i][j] = '0';
        }
    }
    return 0;
}

int check_add(int now) {
    return go(0, -1, now);
}

int main() {
    int t, tt, i, j, k;

    memset(use, 0, sizeof(use));
    cin >> tt;
    xrep(t, 1, tt+1) {
        cin >> n;
        rep(i, n) { cin >> in[i]; }
        rep(i, 10000) {
            if (check_add(i)) {
                cout << "Case #" << t << ": " << i << endl;
                break;
            }
        }
    }
}
