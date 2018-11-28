#include<stdio.h>

using namespace std;

int main()
{
  long int A, B, K;
  int T;
  scanf("%d", &T);
  for (int t = 0; t < T; t++){
    scanf("%ld %ld %ld", &A, &B, &K);
    //printf("%ld %ld %ld\n", A, B, K);
    long int win = 0;
    for (long int i = 0; i < A; i++){
      for (long int j = 0; j < B; j++){
	long int zreb = i&j;
	if (zreb < K) win++;
      }
    }
    printf("Case #%d: %ld\n", t+1, win);
  }
  return 0;
}