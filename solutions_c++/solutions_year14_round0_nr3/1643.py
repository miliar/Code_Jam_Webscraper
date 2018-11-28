#include<iostream>
#include<cstdio>
#include<cstring>
#include<vector>
#include<list>
#include<cctype>
#include<algorithm>
#include<functional>
#include<map>
#include<set>
#include<queue>
#include<stack>
#include<cmath>

using namespace std;

#define INF 0x7FFFFFFF
#define INFLL 0x7FFFFFFFFFFFFFFF
#define BIG 0x4F4F4F4F
#define RESET(a,x) memset(a,x,sizeof(a))
#define EXIST(a,s) ((s).find(a) != (s).end())
#define eps 1e-9
typedef long long ll;
typedef unsigned long long ull;
const double PI = acos(-1.0);

#define sqr(x) ((x)*(x))
#define eps 1e-9
#define REP(I,N) for(size_t I=0;I<(N);I++)
#define REPR(I,A,B) for(size_t I=(A);I<(B);I++)
#define REPE(I,A,B) for(size_t I=(A);I<=(B);I++)
#define RS(X) scanf("%s", (X))
#define RI(X) scanf("%d", &(X))
#define RD(X) scanf("%lf", &(X))
#define RII(X,Y) scanf("%d%d", &(X), &(Y))
#define FOR_EACH(i,c) for (__typeof(c.begin()) i = c.begin(); i != c.end(); ++i)

const int maxn = 100;
int n;
int r, c, m;
bool bo;
bool ans;
char g[maxn][maxn];

int main() {
#ifdef PRETEST
  freopen("in.txt", "r", stdin);
#endif
  int t;
  RI(t);
  REPE(tt, 1, t) {
    RII(r, c);
    RI(m);
    m = r*c - m;
    printf("Case #%d:\n", tt);
    ans = true;
    for (int i = 0; i < 60; i++) {
      for (int j = 0; j < 60; j++) {
        g[i][j] = '*';
      }
    }
    if (m == 1) {
      g[1][1] = 'c';
      for (int i = 1; i <= r; i++) {
        for (int j = 1; j <= c; j++) {
          printf("%c", g[i][j]);
        }
        printf("\n");
      }
      continue;
    }
    if (r > c) {
      swap(r, c);
      bo = true;
    } else {
      bo = false;
    }
    if (r == 1) {
      g[1][1] = 'c';
      for (int i = 2; i <= m; i++) {
        g[1][i] = '.';
      }
      for (int i = m+1; i <= c; i++) {
        g[1][i] = '*';
      }
    } else if (r == 2 && c == 2) {
      if (m != 4) {
        ans = false; 
      } else {
        g[1][1] = 'c';
        g[1][2] = '.';
        g[2][2] = '.';
        g[2][1] = '.';
      }
    } else if (m <= 3 || m == 5 || m == 7) {
      ans = false;
    } else {
      g[1][1] = 'c';
      g[1][2] = '.';
      g[2][2] = '.';
      g[2][1] = '.';
        if (m % 2 == 0) {
          if (m <= 2 * c) {
            for (int i = 3; i <= m /2; i++) {
              g[1][i] = '.';
              g[2][i] = '.';
            }
          } else { 
            for (int i = 3; i <= c; i++) {
              g[1][i] = '.';
              g[2][i] = '.';
            }
            for (int i = 3; i <= m / c; i++) {
              for (int j = 1; j <= c; j++) {
                g[i][j] = '.';
              }
            }
            if (m % c == 1) {
              g[m/c][c] = '*';
              g[m/c+1][1] = '.';
              g[m/c+1][2] = '.';
            } else if (m % c != 0) {
              for (int i = 1; i <= m % c; i++)  {
                g[m/c+1][i] = '.';
              }
            }
          }
        } else {
          if (m <= 2*c) {
            for (int i = 3; i <= (m-3)/2; i++) {
              g[1][i] = '.';
              g[2][i] = '.';
            }
            if (r == 2) {
              ans = false;
            } else {
              g[3][1] = '.';
              g[3][2] = '.';
              g[3][3] = '.';
            }
          } else if (m == 2*c+1) {
            if (r == 2) {
              ans = false;
            } else {
              for (int i = 3; i <= c - 1; i++) {
                g[1][i] = '.';
                g[2][i] = '.';
              }
              g[3][1] = '.';
              g[3][2] = '.';
              g[3][3] = '.';
            }
          } else {
            for (int i = 3; i <= c; i++) {
              g[1][i] = '.';
              g[2][i] = '.';
            }
            for (int i = 3; i <= m / c; i++) {
              for (int j = 1; j <= c; j++) {
                g[i][j] = '.';
              }
            }
            if (m % c == 1) {
              g[m/c][c] = '*';
              g[m/c+1][1] = '.';
              g[m/c+1][2] = '.';
            } else if (m % c != 0) {
              for (int i = 1; i <= m % c; i++)  {
                g[m/c+1][i] = '.';
              }
            }
          }
        }
    }
    if (!ans) {
      printf("Impossible\n");
    } else {
      if (bo) {
        for (int i = 1; i <= c; i++) {
          for (int j = 1; j <= r; j++) {
            printf("%c", g[j][i]);
          }
          printf("\n");
        }
      } else {
        for (int i = 1; i <= r; i++) {
          for (int j = 1; j <= c; j++) {
            printf("%c", g[i][j]);
          }
          printf("\n");
        }
      }
    }
  }
  return 0;
}


