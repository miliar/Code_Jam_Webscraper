#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <queue>

using namespace std;

typedef long long ll;

int d;
int p[1<<10];

int main(int argc, char* argv[]){
  int T;
  scanf("%d", &T);
  for(int o = 1; o <= T; o++){
    scanf("%d", &d);
    int mx = 0;
    for(int i = 0; i < d; i++){
      scanf("%d", p+i);
      mx = max(mx, p[i]);
    }
    int ans = mx;
    for(int i = 1; i <= mx; i++){
      int sum = 0;
      for(int j = 0; j < d; j++)
        sum += (p[j] - 1) / i;
      ans = min(ans, sum + i);
    }
    printf("Case #%d: %d\n", o, ans);
  }

  return 0;
}

