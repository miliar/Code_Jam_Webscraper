#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <iostream>
#include <limits>
#include <numeric>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>

using namespace std;

#define MP make_pair
#define all(v) (v).begin(), (v).end()
#define PROBLEM_ID "C"

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<vvi> vvvi;
typedef vector<bool> vb;
typedef vector<vb> vvb;
typedef vector<vvb> vvvb;
typedef long double ld;
typedef pair<int, int> pii;
typedef long long ll;
typedef vector<ll> vl;
typedef vector<vl> vvl;
typedef vector<vvl> vvvl;
typedef pair<ll, ll> pll;
typedef vector<double> vd;
typedef vector<vd> vvd;
typedef vector<vvd> vvvd;

int GetMinBilingual(const vector< set<string> >& sentences, const vector<int>& masks) {
  int n = sentences.size();
  int res = 0;
  for (int i = 0; i < n; ++i) {
    res += sentences[i].size();
  }
  for (int mask = 0; mask < (1 << (n - 2)); ++mask) {
    int curres = 0;
    int full_mask = (mask << 2) + 1;
    for (int i = 0; i < masks.size(); ++i) {
      if ((full_mask & masks[i]) == masks[i] || (full_mask & masks[i]) == 0) {
        continue;
      }
      ++curres;
    }
    res = min(res, curres);
  }
  return res;
}

int main() {
  freopen(PROBLEM_ID".in", "r", stdin);
  freopen(PROBLEM_ID".out", "w", stdout);
  int tests;
  cin >> tests;
  for (int test_index = 0; test_index < tests; ++test_index) {
    int n;
    cin >> n;
    cerr << n << endl;
    char buffer[100000];
    gets(buffer);
    vector< set<string> > sentences(n);
    for (int i = 0; i < n; ++i) {
      gets(buffer);
      string sentence = buffer;
      istringstream in(sentence);
      string word = "";
      do {
        in >> word;
        if (word == "") {
          break;
        }
        sentences[i].insert(word);
        word = "";
      } while (true);
    }
    set<string> words;
    for (int i = 0; i < sentences.size(); ++i) {
      for (set<string>::const_iterator it = sentences[i].begin(); it != sentences[i].end(); ++it) {
        words.insert(*it);
      }
    }
    vector<string> all_words(words.begin(), words.end());
    vector<int> masks(all_words.size());
    for (int i = 0; i < all_words.size(); ++i) {
      for (int j = 0; j < sentences.size(); ++j) {
        if (sentences[j].find(all_words[i]) != sentences[j].end()) {
          masks[i] |= (1 << j);
        }
      }
    }
    int res = GetMinBilingual(sentences, masks);
    cout << "Case #" << (test_index + 1) << ": " << res << endl;
    cerr << "Case #" << (test_index + 1) << ": " << res << endl;
  }
  return 0;
}
