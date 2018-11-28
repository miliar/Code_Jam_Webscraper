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

const vector<string> kNumToStr = {
  "ZERO", "ONE", "TWO", "THREE", "FOUR",
  "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"
};

void Search(vector<int> &char_count, string digits, int digit, string &ret) {
  if (digit > 9) {
    for (int count : char_count) {
      if (count != 0) {
        return;
      }
    }
    ret = digits;
    return;
  }

  // check there's still a matching str.
  bool fail = false;

  Search(char_count, digits, digit + 1, ret);

  for (char c : kNumToStr[digit]) {
    if (char_count[c - 'A'] <= 0) {
      fail = true;
    }
    --char_count[c - 'A'];
  }

  if (!fail) {
    digits.push_back('0' + digit);
    Search(char_count, digits, digit, ret);
  } 
  // restore last minus.
  for (char c : kNumToStr[digit]) {
    ++char_count[c - 'A'];
  }
}

int main() {
  int T;
  fin >> T;

  for (int case_idx = 1; case_idx <= T; ++case_idx) {
    string S;
    fin >> S;

    vector<int> char_count(26, 0);
    for (char c : S) {
      ++char_count[c - 'A'];
    }

    string digits;
    Search(char_count, "", 0, digits);

    fout << "Case #" << case_idx << ": " << digits << endl;
  }

  fout.close();
}
