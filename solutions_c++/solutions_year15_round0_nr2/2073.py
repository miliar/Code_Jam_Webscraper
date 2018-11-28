#include <bits/stdc++.h>
using namespace std;

const int INF = 1000000000;
const int MAXD = 1005;
int T, D, P[1005], res;

int main(){
  scanf("%d", &T);
  for(int _t = 1; _t <= T; _t++){
    scanf("%d", &D);
    for(int i = 0; i < D; i++){
      scanf("%d", &P[i]);
    }
    res = INF;
    for(int i = 1; i < MAXD; i++){
      int cur = i;
      for(int j = 0; j < D; j++){
        cur += max(0, (P[j] - 1) / i);
      }
      res = min(res, cur);
    }
    printf("Case #%d: %d\n", _t, res);
  }
}
