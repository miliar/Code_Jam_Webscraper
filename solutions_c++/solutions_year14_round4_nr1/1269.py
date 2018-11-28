#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#define MAXN 10005
#define MAXC 705
using namespace std;

typedef long long int LL;
int testcase;
int N,C,A[MAXN],dp[MAXN];

int main () {
  freopen("A-large.in","r",stdin);
  //freopen("A-large.in","r",stdin);
  freopen("A.out","w",stdout);
  scanf("%d",&testcase);
  for (int TC=1;TC<=testcase;TC++) {
    scanf("%d%d",&N,&C);
    for (int i=1;i<=N;++i) scanf("%d",&A[i]);
    sort(A+1,A+N+1);
    int ans = 0, t1 = 1, t2 = N;
    while (t1 <= t2) {
      if (t1 == t2) t1++;
      else if (A[t1] + A[t2] <= C) {
        t1++;
        t2--;
      }
      else t2--;
      ans++;
    }
    printf("Case #%d: %d\n",TC,ans); 
  }
  //system("pause");
}
