// =====================================================================================
//
//       Filename:  c.cpp
//
//    Description:  
//
//        Version:  1.0
//        Created:  04/09/16 01:21:48
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
  cout << "Case #1:" << endl; 
  int num = 0;
  for (int i = (1<<15)+1; i < (1<<16) && num < 50; i+=2) {
    int factor[11] = {0};
    int cnt = 0;
    for (int k = 2; k <= 10; ++k) {
      long long tmp = 1;
      long long v = 0;
      for (int l = 0; l < 16; ++l) {
        if ((1<<l)&i) {
          v += tmp;
        } 
        tmp *= k;
      }
      for (long long j = 3; j <= 500; j+=2) {
        if (v % j == 0) {
          if (factor[k] == 0) {
            factor[k] = j;
            ++cnt;
          }
          break;
        }
      }
    }
    if (cnt == 9) {
      cout << bitset<16>(i) ;
      for (int j = 2; j <= 10; ++j) {
        cout <<" " << factor[j];
      }
      cout << endl;
      num++;
    }
  }
  return EXIT_SUCCESS;
}				
// ----------  end of function main  ----------
