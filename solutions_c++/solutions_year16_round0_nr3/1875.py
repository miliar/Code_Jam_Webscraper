#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cctype>
#include <sstream>
#include <iterator>
#include <string>
#include <vector>

using namespace std;

typedef long long LL;

#define FOR(v,p,k) for(int v=p;v<=k;++v)
#define FORD(v,p,k) for(int v=p;v>=k;--v)
#define FORL(v,p,k) for(int v=p;v<k;++v)
#define REP(i,n) for(int i=0;i<(n);++i)
#define VAR(v,i) __typeof(i) v=(i)
#define FOREACH(i,c) for(VAR(i,(c).begin());i!=(c).end();++i)
#define PB push_back
#define SIZE(x) (int)x.size()
#define ALL(c) c.begin(),c.end()

int t[20];
const int n = 16, m = 50;
int cnt = 0;
vector<int> divs;

vector<int> primes;

const int MAXP = 40*1000*1000;
char sieve[MAXP];

void makeprimes(void){
  primes.PB(2);
  FOR(i, 3, MAXP)
    if (!sieve[i]) {
       primes.PB(i);
       for (int j = i + i; j < MAXP; j += i)
          sieve[j] = 1;
    }
}

int check_prime(long long x){
  for (int i = 0; (LL)primes[i] * (LL)primes[i] <= x; ++i)
    if ((LL)primes[i] < x && x % primes[i] == 0LL)
      return primes[i];
  return 0;
}

bool check(void){
  divs.clear();
  FOR(a, 2, 10){
    long long x = 0LL;
    REP(i, n)
      x = (LL)a * x + (LL)t[i];
    int z = check_prime(x);
    if (z <= 1) return false;
    divs.PB(z);
  }
  REP(i, n) printf("%d", t[i]);
  FOREACH(it, divs) printf(" %d", *it);
  printf("\n");
  cnt++;
  return true;
}

void rekur(int z){
  if (cnt >= m) return;
  if (z == n-1)
    check();
  else{
    t[z] = 0; rekur(z+1);
    t[z] = 1; rekur(z+1);
  }
}

int main()
{
  makeprimes();
  t[0] = t[n-1] = 1;
  printf("Case #1:\n");
  rekur(1);
  return 0;
}
