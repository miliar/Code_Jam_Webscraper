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


void Search(
    const vector<vector<int>> &papers,
    const int begin,

    const int N,
    vector<vector<int>> &matrix,
    vector<bool> &row_filled,
    vector<bool> &col_filled,

    vector<int> &ret) {

  if (begin == papers.size()) {

    for (int r = 0; r < N; ++r) {
      if (row_filled[r]) {
        continue;
      }
      for (int c = 0; c < N; ++c) {
        ret[c] = matrix[r][c];
      }
      return;
    }

    for (int c = 0; c < N; ++c) {
      if (col_filled[c]) {
        continue;
      }
      for (int r = 0; r < N; ++r) {
        ret[r] = matrix[r][c];
      }
      return;
    }

  }

  // search on row.
  const auto &paper = papers[begin];
  for (int r = 0; r < N; ++r) {
    if (row_filled[r]) {
      continue;
    }
    bool mismatch = false;
    for (int c = 0; c < N; ++c) {
      if (matrix[r][c] == -1 || matrix[r][c] == paper[c]) {
        continue;
      } else {
        mismatch = true;
        break;
      }
    }
    if (mismatch) {
      continue;
    } else {
      auto tmp = matrix[r];
      row_filled[r] = true;
      matrix[r] = paper;

      Search(papers, begin + 1, N, matrix, row_filled, col_filled, ret);

      matrix[r] = tmp;
      row_filled[r] = false;
    }
  }

  // search on column;
  for (int c = 0; c < N; ++c) {
    if (col_filled[c]) {
      continue;
    }
    bool mismatch = false;
    for (int r = 0; r < N; ++r) {
      if (matrix[r][c] == -1 || matrix[r][c] == paper[r]) {
        continue;
      } else {
        mismatch = true;
        break;
      }
    }
    if (mismatch) {
      continue;
    } else {
      vector<int> tmp(N, 0);
      for (int r = 0; r < N; ++r) {
        tmp[r] = matrix[r][c];
        matrix[r][c] = paper[r];
      }
      col_filled[c] = true;

      Search(papers, begin + 1, N, matrix, row_filled, col_filled, ret);

      for (int r = 0; r < N; ++r) {
        matrix[r][c] = tmp[r];
      }
      col_filled[c] = false;
    }
  }
}


int main() {
  int T;
  fin >> T;

  for (int case_idx = 1; case_idx <= T; ++case_idx) {
    int N;
    fin >> N;

    vector<vector<int>> papers;
    for (int i = 0; i < 2 * N - 1; ++i) {
      vector<int> paper(N, -1);
      for (int j = 0; j < N; ++j) {
        fin >> paper[j];
      }
      papers.push_back(paper);
    }

    vector<vector<int>> matrix(N, vector<int>(N, -1));
    vector<bool> row_filled(N, false);
    vector<bool> col_filled(N, false);
    
    vector<int> ret(N, -1);

    Search(papers, 0, N, matrix, row_filled, col_filled, ret);

    fout << "Case #" << case_idx << ":";
    for (int i = 0; i < N; ++i) {
      fout << " " << ret[i];
    }
    fout << endl;
  }

  fout.close();
}
