#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
#include <utility>
#include <bitset>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstdio>

using namespace std;

int main() {
  freopen("bl.in", "r", stdin);
  freopen("bl.out", "w", stdout);
  int N;
  scanf("%d", &N);

  for (int qq = 1; qq <= N; qq++) {
    int fl = 0;
    char stk[150];
    scanf("%s", stk);
    for( int i = 150; i >= 0; i--){
      if( stk[i] == '-') {
        for( int j = i; j >= 0; j--){
          if( stk[j] == '-' ) {
            stk[j] = '+';
          }
          else if( stk[j] == '+' ) {
            stk[j] = '-';
          }
        }
        fl++;
      }
    }
    printf("Case #%d: %d\n",qq, fl);
  }
  return 0;
}
