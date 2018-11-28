#include <stdio.h>
#include <assert.h>
#include <algorithm>
#include <vector>
#include <queue>
#include <functional>

using namespace std;

#define inf 1000000007
#define rep(i, n) for(int i = 0; i < n; i++)

typedef long long ll;

int d[10][10];
int dw[10][10];
int ww[10];

int main() {
  int t;
  scanf("%d",&t);
  rep(tt, t) {
    int n;
    scanf("%d",&n);
    rep(i, n) {
      char s[10];
      scanf("%s",s);
      rep(j, n) {
        d[i][j] = s[j] - '0';
      }
    }
    int mi = 10000;
    rep(i, (1 << (n * n))) {
      int kk = 0;
      rep(j, n) {
        rep(k, n) {
          dw[j][k] = (i >> (j * n + k)) & 1;
          if(d[j][k] == 1 && dw[j][k] == 0) {
            goto aa;
          }
          if(d[j][k] == 0 && dw[j][k] == 1) {
            kk++;
          }
        }
      }
      rep(j, n) {
        ww[j] = (i >> (j * n)) & ((1 << n) - 1);
      }
      rep(j, n) {
        int kq = 0;
        rep(k, n) {
          kq += dw[j][k];
        }
        if(kq == 0) {
          goto aa;
        }
        int o = 0;
        rep(k, n) {
          if(ww[j] == ww[k]) {
            o++;
          }
          else if((ww[j] & ww[k]) != 0) {
            goto aa;
          }
        }
        if(o != kq) {
          goto aa;
        }
      }
      mi = min(mi, kk);
      aa:;
    }
    printf("Case #%d: %d\n", tt + 1, mi);
  }
}
