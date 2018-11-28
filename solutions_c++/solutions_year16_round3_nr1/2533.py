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

#define REP(i,n) for((i)=0;(i)<(int)(n);(i)++)
#define snuke(c,itr) for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();itr++)

int main() {

freopen("al.in", "r", stdin);
freopen("al.out", "w", stdout);
int T;
scanf("%d", &T);
char c[26];
for( int ii = 0; ii < 26; ii++){
  c[ii] = static_cast<char>('A' + ii);
}
for(int qq = 1; qq <=T; qq++) {
  int N;
  scanf("%d", &N);
  int tot = 0;
  int s[N];
  for( int ii = 0; ii < N; ii++) {
    scanf("%d", &s[ii]);
    tot+=s[ii];
  }
  vector <int> nn;
  printf("Case #%d: ", qq);
  while(tot > 0) {
    int max = 0;
    for( int jj = 0; jj < N; jj++) {
      if( s[jj] > max){
        max = s[jj];
      }
    }
    vector <int> l;
    int mp = 0;
    for( int jj = 0; jj < N; jj++) {
      if( s[jj] == max && mp < 2) {
        if (mp == 0) {
          mp++;
          s[jj]--;
          tot--;
          printf("%c", c[jj]);
        }
        else if( tot !=2 && mp == 1) {
          mp++;
          s[jj]--;
          tot--;
          printf("%c", c[jj]);
        } else {
          break;
        }
        }
    }
    printf(" ");
  }
  // for( int ii = 0; ii < N; ii++){
  //   printf(" %d ", s[ii]);
  // }
  printf("\n");
}

return 0;
}
