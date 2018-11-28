#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<algorithm>
using namespace std;

int a[1005], b[1005];
int T, n;
int solve1(){
    int best = 0;
    for (int win = 1; win <= n; win ++){
         bool check = true;
         for (int j = 1; j <= win; j ++)
             if (a[n - win + j] < b[j]){
                check = false;
                break;
             }
         if (check) best = win;
    }
    return best;
}
int solve2(){
     int pts = n, j = 1;
     for (int i = 1; i <= n; i ++){
         while (j <= n && b[j] < a[i]) j ++;
         if (j <= n) pts --, j ++;
     }return pts;
}
int main(){
    freopen("D-large.in","r",stdin);
    freopen("D.out","w",stdout);
    scanf("%d",&T);
    for (int tst = 1; tst <= T; tst ++){
        scanf("%d",&n);
        double x;
        for (int i = 1; i <= n; i ++) scanf("%lf",&x), a[i] = (int)(x * 100000);
        for (int i = 1; i <= n; i ++) scanf("%lf",&x), b[i] = (int)(x * 100000);
        sort(a + 1, a + 1 + n);
        sort(b + 1, b + 1 + n);
        printf("Case #%d: %d %d\n", tst, solve1(), solve2());
    }
    return 0;
}
