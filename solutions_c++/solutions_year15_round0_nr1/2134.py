#include <stdio.h>

int main(int argc, char const *argv[])
{
  int t = 0;
  scanf("%d\n", &t);
  for (int ii = 0; ii < t; ii++) {
    int smax = 0;
    scanf("%d ", &smax);
    int needed = 0;
    int sum = 0;
    for (int i = 0; i < smax+1; i++) { 
      char c;
      scanf("%c", &c);
      int val = c-'0';
      if (sum < i) {
        needed += i-sum;
        sum += i-sum;
      }
      sum += val;
    }
    scanf("%*c");
    printf("Case #%d: %d\n", ii+1, needed);
  }
  return 0;
}