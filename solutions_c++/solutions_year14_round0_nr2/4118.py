#define nPROFILE
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

#define FORN(i,n) for (int (i) = 0; (i) < (n); (i)++)
#define FE  (i,x) for (typeof((x).begin()) (i) = (x).begin(); (i) != (x).end(); (i)++)

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
    double time;      // solution : minimum time to X
    double C, F, X;
    double rate;      // current cookie rate
    double pos;       // current position in time
    double t_stay;    // time without buying
    double t_buy ;    // time with    buying

    cin >> C >> F >> X;
#ifdef DBG
    printf("============================================================\n");
    printf("C=%.7f F=%.7f X=%.7f\n",C,F,X);
#endif

    rate = 2.0;
    pos  = 0.0;

    while(1) {
      // When starting this loop, we always have 0 cookies in the bank !

#ifdef DBG
      printf("pos=%.7f rate=%.7f\n",pos,rate);
#endif

      // Calculate time to reach X with current cookie rate
      // Calculate time to buy a farm and then reach X with current cookie rate
      //   that is : time to buy a farm + time to reach X with new rate
      t_stay = X / rate;
      t_buy  = C / rate + X / (rate + F);

#ifdef DBG
      printf("t_stay=%.7f t_buy=%.7f\n",t_stay,t_buy);
#endif

      // Compare the two
      // If buying a farm is faster, increase position in time to buy it and get new cookie rate
      // Otherwise we're done !
      if (t_stay > t_buy) {
        pos  += C / rate;
        rate += F;
      } else {
        time = pos + t_stay;
        goto found;
      }

    }

found:
    printf("Case #%d: %.7f\n", num++, time);
  }


}
