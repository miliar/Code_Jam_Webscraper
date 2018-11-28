#include <bits/stdc++.h>
#define INF 1000000007
using namespace std;

int T, ans, d, a[5000];

int main(){

  scanf("%d", &T);
  for(int ct = 1; ct <= T; ct ++){
    scanf("%d", &d);
    for(int i = 0; i < d; i ++)
      scanf("%d", &a[i]);

    int mx = 0;
    for(int i = 0; i < d; i ++)
      mx = max(mx, a[i]);

    ans = INF;
    for(int i = 1; i <= mx; i ++){
      int ta = i, pl = 0;
      for(int j = 0; j < d; j ++)
        if(a[j] > i){
          int nn = a[j] / i;
          if(a[j] % i == 0)
            nn --;
          pl += nn;
        }
      ta += pl;
      ans = min(ans, ta);
    }
    
    printf("Case #%d: %d\n", ct, ans);
  }
  
  return 0;
}
