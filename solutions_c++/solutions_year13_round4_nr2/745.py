#include <iostream>
#include <cstdio>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <inttypes.h>
#include <cmath>
#include <cstring>

using namespace std;

long long P;

inline long long ceilhalf(long long n) {
  return n%2 == 0 ? n/2 : n/2+1;
}

long long best(long long N, long long k) {
  if (k==0)
    return 0;
  else if (k==1)
    return 1;
  else if (k==(1LL<<N)-1)
    return k;

  return best(N-1, ceilhalf(k));
}

long long worst(long long N, long long k) {
  if (k==0)
    return 0;
  if (k==(1LL<<N)-1)
    return k;

  // long long better;
  // printf("N %lld k %lld\n", N, k);
  // if (k-1 > (1LL<<N)-k-1) {
  //   long long good = (1LL<<N)-k-1;
  //   better = good + ceilhalf(k-1-good);
  // } else {
  //   better = k-1;
  // }
  // printf("b %lld\n", better);
  return (1LL<<(N-1)) + worst(N-1, (k-1)/2);
}

int main() {
  int T_;
  cin >> T_;

  long long N;
  for (int t_ = 1; t_ <= T_; t_++) {
    printf("Case #%d: ", t_);

    cin >> N >> P;

    long long a = 0; // lowest thats good
    long long b = 1LL<<N; // lowest thats not good
    long long c;
    while (true) {
      if ((a+b) % 2 == 0)
        c = (a+b)/2;
      else
        c = (a+b)/2+1;
      if (worst(N,c) >= P) {
        b = c;
      } else {
        a = c;
      }
      if (b == a+1)
        break;
    }

    cout << a << ' ';

    a = 0; // lowest thats good
    b = 1LL<<N; // lowest thats not good
    while (true) {
      if ((a+b) % 2 == 0)
        c = (a+b)/2;
      else
        c = (a+b)/2+1;
      // cout << a << ' ' << b << endl;
      // cout << "c: " << c << endl;
      // cout << best(N,c) << endl;
      if (best(N,c) >= P) {
        b = c;
      } else {
        a = c;
      }
      if (b == a+1)
        break;
    }

    cout << a;


    // for (int i = 0; i < (1<<N); i++) {
    //   printf("%d: %lld %lld\n", i, best(N, i), worst(N, i));
    // }

    // worst(3, 2);

    cout << endl;
  }

  return 0;
}
