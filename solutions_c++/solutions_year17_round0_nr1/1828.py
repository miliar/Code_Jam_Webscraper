#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>

using namespace std;

int main() {
  int T;
  cin >> T;
  for(int i = 1; i <= T; ++i) {
    string str;
    cin >> str;
    int k;
    cin >> k;
    int nrFlips = 0;
    for(int i = 0; i < str.size(); ++i) {
      if( str[i] == '-' ) {
        if( i + k <= str.size() ) {
          ++nrFlips;
          for(int j = 0; j < k; ++j) {
            str[i + j] = str[i + j] == '-' ? '+' : '-';
          }
        } else {
          nrFlips = -1;
          break;
        }
      }
    }
    // cout << str << endl;

    if( nrFlips != -1 ) {
      printf("Case #%d: %d\n", i, nrFlips);
    } else {
      printf("Case #%d: IMPOSSIBLE\n", i);
    }
  }
  return 0;
}