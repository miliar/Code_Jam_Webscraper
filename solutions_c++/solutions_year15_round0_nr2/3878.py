#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;

int T, d, p[1100], a[1100];
bool ok(int tot, int time, int lim){
    int pos = 0, ma = 0;
    for (int i = 0; i < tot; i++)
    if (a[i] > ma){
            ma = a[i];
            pos = i;
    }
    if (time + ma <= lim) return true;
    if (ma == 1) return false;
    //for (int i = (ma+1)/2; i >= max(1, ma/2 - 2); i--){
            //printf("%d\n", i);
    if (ma == 9){
        a[pos] = 3; a[tot] = 6;
        if (ok(tot+1, time+1, lim)) return true;
        a[pos] = 4; a[tot] = 5;
        if (ok(tot+1, time+1, lim)) return true;
        a[pos] = 9;
    }
    else{
        a[pos] = ma/2; a[tot] = (ma+1)/2;
        if (ok(tot+1, time+1, lim)) return true;
        a[pos] = ma;
    }
    return false;
}
int main()
{
    //freopen("B-small-attempt2.in", "r", stdin);
    //freopen("bb.out", "w", stdout);
    scanf("%d", &T);
    int cas = 0;
    while(T--){
        scanf("%d", &d);
        for (int i = 0; i < d; i++)
            scanf("%d", p+i);
        for (int i = 1; i <= 9; i++){
            for (int j = 0; j < d; j++) a[j] = p[j];
            if (ok(d, 0, i)){
                printf("Case #%d: %d\n", ++cas, i);
                break;
            }
        }
    }
    return 0;
}
