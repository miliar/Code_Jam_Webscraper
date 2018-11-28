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

  vector<long long> ret;
  for (int i = 0; i < T; ++i) {
    int N;
    fin >> N;
    if (N == 0) {
      ret.push_back(-1);
      continue;
    }
    
    vector<bool> searched(10, false);
    long long last_num = N;
    long long next_scale = 2;
    while (true) {

      long long num = last_num;
      while (num != 0) {
        searched[num % 10] = true;
        num /= 10;
      }

      bool all_searched = true;
      for (bool f : searched) {
        if (!f) {
          all_searched = false;
          break;
        }
      }

      if (all_searched) {
        break;
      }

      last_num = N * next_scale;
      ++next_scale;
    }

    ret.push_back(last_num);
  }

  for (int case_idx = 1; case_idx <= T; ++case_idx) {
    fout << "Case #" << case_idx << ": ";
    if (ret[case_idx - 1] < 0) {
      fout << "INSOMNIA" << endl;
    } else {
      fout << ret[case_idx - 1] << endl;
    }
  }

  fout.close();
}
