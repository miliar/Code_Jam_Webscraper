#include <stdio.h>
#include <stdlib.h>
#include <queue>
using namespace std;

int P[1000];

int main() {

  int T;

  scanf("%d", &T);

  for(int i=1; i<=T; ++i) {
    
    int D;

    scanf("%d", &D);

    for(int j=0; j<D; j++) 
      scanf("%d", &P[j]);

    int best = 1000;

    for(int j=1; j<=1000; j++) {
      int special_mins = j;
      for(int k=0; k<D; k++) {
	special_mins += (P[k]-1)/j;
      }
      if(special_mins<best)
	best = special_mins;
    }

    printf("Case #%d: %d\n", i, best);
  }

  return 0;

}
