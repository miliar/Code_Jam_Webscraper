#include <cstdio>
#include <algorithm>
#include <vector>
using namespace std;

const int infinity = 1e9 + 9;

int N;
bool seen[19];

int main()
{
  int T;
  scanf("%d", &T);
  for (int Ti = 1; Ti <= T; Ti++)
  {
    // input
    scanf("%d", &N);

    // zero is a special case
    if (N == 0) {
      printf("Case #%d: INSOMNIA\n", Ti);
      continue;
    }
    
    // init
    for (int d = 0; d <= 9; ++d)
      seen[d] = false;
    int num_seen = 0;
    
    int K = 0;
    while (num_seen < 10)
    {
      K += N;
      int k = K;
      while (k > 0) {
	if (!seen[k % 10]) {
	  seen[k % 10] = true;
	  num_seen++;
	}
	k /= 10;
      }
    }
    
    // output
    printf("Case #%d: %d\n", Ti, K);
  }
  return 0;
}
