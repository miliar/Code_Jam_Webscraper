#include<bits/stdc++.h>

using namespace std;

int main() {
  int t;

  scanf("%d", &t);

  for (int i=0; i<t ;i++ ) {
    int sm, fiend=0, sum=0;
    int temp;

    scanf("%d", &sm);

    for (int j=0; j<=sm ;j++ ) {
      scanf("%1d", &temp);
      if(sum <= j) {
        fiend += (j-sum);
        sum=j;
      }
      sum += temp;
      // printf("%d %d %d\n", j, sum, temp, fiend);
    }

    printf("Case #%d: %d\n", i+1, fiend);
  }



return 0;
}
