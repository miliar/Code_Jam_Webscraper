#define nDBG

#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <list>
#include <cmath>
#include <algorithm>
#include <iterator>
#include <utility>
using namespace std;

typedef vector<int>          vint;
typedef vector<unsigned int> vuint;
typedef vector<string>       vstr;
typedef long long            ll;
typedef unsigned long long   ull;
typedef pair<int, int>       pii;
typedef set<double>           sf;

#define FORN(i,n) for (int (i) = 0; (i) < (n); (i)++)

#define PB push_back
#define MP make_pair
#define A  first
#define B  second

ostream& operator<<(ostream& os, const vector<int> keys) {
  vector<int>::size_type sz = keys.size();
  for (unsigned int i = 0; i < sz; i++)
    os << keys[i] << " ";
  os << endl;
  return os;
}

void disp_table(int table[101][101], int N, int M) {
  for (int i = 0; i < N; i++) {
    for (int j = 0; j < M; j++)
      printf("%d ", table[i][j]);
    printf("\n");
  }
  printf("\n");
}



int main() {
  int T, num=1;

  for (cin >> T; T--;) {
    int N, score_war, score_deceit;
    double k;
    set<double> blocks_naomi, blocks_ken;
    set<double> bn,bk; // working versions
    set<double>::iterator f;
    set<double>::iterator mn, mk; // min of naomi, min of ken
    set<double>::iterator trade_n, trade_k; // traded blocks

    cin >> N;
    FORN(i,N) { cin >> k ; blocks_naomi.insert(k);}
    FORN(i,N) { cin >> k ; blocks_ken.insert(k);}
    bn = blocks_naomi;
    bk = blocks_ken;
    score_war = score_deceit = 0;

#ifdef DBG
    for (f = blocks_naomi.begin(); f != blocks_naomi.end(); f++)
      printf("%f ", *f);
    printf("\n");
    for (f = blocks_ken.begin(); f != blocks_ken.end(); f++)
      printf("%f ", *f);
    printf("\n");
#endif

    // ----------------------------------------------------
    // Deceitful war strategy
    FORN(i,N) {

      // Find min weight of Naomi and of Ken
      mn = bn.begin();
      mk = bk.begin();

      // If min weight of Naomi is lower than the one of Ken, it can never win, trade it for the biggest of Ken
      // No points scored
      if (*mn < *mk) {
        trade_n = mn;
        trade_k = bk.end();
        trade_k--;

      } else {
      // Otherwise, trade it for the smallest of Ken
      // Score a point
        trade_n = mn;
        trade_k = mk;
        score_deceit++;
      }

      // Remove the traded items
      bn.erase(trade_n);
      bk.erase(trade_k);

    }

    // ----------------------------------------------------
    // War strategy
    // Is there even any strategy for Naomi ?
    // Just play all the blocks from smallest to biggest
    bn = blocks_naomi;
    bk = blocks_ken;
    FORN(i,N) {

      // Find min weight of Naomi
      mn = bn.begin();

      // Look for any block of Ken bigger than this
      mk = bk.lower_bound(*mn);

      // If it is found use those two
      // No point scored
      // Otherwise, use the smallest from Ken
      // Score a point
      if (mk == bk.end()) {
        mk = bk.begin();
        score_war++;
      }

      bn.erase(mn);
      bk.erase(mk);

    }

    printf("Case #%d: %d %d\n", num++, score_deceit,score_war);
  }

}
