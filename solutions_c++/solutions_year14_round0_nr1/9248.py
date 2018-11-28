#include <cstdio>

using namespace std;

int main() {
  int T, iteration  = 0, i, j;
  int firstAnswer, secondAnswer; 
  int possibleAnswer[17];
  int elem;
  int count;
  int answer;

  scanf("%d", &T);
  while(T--) {
    iteration++;
    for(i=1; i<=16; i++)
      possibleAnswer[i] = 0;
    scanf("%d", &firstAnswer);
    for(i = 1; i <= 4; i++) {
      for(j = 1; j <= 4; j++) {
        scanf("%d", &elem);
        if(i==firstAnswer) {
          possibleAnswer[elem] = 1;
        }
      }
    }
    count = 0;
    scanf("%d", &secondAnswer);
    for(i=1; i <= 4; i++) {
      for(j=1; j <= 4; j++) {
        scanf("%d", &elem);
        if(i==secondAnswer && possibleAnswer[elem]==1) {
          answer = elem;
          count++;
        }
      }
    }
    if(count == 1) {
      printf("Case #%d: %d\n", iteration, answer);
    }
    else if(count == 0) {
      printf("Case #%d: Volunteer cheated!\n", iteration);
    }
    else {
      printf("Case #%d: Bad magician!\n", iteration);
    }
  }
  return 0;
}


