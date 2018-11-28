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

int n;
int L, R;
double c, f, x;

double ans(int k) {
  double sum = 0;
  double f1 = 2;
  while (k--) { 
    sum += c / f1;
    f1 += f; 
  }
  sum += x/f1; 
  return sum;
}

int main() {
#ifdef PRETEST
  freopen("in.txt", "r", stdin);
#endif
  int t;
  RI(t);
  REPE(tt, 1, t) {
    scanf("%lf%lf%lf", &c, &f, &x);
    if (x < c - eps) {
      printf("Case #%d: %.6lf\n", tt, x/2);
      continue;
    }
    L = 0;
    R = 100002;
    while (L + 2 < R) {
      int L1 = L + (R-L)/3;
      int R1 = L + ((R-L))/3*2;
      double ans1 = ans(L1); 
      double ans2 = ans(R1);
      if (ans1 < ans2) {
        R = R1;
      } else {
        L = L1; 
      }
    }
    double tmp;
    tmp = min(ans(L), ans(L+1));
    tmp = min(tmp, ans(L+2));
    tmp = min(tmp, ans(L+3));
    printf("Case #%d: %.6lf\n", tt, tmp);
  }
  return 0;
}


