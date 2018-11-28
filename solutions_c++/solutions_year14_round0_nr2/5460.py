#include <bits/stdc++.h>
using namespace std;

typedef long double ld;

int main(){
  int T;
  cin >> T;
  for(int tc = 1 ; tc <= T ; tc++){
    ld C, F, X;
    cin >> C >> F >> X;
    
    ld ans = X / 2.0;
    ld R = 2.0;    
    ld times = 0;
    while(true){
      times += C / R;
      R += F;
      if(ans > times + X / R) ans = times + X / R;
      else break;
    }
    printf("Case #%d: %.7Lf\n", tc, ans);
  }
}
