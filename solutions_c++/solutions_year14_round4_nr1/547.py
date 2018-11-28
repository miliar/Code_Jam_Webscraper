#include <cstdio>
#include <algorithm>
using namespace std;

int N, X;
int A[10009];
int C[10009];

int main()
{
  int T;
  scanf("%d", &T);
  for (int Ti = 1; Ti <= T; Ti++)
  {
    // input & sort
    scanf("%d %d", &N, &X);
    for (int i = 0; i < N; ++i)
      scanf("%d", &A[i]);
    sort(A, A + N);
    reverse(A, A + N);
    
    // simulate
    int used = 0;
    for (int i = 0; i < N; ++i) {
      int j = 0;
      while (j < used && C[j] < A[i])
        j++;
      //printf("Put %d into bucket %d\n", A[i], j);
      if (j < used) {
        C[j] = 0;
      }
      else {
        used++;
        C[used - 1] = X - A[i];
      }
    }
    
    printf("Case #%d: %d\n", Ti, used);
  }
  return 0;
}