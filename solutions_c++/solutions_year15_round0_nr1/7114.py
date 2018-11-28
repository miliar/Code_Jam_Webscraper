// =====================================================================================
//
//       Filename:  A.cpp
//
//    Description:  
//
//        Version:  1.0
//        Created:  04/11/15 10:36:14
//       Revision:  none
//       Compiler:  g++ (clang)
//
//         Author:  |Zhiwen Fang| (), |zhiwenf@gmail.com|
//   Organization:  
//
// =====================================================================================

#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <algorithm>

using namespace std;
bool check(string str, int cnt) {
  int S = str.length();
  for (int i = 0; i < S; ++i) {
    if (cnt >= i) {
      cnt += str[i] - '0';
    } else return false;
  }
  return true;
}

int main ( int argc, char *argv[] )
{
  int T;
  cin >> T;
  for (int t = 1; t <= T; ++t) {
    int S;
    string str;
    cin >> S >> str;
    int cnt = 0;
    bool stop = false;
    while (!(stop = check(str, cnt))) ++cnt;
    cout << "Case #" << t << ": " << cnt << endl;
  }

  return EXIT_SUCCESS;
}				
// ----------  end of function main  ----------
