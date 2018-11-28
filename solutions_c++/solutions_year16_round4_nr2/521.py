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

  double  row[2][202];

  for(int t = 0; t < T; ++t) {
    printf("Case #%d: ", t+1);

    int n, k;
    scanf("%d%d", &n, &k);

    vector<double> ch(n, 0.0);

    for (int i = 0; i < n; ++i) {
      scanf("%lf", &(ch[i]));
    }

    sort(ch.begin(), ch.end());

    double ret = -1.;


    for(int num = 0; num <= k; ++num){
//      printf("\n\n");
      int top = n-1, bottom = 0;
      int actrow = 0;
      int lastrow = 1;
      row[0][0] = 1.;
      row[0][1] = 0.;

      for (int i = 1; i <= k; ++i) {
        lastrow = actrow;
        actrow = 1 - actrow;

//        double big = -1.;
//        int bigi = -1;

//        for (int j = 0; j < i; ++j) {
//          if(row[lastrow][j] > big) {
//            big = row[lastrow][j];
//            bigi = j;
//          }
//        }

        double us;
        if(i <= num) {
          us = ch[top];
          --top;
        } else {
          us = ch[bottom];
          ++bottom;
        }
//        printf("\n%.3f:  ", us);

        for (int j = 0; j <= i; ++j) {
          row[actrow][j] = 0.;
          if(j > 0) {
            row[actrow][j] += row[lastrow][j-1] * (us);
          }
          if(j < i) {
            row[actrow][j] += row[lastrow][j] * (1 - us);
          }
//          printf(" %.3f", row[actrow][j]);
        }
      }

      ret = max(ret, row[actrow][k / 2]);
    }
//    printf("\n");


    printf("%.8f\n", ret);


//    printf("\n");
//    for (int i = 0; i < n; ++i) {
//      printf("%.8f ", ch[i]);
//    }
//    printf("\n");

  }

  return 0;
}
