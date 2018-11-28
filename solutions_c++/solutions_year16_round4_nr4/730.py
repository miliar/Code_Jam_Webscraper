#define _CRT_SECURE_NO_DEPRECATE
#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include <queue>
#include <algorithm>
#include <iomanip>
#include <map>
#include <set>
#include <math.h>
#include <stack>
#include <deque>
#include <numeric>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <bitset>
#include <functional>
#define all(x) x.begin(),x.end()
#define mpair make_pair
using namespace std;
typedef long long ll;
typedef long double ld;
const ld epsylon = 1e-9;

const string PROGRAM_NAME = "google";

int main() {
  freopen((PROGRAM_NAME + ".in").c_str(), "r", stdin);
  freopen((PROGRAM_NAME + ".out").c_str(), "w", stdout);
  int nt;
  cin >> nt;
  for (int it = 1; it <= nt; it++) {
    int n;
    cin >> n;
    vector<string> a(n);
    getline(cin, a[0]);
    for (int i = 0; i < (int)a.size(); ++i) {
      getline(cin, a[i]);
    }

    int best = n * n;
    for (int mask = 0; mask < 1 << (n * n); ++mask) {
      bool good_mask = true;
      for (int j = 0; j < n * n; ++j) {
        if (a[j / n][j % n] == '1' && (mask & (1 << j)) == 0) {
          good_mask = false;
          break;
        }
      }
      if (!good_mask) {
        continue;
      }
      bool works = true;
      vector<int> w(n);
      vector<int> m(n);
      for (int i = 0; i < n; ++i) {
        w[i] = i;
      }
      bool all_orders_work = true;
      do {
        for (int i = 0; i < n; ++i) {
          m[i] = i;
        }
        bool some_order_fails = false;
        do {
          bool valid = true;
          for (int i = 0; i < n; ++i) {
             if ((mask & (1 << (w[i] * n + m[i]))) == 0) {
               bool still_good = false;
               for (int j = i + 1; j < n; ++j) {
                 if ((mask & (1 << (w[i] * n + m[j]))) != 0) {
                   still_good = true;
                   break;
                 }
               }
               if (!still_good) {
                 some_order_fails = true;
                 break;
               } else {
                 valid = false;
                 break;
               }
             }
          }
          if (some_order_fails) {
            break;
          }
        } while (next_permutation(all(m)));
        if (some_order_fails) {
          all_orders_work = false;
          break;
        }
      } while (next_permutation(all(w)));
      if (!all_orders_work) {
        works = false;
      }
//      for (int j = 0; j < n; ++j) {
//        bool all_zero = true;
//        for (int i = 0; i < n; ++i) {
//          if ((mask & (1 << (i * n + j)))) {
//            all_zero = false;
//            break;
//          }
//        }
//        if (all_zero) {
//          works = false;
//          break;
//        }
//      }
//
//      for (int i = 0; i < n; ++i) {
//        bool all_zero = true;
//        for (int j = 0; j < n; ++j) {
//          if ((mask & (1 << (i * n + j)))) {
//            all_zero = false;
//            break;
//          }
//        }
//        if (all_zero) {
//          works = false;
//          break;
//        }
//      }
//      if (!works) {
//        continue;
//      }
//      for (int i = 0; i < n; ++i) {
//        for (int j = 0; j < n; ++j) {
//          if ((mask & (1 << (i * n + j))) == 0) {
//            vector<int> temp;
//            for (int k = 0; k < n; ++k) {
//              if (k != j) {
//                temp.push_back(k);
//              }
//            }
//            bool found = false;
//            do {
//              int it = 0;
//              bool good2 = true;
//              for (int k = 0; k < (int)temp.size(); ++k) {
//                while (it == i) {
//                  ++it;
//                }
//                if ((mask & (1 << (it * n + temp[k]))) == 0) {
//                  good2 = false;
//                  break;
//                }
//                it++;
//              }
//              if (good2) {
//                found = true;
//                break;
//              }
//            } while (next_permutation(all(temp)));
//            if (found) {
//              works = false;
//              break;
//            }
//          }
//        }
//      }

      if (works) {
        int needed = 0;
        for (int j = 0; j < n * n; ++j) {
          if (a[j / n][j % n] == '0' && (mask & (1 << j)) != 0) {
            needed++;
          }
        }
        if (needed < best) {
          best = needed;
        }
      }
    }
    cout << "Case #" << it << ": " << best << endl;
  }
  return 0;
}
