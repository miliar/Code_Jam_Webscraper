#include <vector> 
#include <list> 
#include <map> 
#include <set> 
#include <deque> 
#include <queue> 
#include <stack> 
#include <bitset> 
#include <algorithm> 
#include <functional> 
#include <numeric> 
#include <utility> 
#include <sstream> 
#include <iostream> 
#include <iomanip> 
#include <cstdio> 
#include <cmath> 
#include <cstdlib> 
#include <cctype> 
#include <string> 
#include <cstring> 
#include <ctime>
#include <sys/types.h>


using namespace std;
typedef vector<int> vi_t; 
typedef pair<int, int> pii_t;
typedef long long int64;

int main() {

  int tc, N, cnt, ls, rv;
  scanf("%d\n", &tc);
  for( int tid= 1; tid <= tc ; tid++) {
    ls = 0;
    rv = 0;
    scanf("%d ", &N);
     for( int i = 0; i <= N ; i++)  { 
        cnt = getchar() - '0';
        if( i > ls)
        {
          rv += i - ls;
          ls += i - ls;
        }
        ls += cnt;
      }
    printf("Case #%d: %d\n", tid, rv);
  }
  return 0;
}
