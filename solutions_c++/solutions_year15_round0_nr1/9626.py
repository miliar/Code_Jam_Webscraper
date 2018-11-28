#include <iostream>
#include <vector>
#include <cstdio>
#include <algorithm>
using namespace std;

int main() {
  int T;
  scanf("%d",&T);
  for(int t = 1;t <= T;t++) {
    int Smax;
    scanf("%d",&Smax);
    char sh[1010];
    scanf("%s",sh);
    int cnt = sh[0] - '0';
    int ans = 0;
    for(int i = 1;i <= Smax;i++) {
      if(cnt >= i) {
	cnt += sh[i] - '0';
      }else {
	ans += i - cnt;
	cnt = i + sh[i] - '0';
      }
    }
    printf("Case #%d: %d\n",t,ans);
  }
  
  return 0;
}
