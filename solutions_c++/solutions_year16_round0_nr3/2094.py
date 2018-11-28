#include <cstdio>
#include <algorithm>

using namespace std;

int main()
{
   int N, J;
   scanf("%d%d", &N, &J);
   printf("Case #1:\n");
   for(int i=0; i<J; i++){
      int k = i;
      printf("11");
      for(int j=0; j<N/2-2; j++) {
         printf("%s", k%2 ? "11" : "00");
         k /= 2;
      }
      printf("11");
      for(int j=2; j<=10; j++)
         printf(" %d ", j+1);
      printf("\n");
   }
   return 0;
}
