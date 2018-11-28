#include <stdio.h>
#include <string.h>
#include <algorithm>

using namespace std;

long long A, N;
long long D[1000010];

int main() {
  int T, kas=0;
  
  scanf("%d", &T);
  while(T--) {
    scanf("%lld%lld", &A, &N);
    for(int i=0;i<N;++i)
      scanf("%lld", D+i);
    sort(D, D+N);
    
    long long eat = 0;
    bool first = true;
    long long count = 0;
    for(int i=0;i<N;++i) {
      if(D[i] < A) {
        A += D[i];
        if(first) ++eat;
      } else {
        first = false;
        int x = (N - i);
        int j;
        bool yes = false;
        long long sum = A;
        for(j=1;j<=x;++j) {
          sum = 2 * sum - 1;
          //if(i == 2)
            //fprintf(stderr, "sum = %lld\n", sum);
          if(sum > D[i]) {
            sum += D[i];
            yes = true;
            break;
          }
        }
        if( yes )  A = sum, count += j;
        else  ++count;
      }
    }
    //fprintf(stderr, "eat = %lld\n", eat);
    if( count > N - eat ) count = N - eat;
    printf("Case #%d: %lld\n", ++kas, count);
  }

  return 0;
}

