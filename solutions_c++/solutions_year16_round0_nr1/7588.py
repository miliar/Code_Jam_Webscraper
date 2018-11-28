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
  freopen("ab.in", "r", stdin);
  freopen("ab.out", "w", stdout);
  int N;
  scanf("%d", &N);

  for (int qq = 1; qq <= N; qq++) {
    int no;
    int mult = 1;
    int ctd[] = {0,0,0,0,0,0,0,0,0,0};

    int tt;
    scanf("%d", &tt);
    no = tt;

    int nf = 1;
    if ( tt == 0 ){
      nf = 0;
    }

    while(nf && mult < 100) {

      no = mult*tt;
      int itr = no;
      // printf("mult %d\n", mult);
      // printf("no %d\n", no);

      while(itr) {
          int d = itr % 10;
          itr /= 10;
          ctd[d] = 1;
      }

      for(int i = 0; i < 10; i++){
        if( ctd[i] == 0 ){
          break;
        }
        else if( i == 9 && ctd[i] == 1) {
          nf = 0;
        }
      }
      mult++;
    }
    if( no == 0 ){
      printf("Case #%d: INSOMNIA\n",qq);
    } else {
      printf("Case #%d: %d\n",qq, no);
    }
  }
  return 0;
}
