#include<stdio.h>
#include<string.h>
#include<math.h>
#include<algorithm>
using namespace std;

int l[1010], t[1010], ans = 0;
bool upd;

struct attack {
    int m, e, w, move, s, d, dd, ss;
}at[20];

void gao(int x, int j) {
    int nowe = at[j].e + x * at[j].move, noww = at[j].w + x * at[j].move, nows = at[j].s + x * at[j].ss;
    //printf("%d %d %d %d %d\n", x, j, noww - 110, nowe - 110, nows);
    for(int i = noww; i <= nowe; i++) {
        if(l[i] < nows) {
            //puts("SUCCESS");
            ans++;
            upd = true;
            break;
        }
    }
    for(int i = noww; i <= nowe; i++) t[i] = max(t[i], nows);
}

int main()
{
    freopen("C-small-attempt1.in", "r", stdin);
    freopen("C-small-attempt1.out", "w", stdout);
    int _, cnt = 1;
    scanf("%d", &_);
    while(_--) {
        memset(l, 0, sizeof(l));
        memset(t, 0, sizeof(t));
        ans = 0;
        int n;
        scanf("%d", &n);
        for(int i = 0; i < n; i++) {
            scanf("%d%d%d%d%d%d%d%d", &at[i].d, &at[i].m, &at[i].w, &at[i].e, &at[i].s, &at[i].dd, &at[i].move, &at[i].ss);
            at[i].e *= 2, at[i].w *= 2, at[i].move *= 2;
            at[i].e += 320, at[i].w += 320;

        }
        for(int i = 0; i <= 676060; i++) {
            upd = false;
            for(int j = 0; j < n; j++) {
                if((i - at[j].d) % at[j].dd == 0) {
                    if((i - at[j].d) / at[j].dd >= 0 && (i - at[j].d) / at[j].dd < at[j].m) gao((i - at[j].d) / at[j].dd, j);
                }
            }
            if( upd == true ) {
                for(int j = 0; j < 1000; j++) l[j] = max(l[j], t[j]);
                memset(t, 0, sizeof(t));
            }
        }
        printf("Case #%d: %d\n", cnt++, ans);
    }

    return 0;
}
