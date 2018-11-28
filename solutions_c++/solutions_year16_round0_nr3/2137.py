#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cctype>
#include <sstream>
#include <string>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <bitset>
#include <list>
using namespace std;
 
#define  rep(i,n)  for((i) = 0; (i) < (n); (i)++)
#define  rab(i,a,b)  for((i) = (a); (i) <= (b); (i)++)
#define all(v)    (v).begin(),(v).end()
#define  Fi(n)    rep(i,n)
#define  Fj(n)    rep(j,n)
#define  Fk(n)    rep(k,n)
#define  sz(v)    (v).size()

#define MAX 1000000000L

bitset<MAX/2+1> f;
vector <int> primes;

long get(string s, int base) {
  long x = 0;

  for (int i = 0; i < sz(s); i++) {
    x = (x * base) + (s[i] - '0');
  }

  return x;
}

long is_prime(long x) {
  if (x % 2 == 0) return 2;
  else {
    for (int i = 0; i < sz(primes) && primes[i] * primes[i] <= x; i++) {
      if (x % primes[i] == 0) return primes[i];
    }
  }
  return -1;
}

int main() {
	int T,cs;

  f.reset();
  long i,j;

  for (i = 3; i * i <= MAX; i+=2) {
    if (f.test(i>>1)) continue;
    primes.push_back(i);

    for (j = i * i; j <= MAX; j += 2 * i) {
      f.set(j>>1);
    }
  }

	scanf("%d",&T);

  int N,J,t = 0;

	rab(cs,1,T) {
    scanf("%d %d",&N,&J);

    int i,j;

    cout << "Case #" << cs << ":" << endl;

    rab(i,1,(1 << (N - 2)) - 1) {
      string s = "1";

      j = i;

      int k;

      Fk(N - 2) {
       s += ((j & 1) + '0');
       j >>= 1;
      }

      s += "1";

      vector <long> d;

      for (j = 2; j <= 10; j++) {
        long v = is_prime(get(s,j));

        if (v == -1) break;
        else {
          d.push_back(v);
        }
      }

      if (j > 10) {
        cout << s;

        for (j = 0; j < sz(d); j++) cout << " " << d[j]; // << "(" << get(s, j + 2) <<")";
        cout << endl;
        t++;

        if (t == J) break;
      }
    }
	}

} 
