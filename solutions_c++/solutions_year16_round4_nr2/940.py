#include<stdio.h>
#include<vector>
#include<algorithm>
#include<string>
#include<queue>
#include<map>
#include<set>
using namespace std;
int count(int n) {
  int res=0;
  while (n) {
    n &= n-1;
    res++;
  }
  return res;
}
double p[210];
int k,n;
int idx(int i) {
  int res=-1;
  while (i){
    i>>=1;
    res++;
  }
  return res;
}
double M[210][110];
double dfs(int s, int rem, int level) {
  if (s == 0) {
    return 1.0;
  }
  if(M[rem][level]>=0) return M[rem][level];
  int i = idx(s&(-s));
  double res= 0;
  if(k-level > rem) res += p[i] * dfs(s&(s-1), rem, level+1);
  if(rem) res += (1.0-p[i]) * dfs(s&(s-1), rem-1, level+1);
  return M[rem][level]=res;
}
int main() {
  int T;
  scanf("%d",&T);
  for(int tn=1;tn<=T;tn++){
    scanf("%d%d", &n,&k);
    for(int i=0;i<n;i++)scanf("%lf",p+i);
    double res = 0;
    for (int i = 1; i < (1 << n);i++) {
      if(count(i)==k){
        for(int j=0;j<=k;j++)for(int l=0;l<=k;l++)M[j][l]=-1.0;
        res = max(res, dfs(i, k/2, 0));
      }
    }
    printf("Case #%d: %lf\n", tn, res);
  }
  return 0;
}
