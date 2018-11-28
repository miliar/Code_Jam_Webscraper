#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cmath>
#include<algorithm>
#include<string>
#include<map>
#include<set>
#include<iostream>
#include<vector>
#include<queue>

using namespace std;
#define sz(v) ((int)(v).size())
#define rep(i, n) for (int i = 0; i < (n); ++i)
#define repf(i, a, b) for (int i = (a); i <= (b); ++i)
#define repd(i, a, b) for (int i = (a); i >= (b); --i)
#define clr(x) memset(x,0,sizeof(x))
#define clrs( x , y  ) memset(x,y,sizeof(x))
#define out(x) printf(#x" %d\n", x)
#define sqr(x) ((x) * (x))
typedef long long lint;

const int maxint = -1u>>1;
const double eps = 1e-8;
const int maxn = 100000 + 10;

int sgn(const double &x) {  return (x > eps) - (x < -eps);  }

int v[20];
int vn;

void gao(int n) {
    while (n != 0) {
        int d = n % 10;
        if (v[d] == 0) {
            v[d] = 1;
            vn--;
        }
        n /= 10;
    }
}

int main() {
    freopen("A.in", "r", stdin);
    freopen("A.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int ca = 1; ca <= T; ca++) {
        long long n;
        long long ans = -1;
        scanf("%lld", &n);
        if (n == 0) {
            ans = -1;
        }
        else {
            ans = 0;
            memset(v, 0, sizeof(v));
            vn = 10;
            long long m = n;
            while (1) {
                gao(m);
                ans = m;
               // for (int i = 0; i < 10; i++)
              //    printf("%d ", v[i]);
              // printf ("\n");
                if (vn == 0) {
                    break;
                }
                m += n;
            }
        }
        printf ("Case #%d: ", ca);
        if (ans == -1) {
            printf("INSOMNIA\n");
        }
        else {
            printf ("%lld\n", ans);
        }
    }
}
