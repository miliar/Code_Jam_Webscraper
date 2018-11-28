#include <stdio.h>
#include <set>

using namespace std;

int Deceitful(set<double> naomi, set<double> ken, int n) {
  int ds = 0;
  while (n--) {
    auto iter_n1 = naomi.begin();
    auto iter_k1 = ken.begin(), iter_k2 = ken.end();
    if (*iter_n1 > *iter_k1) {
      ++ds;
      naomi.erase(iter_n1), ken.erase(iter_k1);
    } else {
      naomi.erase(iter_n1), ken.erase(--ken.end());
    }
  }
  return ds;
}

int War(set<double> naomi, set<double> ken, int n) {
  int ws = 0;
  // 1:min 2:max
  while (n--) {
    auto iter_n1 = naomi.begin();
    auto iter_k1 = ken.begin(), iter_k2 = ken.end();
    for ( ; iter_k1 != iter_k2 && *iter_n1 > *iter_k1; ++iter_k1) {}
    if (iter_k1 == iter_k2) {
      // cannot use naomi.end() - 1, set is no operator -
      ken.erase(ken.begin()), naomi.erase(--(naomi.end()));
      ++ws;
    } else {
      ken.erase(iter_k1), naomi.erase(iter_n1);
    }
  }
  return ws;
}

void Read(set<double> &st, int n) {
  double block;
  for (int i = 0; i < n; ++i) {
    scanf("%lf", &block);
    st.insert(block);
  }
  return;
}

int main() {
  int T, N; 
  scanf("%d", &T);
  for (int c = 1; T--; ++c) {
    set<double> naomi, ken;
    scanf("%d", &N);
    Read(naomi, N), Read(ken, N);
    // must pass value, too cost!
    int ds = Deceitful(naomi, ken, N);
    int ws = War(naomi, ken, N);
    printf ("Case #%d: %d %d\n", c, ds, ws);
  }
  return 0;
}
