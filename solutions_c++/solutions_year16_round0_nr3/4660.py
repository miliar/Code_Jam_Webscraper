#include <cstdio>
#include <cstring>
#include <vector>

using namespace std;

const int maxn = 20;
bool number[maxn];
int n, j;
int factor[11];

void fill(int mask) {
  for(int i = 1; i < n - 1; i++) {
    number[i] = mask & 1;
    mask >>= 1;
  }
}

int primes[5800000];
int pi;
bool check[100000000+1];

void init() {
  pi = 0;
  memset(check, false, sizeof check);
  for(int i = 2; i <= 100000000; i++) {
    if(!check[i]) {
      primes[pi++] = i;
    }
    for(int j = 0; j < pi; j++) {
      if(i * 1LL * primes[j] > 100000000)
	break;
      check[i * primes[j]] = true;
      if(i % primes[j] == 0)
	break;
    }
  }
}

int find_factor(int base) {
  long long num = 0;
  long long cur = 1;
  for(int i = 0; i < n; i++) {
    if(number[i]) {
      num += cur;
    }
    cur *= base;
  }
  //printf("number is %lld\n", num);
  for(int i = 0; i < pi; i++) {
    if(primes[i] * 1LL * primes[i] > num) {
      //printf("finishing at prime %d\n", primes[i]);
      break;
    }
    //printf("testing %lld\n", primes[i]);
    if(num % primes[i] == 0) {
      return primes[i];
    }
  }
  return -1;
}

int main() {
  init();
  int tc;
  scanf("%d", &tc);
  for(int kase = 1; kase <= tc; kase++) {
    scanf("%d%d", &n, &j);
    printf("Case #%d:\n", kase);
    number[0] = true;
    number[n-1] = true;
    for(int mask = 0; mask < (1 << (n - 2)) && j; mask++) {
      fill(mask);
      bool ok = true;
      for(int base = 2; base <= 10; base++) {
	int fact = find_factor(base);
	factor[base] = fact;
	if(fact == -1) {
	  ok = false;
	  break;
	}
      }
      if(ok) {
	for(int j = n - 1; j >= 0; j--) {
	  printf("%d", number[j] ? 1 : 0);
	}
	for(int j = 2; j <= 10; j++) {
	  printf(" %d", factor[j]);
	}
	printf("\n");
	j--;
      }
    }
  }
  return 0;
}
