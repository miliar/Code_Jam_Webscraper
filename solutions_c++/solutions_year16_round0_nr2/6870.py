// {{{ $VIMCODER$ <-----------------------------------------------------
// vim:filetype=cpp:foldmethod=marker:foldmarker={{{,}}}

#include <algorithm>
#include <array>
#include <bitset>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <functional>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>

using namespace std;

// }}}

const string kInputFilename = "input.txt";
const string kOutputFilename = "output.txt";

ifstream fin(kInputFilename);
ofstream fout(kOutputFilename);



int main() {
  int T;
  fin >> T;

  for (int case_idx = 1; case_idx <= T; ++case_idx) {
    string pancakes;
    fin >> pancakes;

    int base = static_cast<int>(pancakes.size()) - 1;
    while (base >= 0 && pancakes[base] == '+') {
      --base;
    }
    if (base < 0) {
      fout << "Case #" << case_idx << ": " << 0 << endl;
      continue;
    }

    int count = 0;
    char state = '-';
    while (base >= 0) {
      int next_base = base - 1;
      while (next_base >= 0 && pancakes[next_base] == state) {
        --next_base;
      }
      ++count;
      state = state == '+' ? '-' : '+';
      base = next_base;
    }
    fout << "Case #" << case_idx << ": " << count << endl;
  }

  fout.close();
}
