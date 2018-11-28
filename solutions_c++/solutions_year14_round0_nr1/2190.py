#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
#include<cstdlib>
#include<algorithm>
using namespace std;

#define rep(i, s, t) for (int i = (s); i <= (t); ++i)
#define REP(i, n) rep(i, 1, n)
#define MOD 1000000007
typedef long long LL;

int a[5][5], b[5][5], h[111], ans[5];

void Excalibur(int ca){
    int x;
    scanf("%d", &x);
    memset(h, 0, sizeof h);
    REP(i, 4) REP(j, 4){
        scanf("%d", &a[i][j]);
        if (i == x) h[a[i][j]]++;
    }
    scanf("%d", &x);
    int tot = 0;
    REP(i, 4) REP(j, 4){
        scanf("%d", &b[i][j]);
        if (i == x && h[b[i][j]]) ans[++tot] = b[i][j];
    }
    printf("Case #%d: ", ca);
    if (tot == 0) printf("Volunteer cheated!\n");
    if (tot == 1) printf("%d\n", ans[1]);
    if (tot > 1) printf("Bad magician!\n");
}

int main(){
    freopen("A.in", "r", stdin);
    freopen("A.out", "w", stdout);
    int Ti;
    scanf("%d", &Ti);
    REP(z, Ti) Excalibur(z);
}
