#include <stdio.h>
#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;
void solve_case()
{
  int A,B, K;
  long long way = 0;
  scanf ("%d %d %d", &A, &B, &K);

  for (int i = 0; i < A; i++)
    {
      for (int j = 0; j < B; j++)
        {
          if ((i&j) < K)
          {
//          printf ("--%d %d--\n" , i , j);
            way++; 
          }
        }
    }
  printf("%lld\n", way);

}

int main()
{
  int T = 0;
  scanf("%d", &T);
  for (int i = 0; i < T; i++)
    {
      printf ("Case #%d: ", i+1);
      solve_case();
    }
}
