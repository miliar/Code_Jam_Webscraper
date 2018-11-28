// =====================================================================================
//
//       Filename:  b.cpp
//
//    Description:  
//
//        Version:  1.0
//        Created:  04/09/16 00:24:48
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

int dp[2][128];

void solve() {
  dp[0][1] = 1;
  dp[1][1] = 0;
  for (int i = 2; i < 101; ++i) {
    dp[0][i] = dp[1][i-1] + 1;
    dp[1][i] = dp[0][i-1] + 1;
  }
}

int main ( int argc, char *argv[] )
{
  solve();
  int T;
  cin >> T;
  for (int t = 1; t <= T; ++t) {
    string str;
    cin >> str;
    int s = (str[0] == '+') ? 1 : 0;
    int len = 1;
    for (int i = 1; i < str.length(); ++i) {
      if (str[i] != str[i-1]) ++len;
    }
    cout << "Case #" << t << ": " << dp[s][len] << endl;
  }
  return EXIT_SUCCESS;
}				
// ----------  end of function main  ----------
