#include <bits/stdc++.h>

#define FO(i,a,b) for (int i = (a); i < (b); i++)
#define sz(v) int(v.size())

using namespace std;

typedef long double ld;

int n, k;
ld p[205];

ld c[205];
int cc;

bool seen[205][205];
ld cache[205][205];

ld dp(int i, int ny) {
    if (i == k) {
        return ny == k/2 ? 1 : 0;
    } else if (seen[i][ny]) {
        return cache[i][ny];
    } else {
        seen[i][ny] = true;
        return cache[i][ny] = dp(i+1, ny) * (1-c[i]) + dp(i+1, ny+1) * c[i];
    }
}

int main() {
    int T; scanf("%d", &T);
    FO(Z,1,T+1) {
        scanf("%d %d", &n, &k);
        FO(i,0,n) scanf(" %Lf", p+i);
        sort(p,p+n);

        ld ans = 0;
        FO(i,0,k+1) {
            cc = 0;
            FO(j,0,i) c[cc++] = p[j];
            FO(j,0,k-i) c[cc++] = p[n-1-j];

            memset(seen, 0, sizeof seen);

            ld res = dp(0,0);
            ans = max(ans,res);
        }
        printf("Case #%d: %.10Lf\n", Z, ans);
        fflush(stdout);
    }
}

