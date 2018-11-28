#include <stdio.h>
#include <vector>
#include <map>
#include <string>
#include <string.h>
#include <algorithm>
#include <assert.h>

using std::map;
using std::pair;
using std::vector;
using std::sort;
unsigned long long motes[110];
unsigned long long ans[151][151];


#define FOR(i, a , b) for(int i = (a); i <= (b); ++i)
#define FOREACH(it, container) for(typeof(container.begin()) it = container.begin(); it != container.end(); ++it)

int main(){
  int T;
  scanf("%d", &T);
  for(int I = 1; I <= T; ++I){
    int n;
    unsigned long long a;
    scanf("%llu %d", &a, &n);
    for(int i = 1; i <= n; ++i){
      scanf("%llu", &motes[i]);
    }
    sort(motes+1, motes + (n + 1));
    FOR(i, 0, 150){
      ans[0][i] = a;
      FOR(j, 1, 150){
	ans[j][i] = 0;
      }
    }
    int min = 0;
    FOR(i, 1, n){
      int temp = min;
      if (ans[i-1][min] > motes[i]){
	ans[i][min] = ans[i-1][min] + motes[i];
      }
      else{
	min++;
	ans[i][min] = ans[i-1][min-1];
      }
      FOR(j, min, 150){
	if(ans[i-1][j] > motes[i]){
	  ans[i][j] = ans[i-1][j] + motes[i];
	}
	else if(j > temp){
	  ans[i][j] = ans[i-1][j-1];
	}
	if(j > temp && ans[i][j] < ans[i][j-1]){
	  ans[i][j] = ans[i][j-1];
	}
	for(int k = temp; k < j; k++){
	  unsigned long long cur = ans[i-1][k];
	  if (cur <= 1)
	    continue;
	  int t = 0;
	  while (cur <= motes[i]){
	    cur = cur*2 - 1;
	    t++;
	  }
	  if(k + t <= j && ans[i][j] < cur + motes[i]){
	    ans[i][j] = cur + motes[i];
	  }
	}
      }
    }
    printf("Case #%d: %d\n", I, min);
  }
  return 0;
}



// Local Variables:
// compile-command: "g++ -O3 -o A A.cc"
// End:
