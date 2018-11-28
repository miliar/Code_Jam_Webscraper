#include <cstdio>
#include <algorithm>

using namespace std;

#define Nmax 1000001

int n,t;
int dp[Nmax];

int rev(int x) {
  int dg[10]={0};
  while(x) {
    dg[++dg[0]] = x % 10;
    x /= 10;
  }
  x = 0;
  for (int i = 1; i <= dg[0]; ++i)
    x = x * 10 + dg[i];
  return x; 
}

int main() {
  scanf("%d", &t);
  
  for (int i = 1; i < Nmax; ++i)
    dp[i] = i;
  for (int times = 1; times <= 20; ++times)
  for (int i = 2; i < Nmax; ++i) {
    //dp[i] = min(dp[i], min(dp[i-1] + 1, dp[ rev(i) ] + 1));
    dp[ rev(i) ] = min(dp[ rev(i) ], min(dp[ rev(i) - 1 ] + 1, dp[i] + 1));   
    dp[i] = min(dp[i], dp[i-1] + 1);

    //if (i < 25)
    //  printf("%d: %d\n", i, dp[i]);
  }

  for (int i = 1; i <= t; ++i) {
    scanf("%d", &n);
    printf("Case #%d: %d\n", i, dp[n]);
  }
} 
