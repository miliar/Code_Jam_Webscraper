#include <cstdio>

typedef long long ll;

ll result[1000000];
int ct=0;
int parse[20];
int p;

int main()
{
    freopen("C-small-attempt1.in", "r", stdin);
    freopen("C-small.txt", "w", stdout);
    int i, base;
    ll now;
    int l, r;
    int tc, nc, res;
    int small, big;
    for (i=1;i<=50;i++) {
        base = i;
        for (p=0;base>0;p++) {
            parse[p] = base%10;
            base/=10;
        }
        for (l=0, r=p-1; l<=r && parse[l]==parse[r]; l++, r--);
        if (r< l) {
            now = i*i;
            for (p=0;now>0;p++) {
                parse[p] = now%10LL;
                now/=10LL;
            }
            for (l=0, r=p-1; l<=r && parse[l]==parse[r]; l++, r--);
            if (r < l) {
                result[ct] = i*i;
                ct++;
                //printf("%8d %8d %8d\n", ct, i, i*i);
            }
        }
    }
    result[ct++] = 100000000000000LL;
    scanf("%d", &tc);
    for (nc=1;nc<=tc;nc++) {
        scanf("%d%d", &small, &big);
        //printf("%4d %4d", small, big);
        for (l=0;small>result[l];l++);
        for (r=0;big>=result[r];r++);
        res = r-l;
        //printf(" %5d %5d %5d %5d ", l, result[l], r, result[r]);
        printf("Case #%d: %d\n", nc, res);
    }
}
