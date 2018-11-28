#include <iostream>
#include <cstdio>
#include <algorithm>
#include <set>
#define MAXN 1005
using namespace std;

int testcase,N;
double A[MAXN], B[MAXN];
set <double> S;

int main () {
  freopen("D-large.in","r",stdin);
  freopen("a.out","w",stdout);
  scanf("%d",&testcase);
  for (int TC=1;TC<=testcase;++TC) {
    scanf("%d",&N);
    for (int i=0;i<N;++i) scanf("%lf",&A[i]);
    for (int i=0;i<N;++i) scanf("%lf",&B[i]);
    sort(A,A+N);
    sort(B,B+N);
    int A1 = 0, A2 = 0;
    for (int t=0;t<N;++t) {
      bool can = 1;
      for (int i=0;i<N-t;++i)
        if (A[t+i] < B[i]) {
          can = 0;
          break;
        }
      if (can) {
        A1 = N-t;
        break;
      }
    }
    S.clear();
    for (int i=0;i<N;++i) S.insert(B[i]);
    for (int i=N-1;i>=0;--i) {
      if (S.lower_bound(A[i]) == S.end()) {
        ++A2;
        S.erase(S.begin());
      }
      else S.erase(S.lower_bound(A[i]));
    }
    printf("Case #%d: %d %d\n",TC,A1,A2);
  }
  //system("pause");
}
