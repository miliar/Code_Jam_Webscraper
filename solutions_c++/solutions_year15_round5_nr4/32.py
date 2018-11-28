#include <algorithm>
#include <cassert>
#include <cstring>
#include <iostream>

using namespace std;

#define FOR(i, a, b) for (int i = (a); i < (b); ++i)
#define REP(i, n) FOR(i, 0, n)
#define TRACE(x) cout << #x << " = " << x << endl
#define _ << " _ " <<

typedef long long llint;
typedef pair<llint, llint> par;
#define s first
#define c second

const int MAX = 10100;

par a[MAX];
llint ok[MAX], le[MAX];
int bio[MAX], cookie;
llint v[MAX];

int main(void) {
  int TC;
  scanf("%d", &TC);
  for (int tp = 1; tp <= TC; ++tp, fflush(stdout)) {
    int P;
    scanf("%d", &P);
    REP(i, P) scanf("%lld", &a[i].s);
    REP(i, P) scanf("%lld", &a[i].c);
    
    sort(a, a + P);
    llint m = 0;
    REP(i, P) m += a[i].c;
    
    int n = 0;
    while ((1LL<<n) < m) n++;
    assert((1LL<<n) == m);
    int cur = 0;
    llint last = -1e18;
    while (cur < n) {
      vector<llint> w;
      REP(i, P) if (a[i].c) w.push_back(a[i].s);

      bool found = false;
      for (llint x: w) {
        if (x < last) continue;

        cookie++;

        bool bad = false;
        if (x >= 0) {
          int j = 0;
          REP(i, P) {

            if (bio[i] != cookie) bio[i] = cookie, ok[i] = 0, le[i] = 0;

            if (a[i].c-ok[i] == 0) continue;
            while (j < P && a[j].s < a[i].s + x) j++;
            if (j >= P || a[j].s != a[i].s + x) { bad = true; break; }
            
            if (bio[j] != cookie) bio[j] = cookie, ok[j] = 0, le[j] = 0;

            llint rem = a[i].c - ok[i];
            if (i != j) {
              if (ok[j] + rem > a[j].c) { bad = true; break; }
              
              ok[i] = a[i].c;
              ok[j] += rem;
              le[i] += rem;
            } else {
              assert(i == j);
              if (rem % 2) { bad = true; break; }
              ok[i] += rem;
              le[i] += rem / 2;
            }
          }
        } else {
          int j = P-1;
          for (int i = P-1; i >= 0; --i) {
            if (bio[i] != cookie) bio[i] = cookie, ok[i] = 0, le[i] = 0;

            if (a[i].c-ok[i] == 0) continue;
            while (j >= 0 && a[j].s > a[i].s + x) j--;
            if (j < 0 || a[j].s != a[i].s + x) { bad = true; break; }
            
            if (bio[j] != cookie) bio[j] = cookie, ok[j] = 0, le[j] = 0;

            llint rem = a[i].c - ok[i];
            if (i != j) {
              if (ok[j] + rem > a[j].c) { bad = true; break; }
              
              ok[i] = a[i].c;
              ok[j] += rem;
              le[i] += rem;
            } else {
              assert(i == j);
              if (rem % 2) { bad = true; break; }
              ok[i] += rem;
              le[i] += rem / 2;
            }
          }
        }

        if (!bad) {
          found = true;
          last = x;
          break;
        }
      }

      assert(found);
      v[cur++] = last;

      int nP = 0;
      REP(i, P) {
        if (bio[i] != cookie) le[i] = 0;
        if (le[i]) a[nP++] = {a[i].s, le[i]};
      }
      P = nP;
    }
    
    sort(v, v + n);
    printf("Case #%d: ", tp);
    REP(i, n) printf("%lld ", v[i]);
    printf("\n");
  }
  return 0;
}
