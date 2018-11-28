// =====================================================================================
//
//       Filename:  1.cpp
//
//    Description:  
//
//        Version:  1.0
//        Created:  04/30/16 09:05:50
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

int main ( int argc, char *argv[] )
{
  vector<string> ss  = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
  //for (int i = 0; i < 10; ++i) {
    //for (int j = 0; j < ss[i].length(); ++j) {
     // cout << ss[i][j] << endl;
    //}
 // }
  int table[128] = {0};
  table['Z'] = 0;
  table['X'] = 6;
  table['W'] = 2;
  table['U'] = 4;
  table['G'] = 8;
  table['S'] = 7;
  table['V'] = 5;
  table['H'] = 3;
  table['O'] = 1;
  table['I'] = 9;
  string order = "ZXWUGSVHOI";
  int T;
  cin >> T;
  for (int t = 1; t <= T; ++t) {
    string str;
    cin >> str;
    vector<int> cnt(128, 0);
    for (int i = 0; i < str.length(); ++i) {
      cnt[str[i]]++;
    }
    vector<int> ans;
    for (int i = 0; i < order.length(); ++i) {
      int v = table[order[i]];
      int num = cnt[order[i]];
      if (num > 0) {
        ans.insert(ans.end(), num, v);
        string temps = ss[v];
        for (int j = 0; j < temps.length(); ++j) {
          cnt[temps[j]] -= num;
        }
      }
    }
    cout << "Case #" << t << ": ";
    sort(ans.begin(), ans.end());
    for (int i = 0; i < ans.size(); ++i) cout << ans[i];
    cout << endl;
  }
  return EXIT_SUCCESS;
}				
// ----------  end of function main  ----------
