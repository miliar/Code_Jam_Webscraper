#include <cstdio>
#include <algorithm>
using namespace std;

int a, b, ans;

int w[20][20];

int check(int x) {
    int res = 0;
    for(int i = 0; i < a * b; i++) {
        if(((1<<i) & x) > 0) w[i / a][i % a] = 1;
        else w[i / a][i % a] = 0;
    }
//    for(int i = 0; i < b; i++) {
//        for(int j = 0; j < a; j++) printf("%d", w[i][j]);
//        printf("\n");
//    }
    for(int i = 0; i < b; i++) {
        for(int j = 0; j < a; j++) {
            if(i + 1 < b && ((w[i + 1][j] & w[i][j]) == 1)) res++;
            if(j + 1 < a && ((w[i][j + 1] & w[i][j]) == 1)) res++;
        }
    }
    //printf("!!!!!%d %d\n", x, res);
    return res;
}

int main() {
freopen("B-small-attempt0.in", "r", stdin);
    freopen("B-small-attempt0.out", "w", stdout);
    int _, cnt = 0;
    scanf("%d", &_);
    while(_--) {
        int ans = 10000000;
        int n;
        scanf("%d%d%d", &a, &b, &n);
        for(int i = 0; i < 1<<(a * b); i++) {
            int x = i, l = 0;
            while(x > 0) {
                l += (x % 2);
                x /= 2;
            }
            if(l != n) continue;
            ans = min(ans, check(i));
        }
        printf("Case #%d: %d\n", ++cnt, ans);
    }

}
