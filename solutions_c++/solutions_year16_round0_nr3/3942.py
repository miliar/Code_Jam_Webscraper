#include <cstdio>
#include <algorithm>
#include <vector>
using namespace std;

const int infinity = 1e9 + 9;
const int M = 1e7 + 9;

long long N;
int J;

int prime[M + 9];
int divisor[11];

long long find_divisor(long long n) {
  for (int d = 2; d * d <= n; ++d)
    if (n % d == 0)
      return d;
  return -1;
}

int main()
{
  int found = 0;

  int T;
  scanf("%d", &T);
  for (int Ti = 1; Ti <= T; Ti++)
  {
    // input
    scanf("%lld %d", &N, &J);
    printf("Case #%d:\n", Ti);
    
    // look for jamcoins
    for (long long n = (1 << (N - 1)) + 1; n < (1 << N); n += 2) {     
      // find divisors in each base
      bool ok = true;
      for (int b = 2; b <= 10; ++b) {
	// convert to binary and then to base b
	long long k = n;
	long long r = 0;
	long long d = 1 << (N - 1);
	//printf("b = %d\n", b);
	while (d > 0) {
	  r = b * r + k / d;
	  k %= d;
	  d /= 2;
        }
	//printf("r = %d\n", r);
	divisor[b] = find_divisor(r);
	if (divisor[b] == -1) {
	  ok = false;
	  break;
	}
      }
      if (!ok) {
	//printf("%d fails\n", n);
	continue;
      }    
      
      // print in base 2
      long long k = n;
      long long d = 1 << (N - 1);
      while (d > 0) {
	printf("%lld", k / d);
	k %= d;
	d /= 2;
      }
      
      // print divisors
      for (int b = 2; b <= 10; ++b)
	printf(" %d", divisor[b]);
      printf("\n");
      
      // cut off
      found++;
      if (found >= J)
	break;
    }
  }
  return 0;
}
