#include <cstdio>
#include <algorithm>
#include <vector>
#include <cstring>

using namespace std;

int n;
int mo[111];
int dp[111][1111111];
int ma;

int solve(int a,int b)
{
  if(a==n)return 0;
  if(b>ma)return 0;
  if(dp[a][b]>=0)return dp[a][b];
  int res = solve(a+1,b)+1;
  if(mo[a]<b) {
    return dp[a][b]=min(res,solve(a+1,b+mo[a]));
  } else {
    return dp[a][b]=min(res,solve(a,b+b-1)+1);
  }
}

int main(void)
{
  int T;
  int a;
  int c;
  
  scanf("%d", &T);
  for(int I = 1; I <= T; I++) {
    printf("Case #%d: ",I);
    scanf("%d%d",&a,&n);
    ma = 0;
    memset(dp,-1,sizeof(dp));
    for(int i = 0; i < n; i++) {
      scanf("%d",mo+i);
      ma=max(ma,mo[i]);
    }
    sort(mo,mo+n);
    if( a == 1 ) c = n;
    else c = solve(0,a);
    printf("%d\n",c);
  }
  return 0;
}
