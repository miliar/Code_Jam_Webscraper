#include <cstdio>
#include <set>
#include <sstream>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;

set<long long> fsn;

#define MAX 100000000000000LL

bool ispal(long long me) {
  stringstream fs; fs << me;
  string f = fs.str();
  string r(f.rbegin(), f.rend());
  return f == r;
}

void test(long long me) {
  long long mesq = me*me;
  if (mesq && ispal(mesq)) {
    fprintf(stderr, "[%20lld -> %20lld]\n", me, mesq);
    fsn.insert(mesq);
  }
}

void rec(long long melow, long long mehigh, long long order) {
  long long me = melow + mehigh*order;
//  if (order <= 1000) fprintf(stderr, "%lld %lld %lld -> %lld\n", melow, mehigh, order, me);
  long long mesq = me * me;
  if (mesq > MAX) return;
  test(me);
  for (long long i = 0; i < 10; i++) {
    long long b = melow + order*i + mehigh*order*10;
    test(b);
  }

  for (long long i = 0; i < 10; i++) {
//    fprintf(stderr, "%lld,%lld,%lld\n", melow + order*i, mehigh*10 + i, order*10);
    rec(melow + order*i, mehigh*10 + i, order*10);
  }
}

int main() {
  for (int i = 1; i < 10; i++) {
    test(i);
    rec(i, i, 10);
  }

  vector<long long> fv(fsn.begin(), fsn.end());

  int T;
  scanf("%d", &T);
  for (int cn = 1; cn <= T; cn++) {
    long long A, B;
    scanf("%lld%lld", &A, &B);
    long long a = lower_bound(fv.begin(), fv.end(), A) - fv.begin();
    long long b = upper_bound(fv.begin(), fv.end(), B) - fv.begin();
    printf("Case #%d: %d\n", cn, b - a);
  }
}
