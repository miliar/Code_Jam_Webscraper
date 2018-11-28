// =====================================================================================
//
//       Filename:  A.cpp
//
//    Description:  
//
//        Version:  1.0
//        Created:  04/08/16 23:35:22
//       Revision:  none
//       Compiler:  g++ (clang)
//
//         Author:  |Zhiwen Fang| (), |zhiwenf@gmail.com|
//   Organization:  
//
// =====================================================================================

#include <cstdio>
#include <iostream>
#include <fstream>
#include <cstdlib>
#include <cctype>
#include <cstring>
#include <vector>
#include <string>
#include <list>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <bitset>
#include <numeric>
#include <iomanip>
#include <algorithm>
#include <functional>
#include <ctime>

using namespace std;

int solve(int n) 
{
  bitset<10> flag = 0;
  int cnt = 0;
  long long sum = n;
  while (true) {
    long long tmp = sum;
    while (tmp > 0) {
      if (flag[tmp % 10] == 0) {
        ++cnt;
        flag[tmp % 10] = 1;
      }
      tmp /= 10;
    }
    if (cnt == 10) return sum;
    sum += n;;
  }
}

int main ( int argc, char *argv[] )
{
  int T;
  cin >> T;
  for (int t = 1; t <= T; ++t) {
    int n;
    cin >> n;
    if (n == 0) cout << "Case #" << t << ": " << "INSOMNIA" << endl;
    else cout << "Case #" << t << ": " << solve(n) << endl;
  }
  return EXIT_SUCCESS;
}				
// ----------  end of function main  ----------
