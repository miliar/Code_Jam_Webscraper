#include <cstdio>
using namespace std;

const int NUM_ROWS = 4, NUM_COLUMNS = 4;

void go(int case_number) {
  int ans, foo;
  int card = -1;
  int candidates[NUM_COLUMNS];
  scanf("%d", &ans);
  for(int i = 0; i < NUM_ROWS; ++i)
    for(int j = 0; j < NUM_COLUMNS; ++j)
      if(ans == i + 1) {
        scanf("%d", &candidates[j]);
      }
      else
        scanf("%d", &foo);

  scanf("%d", &ans);
  for(int i = 0; i < NUM_ROWS; ++i)
    for(int j = 0; j < NUM_COLUMNS; ++j)
      if(ans == i + 1) {
        int cand;
        scanf("%d", &cand);
        for(int k = 0; k < NUM_COLUMNS; ++k)
          if(candidates[k] == cand)
            if(card == -1)
              card = cand;
            else
              card = 0;
      }
      else
        scanf("%d", &foo);

  if(card == -1)
    printf("Case #%d: Volunteer cheated!\n", case_number);
  else if(card == 0)
    printf("Case #%d: Bad magician!\n", case_number);
  else
    printf("Case #%d: %d\n", case_number, card);
}

int main() {
  int t;
  scanf("%d", &t);
  for(int i = 0; i < t; ++i)
    go(i+1);
  return 0;
}
