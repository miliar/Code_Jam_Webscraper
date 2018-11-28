#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <cstdlib>
#include <ctime>

using namespace std;
typedef long long lglg;

int main()
{
  int T;
  scanf("%d", &T);

  for(int t = 0; t < T; ++t) {
    printf("Case #%d: ", t+1);

    vector<int> S;

    int p;

    scanf("%d", &p);

    vector<lglg> e(p);
    vector<lglg> f(p);

    for(int i = 0; i < p; ++i) {
      scanf("%I64d", &e[i]);
    }
    for(int i = 0; i < p; ++i) {
      scanf("%I64d", &f[i]);
    }

//    printf("Beolvast\n");

    while(f[0] > 1) {
      S.push_back(0);
      for(int i = 0; i < p; ++i) {
        f[i] /= 2;
      }
    }

    for(int i = 1; i < p; ++i) {
      int d = e[i] - e[0];

      bool bad = false;

      while(!bad) {

//        printf("%d\n", d);
        vector<lglg> fproba = f;
        int it2 = 0;

        for(int it1 = 0; it1 < p; ++it1) {
          if(fproba[it1] > 0) {
            while(it2 < p && e[it2] < e[it1] + d) ++it2;
            if(it2 >= p || e[it2] > e[it1] + d || fproba[it2] < fproba[it1]) {
              bad = true;
              break;
            }

            fproba[it2] -= fproba[it1];
          }
        }

        if(!bad) {
          f = fproba;
          S.push_back(d);
        }
      }
    }

    sort(S.begin(), S.end());

    for(int i = 0; i < S.size(); ++i) {
      printf("%d ", S[i]);
    }

    printf("\n");

  }

  return 0;
}
