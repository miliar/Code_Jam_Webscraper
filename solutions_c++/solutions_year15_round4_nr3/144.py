#define NDEBUG
#include <algorithm>
#include <bitset>
#include <cassert>
#include <climits>
#include <cstdio>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <utility>
#include <vector>
using namespace std;

vector<string> split(const string &str, const string &delimeters = " ") {
  vector<string> ret;
  string::size_type pos, end;
  pos = str.find_first_not_of(delimeters);
  while (pos != string::npos) {
    end = str.find_first_of(delimeters, pos+1);
    if (end == string::npos) {
      end = str.length();
    }
    ret.push_back(str.substr(pos, end-pos));
    pos = str.find_first_not_of(delimeters, end);
  }
  return ret;
}
#define repeat(n) for (int repc = (n); repc > 0; --repc)
template<typename T, typename U> inline void makemin(T &res, const U &x) {
  if (x < res) {
    res = x;
  }
}
template <typename T> inline int get_bit(const T &x, int index) {
  return int((x >> index) & 1);
}

int solve() {
  int N;
  cin >> N >> ws;
  map<string, int> wordid;
  using Wordset = bitset<3000>;
  vector<Wordset> sentences;
  repeat (N) {
    string line;
    getline(cin, line);
    vector<string> tok = split(line);
    Wordset ids;
    for (string x : tok) {
      auto it = wordid.find(x);
      if (it == wordid.end()) {
        it = wordid.insert(make_pair(x, wordid.size())).first;
      }
      assert(it->second < (int)ids.size());
      ids.set(it->second);
    }
    sentences.push_back(ids);
  }

  int best = INT_MAX;
  for (int mask=2; mask<(1<<N); mask+=4) {
    Wordset english, french;
    for (int i=0; i<N; ++i) {
      if (get_bit(mask, i)) {
        english |= sentences[i];
      } else {
        french |= sentences[i];
      }
    }
    makemin(best, (english & french).count());
  }
  return best;
}

int main() {
  ios_base::sync_with_stdio(0);

  int T;
  cin >> T;
  for (int tt=1; tt<=T; ++tt) {
    printf("Case #%d: %d\n", tt, solve());
    fflush(stdout);
  }
}
