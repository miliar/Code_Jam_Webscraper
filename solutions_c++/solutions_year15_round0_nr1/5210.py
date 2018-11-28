#include <cstdio>
#define MAX_S 1005

int t;
int smax;
int people[MAX_S];

int main () {
   scanf("%d ", &t);
   for (int i = 1; i <= t; i++) {
      scanf("%d ", &smax);
      int numstanding = 0;
      int numrequired = 0;
      for (int j = 0; j <= smax; j++) {
         char temp;
         scanf("%c ", &temp);
         people[j] = temp - '0';
      }
      for (int j = 0; j <= smax; j++) {
         if (numstanding < j) {
            numrequired += j-numstanding;
            numstanding = j;
         }
         numstanding += people[j];
      }
      printf("Case #%d: %d\n", i, numrequired);
   }
   return 0;
}
