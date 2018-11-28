#include <algorithm>
#include <utility>
#include <vector>
#include <queue>
#include <iostream>
#include <climits>
#include <string>
#include <cmath>
#include <assert.h>
#include <unordered_map>
#include <sstream>
#include <stack>
#include <unordered_set>
#include <bitset>
#include <time.h>
#include <cstring>
#include <set>
#include <list>
#include <cfloat>
#include <iomanip>

using namespace std;


//C is farm price, F is accelaration speed, X is winning amount
void compute(double C, double F, double X, double curr_rate, double &optimal_time, double curr_time) {
    //if we buy no farms and wait
    double temp_curr_time = curr_time + X/curr_rate;
    optimal_time = optimal_time < temp_curr_time? optimal_time : temp_curr_time;
    //if we buy a farm
    curr_time = curr_time + C/curr_rate;
    curr_rate += F;
    if(curr_time < optimal_time)
        compute(C, F, X, curr_rate, optimal_time, curr_time);
    else
        return;
}
int main() {
  //freopen ("C:\\Users\\Case\\Desktop\\B-small-attempt0.in", "r", stdin);
  //freopen ("C:\\Users\\Case\\Desktop\\B-small-attempt0.out", "w", stdout);
  int N;
  double C, F, X;
  cin >> N;
  for(int round = 0; round < N; round++) {
      cin >> C >> F >> X;
      double optimal_time = DBL_MAX;
      compute(C, F, X, 2, optimal_time, 0);
      cout << "Case #" << (round + 1) << ": " ;
      cout << std::fixed;
      cout << setprecision(7) << optimal_time << endl;
  }
  return 0;
}
