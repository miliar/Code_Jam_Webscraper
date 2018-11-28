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


void AllPossiable(const string &S, const int begin,
                  const string word, set<string> &last_words) {
  if (begin == S.size()) {
    last_words.insert(word);
    return;
  }
  string c(1, S[begin]);
  AllPossiable(S, begin + 1, c + word, last_words);
  AllPossiable(S, begin + 1, word + c, last_words);
}


int main() {
  int T;
  fin >> T;

  for (int case_idx = 1; case_idx <= T; ++case_idx) {
    string S;
    fin >> S;

    set<string> last_words;
    AllPossiable(S, 0, "", last_words);

    fout << "Case #" << case_idx << ": " << *last_words.rbegin() << endl;
  }

  fout.close();
}
