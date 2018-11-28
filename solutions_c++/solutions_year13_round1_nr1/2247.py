#include <cstdio>
#include <iostream>
#include <stdlib.h>
using namespace std;

main(){
  long long int r, t;
  long long int val = 0;
  int cases = 1, C;
  for (cin >> C; C--;) {
    cin >> r >> t;
    val = 0;
    while (t >= 0){
      t = t - ((r+1)*(r+1)) + r*r;
      val = val + 1;
      r = r+2;
    }
    if (t < 0){
      val = val - 1;
    }
    printf("Case #%d: %lld\n", cases++, val);
  }
}
