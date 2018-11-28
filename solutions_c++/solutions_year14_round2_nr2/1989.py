#include <cstdio>

using namespace std;

int main()
{
  int T;
  unsigned int A, B, K;

  scanf("%d\n", &T);

  for(int t=1; t<=T; t++) {
    unsigned int count = 0;
    scanf("%d %d %d", &A, &B, &K);
    for(unsigned int i=0; i<A; i++)
      for(unsigned int j=0; j<B; j++)
	if((i&j)<K)
	  count++;
    printf("Case #%d: %d\n", t, count);
  }
  return 0;
}
