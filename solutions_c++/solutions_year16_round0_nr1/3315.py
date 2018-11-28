#include <string>
#include <fstream>
#include <iostream>
#include <istream>
#include <sstream>
#include <functional>
#include <numeric>
#include <vector>
#include <algorithm>
#include <math.h>

using namespace std;

int main() {
  int T;
  cin >> T;

  for (int t = 0; t != T; ++t) {
    int N;
    cin >> N;

    if (N == 0) {
      cout << "Case #" << t + 1 << ": INSOMNIA" << endl;
      continue;
    }

    long long lastNum = 0;
    int count = 0;
    bool numCheck[10] = { false, };

    long long maxLoop = 9000000000000;
    int loop = 0;

    while (count != 10 && loop != maxLoop) {
      lastNum += N;
      
      string s;
      s = to_string(lastNum);

      int len = s.size();

      for (int i = 0; i != len; ++i) {
        int tmp = s[i] - '0';
        if (!numCheck[tmp]) {
          ++count;
          numCheck[tmp] = true;
        }
      }
      ++loop;
    }

    cout << "Case #" << t + 1 << ": " << lastNum << endl;
  }


  return 0;
}