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


void _GenCandidates(const string &score, const int i,
                   const int val, vector<int> &ret) {
  if (i == score.size()) {
    ret.push_back(val);
    return;
  }

  if (score[i] != '?') {
    _GenCandidates(score, i + 1, val * 10 + (score[i] - '0'), ret);
  } else {
    for (int d = 0; d <= 9; ++d) {
      _GenCandidates(score, i + 1, val * 10 + d, ret);
    }
  }
}


vector<int> GenCandidates(const string &score) {
  vector<int> ret;
  _GenCandidates(score, 0, 0, ret);
  return ret;
}


int main() {
  int T;
  fin >> T;

  for (int case_idx = 1; case_idx <= T; ++case_idx) {
    string C, J;
    fin >> C >> J;

    auto C_candidates = GenCandidates(C);
    auto J_candidates = GenCandidates(J);

    int min_diff = INT_MAX;
    int min_c = -1, min_j = -1;

    for (int c : C_candidates) {
      for (int j : J_candidates) {
        if (abs(c - j) < min_diff) {
          min_c = c;
          min_j = j;
          min_diff = abs(c - j);
        }
      }
    }

    fout << "Case #" << case_idx << ": ";
    fout << setfill('0') << setw(C.size()) << min_c;
    fout << ' ';
    fout << setfill('0') << setw(J.size()) << min_j;
    fout << endl;
  }

  fout.close();
}
