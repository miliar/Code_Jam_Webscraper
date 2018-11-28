/*
Problem Name : 
Author       : KZ
*/

#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#include <map>
#include <queue>
#include <stack>
#include <string>
#include <vector>
#include <algorithm>

#define INVALID -1
#define INF  1000000000
#define INFL (long)INF*INF

#define _max(a, b)                 ((a) > (b) ? (a):(b))
#define _min(a, b)                 ((a) < (b) ? (a):(b))
#define _abs(a)                    ((a) > 0 ? (a): -(a))
#define _swap(a, b, t)             do { t=a; a=b; b=t; } while(0)
#define _isEqual(a, b)             (_abs((a) - (b)) < 1e-6)
#define _rscanf                    ret = scanf

typedef std::vector<int> IntVec;
typedef std::vector<long> LongVec;
typedef std::vector<double> DoubleVec;
typedef std::map<std::string, int> StrIntMap;

#define _stl_iter(obj, it) for(typeof(obj.begin()) it = obj.begin(); it != obj.end(); it++) 

#define MAX 2000000

char mark[MAX+1];
int primes[200000], nPrimes = 0;

void sieve(void) {
  long i, j;

  primes[nPrimes++] = 2;
  for(i=3;i<=MAX;i+=2) {
    if(mark[i]) continue;
    else {
      primes[nPrimes++] = i;
      for(j=i*i;j<=MAX;j+=i)
	mark[j] = 1;
    }
  }
  //  printf("%d %d\n", primes[nPrimes-1], nPrimes);
  return;
}

long getBaseN_Mod(long v, int n, long base, long m) {
  if(n==1) return v % m;
  return ((base * getBaseN_Mod(v>>1, n-1, base, m))%m + (v & 1))%m;
}

int isLarger(long v, int n, long base, long p2) {
  long s = 0, mux = (long)1 << (n-1);
  int i;
  for(i=1;i<=n;i++, mux >>= 1) {
    s = s * base + (v & mux);
    if(s > p2) break;
  }
  if(i<=n) return 1;
  return 0;
}

int isLegit(long v, int n, int b) {
  int i;
  for(i=0;i<nPrimes && isLarger(v, n, b, primes[i]*primes[i]);i++) {
    if(getBaseN_Mod(v, n, b, primes[i])==0)
      return primes[i];
  }
  return 0;
}

void printBin(long n) {
  if(n==1) {
    printf("1");
    return;
  }
  printBin(n/2);
  printf("%ld",n%2);
  return;
}

int main(void) {
  int T, kase, ret;
  long N, J;
  long mul[11];
  
  sieve();
  _rscanf("%d", &T);
  for(kase=1;kase<=T;kase++) {
    _rscanf("%ld %ld", &N, &J);
    long mn = ((long)1<<(N-1)) + 1, mx = ((long)1<<N) - 1;
    //    printf("Case #%d: %ld %ld\n", kase, mn, mx);
    printf("Case #%d:\n", kase);
    for(long i=mn;i<=mx && J;i+=2) {
      int b;
      for(b=2;b<=10;b++) {
	mul[b] = isLegit(i, N, b);
	if(mul[b] == 0)
	  break;
      }
      if(b > 10) {
	printBin(i);
	for(b=2;b<=10;b++)
	  printf(" %ld", mul[b]);
	printf("\n");
	J--;
      }
    }
  }

  return 0;
}
