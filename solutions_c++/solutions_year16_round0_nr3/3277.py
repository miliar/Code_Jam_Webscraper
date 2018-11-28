#include<cstdio>
#include<cmath>

#define L 1000000000
bool primes[L] = {0};

void generate_prime(bool primes[L]) {
  for (int i = 0; i < L; ++i)
    primes[i] = true;
  primes[0] = false;
  primes[1] = false;
  for (int i = 2; i <= L/2; ++i)  {
     if (primes[i]) {
       for (int j = 2*i; j < L; j += i) {
         primes[j] = false;
       }
     }
  }
}

int main()
{
//  generate_prime(primes);
  
  int t;
  scanf("%d", &t);
  for (int i = 1; i <= t; ++i) {
    int N, J;
    scanf("%d%d", &N, &J);
    printf("Case #%d:\n", i);

    int count = 0;
    unsigned int x = (1<<(N-2));
    unsigned int end = (unsigned int)(1<<(N-1));
    for (; x < end; x++) {
      unsigned int y = (x<<1);
      y += 1;
      
      int divisors[11] = {0};

      int base = 2;
      for (; base <= 10; ++base) {
      	long long val = 0; 
        long long m = 1;
        for (int j = 0; j < 32; ++j, m*=base) {
          if ((y & (1<<j)) != 0)
            val += m;
        }

        bool prim = true;
        for (int j = 2; j <= sqrt(val); ++j) {
          if (val % j == 0) {
            divisors[base] = j;
            prim = false;
            break;
          }
        }
        if (prim)
          break;
      }

      if (base <= 10) continue;
      for (int j = N-1; j >= 0; j--) {
        if ((y & (1<<j)) != 0) printf("1");
        else printf("0");
      }

      base = 2;
      for (; base <= 10; ++base) {
        printf(" %d", divisors[base]);
      }
      printf("\n");

      count++;
      if (count == J) break;
    }
  }

  return 0;
}
