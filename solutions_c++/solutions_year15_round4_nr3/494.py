#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <deque>
#include <functional>
#include <iostream>
#include <limits>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <tuple>
#include <vector>
using namespace std;

template <class T>
void SortUniq(T& a) {
  sort(a.begin(), a.end());
  a.erase(unique(a.begin(), a.end()), a.end());
}

template<class T>
bool Contains(const T& a, int b) {
  return binary_search(a.begin(), a.end(), b);
}

void Solve() {
  int N;
  cin >> N;

  string line;
  getline(cin, line);

  vector<string> all_words;
  vector<vector<string>> words(N);
  for (vector<string>& sentence : words) {
    line.clear();
    getline(cin, line);

    stringstream ss(line);
    string word;
    while (ss >> word) {
      sentence.push_back(word);
      all_words.push_back(word);
    }
  }

  SortUniq(all_words);

  vector<vector<int>> W(N);
  for (int i = 0; i < N; ++i) {
    for (const string& word : words[i]) {
      int idx = lower_bound(all_words.begin(), all_words.end(), word) -
                all_words.end();
      W[i].push_back(idx);
    }
  }

  vector<int> base_english = W[0];
  vector<int> base_french = W[1];
  SortUniq(base_english);
  SortUniq(base_french);

  vector<int> base;
  set_intersection(base_english.begin(), base_english.end(),
                   base_french.begin(), base_french.end(), back_inserter(base));

  if (N == 2) {
    cout << base.size();
    return;
  }

  int result = numeric_limits<int>::max();

  int NN = 1 << (N - 2);
  vector<int> e, f, ef;
  for (int mask = 0; mask < NN; ++mask) {
    e.clear();
    f.clear();
    ef.clear();

    for (int i = 0; i < N - 2; ++i) {
      if (mask & (1 << i)) {
        for (int idx : W[i + 2]) {
          e.push_back(idx);
        }
      } else {
        for (int idx : W[i + 2]) {
          f.push_back(idx);
        }
      }
    }

    SortUniq(e);
    SortUniq(f);
    set_intersection(e.begin(), e.end(), f.begin(), f.end(), back_inserter(ef));

    int extra = 0;

    for (int idx : ef) {
      if (!Contains(base, idx)) {
        ++extra;
      }
    }

    for (int idx : e) {
      if (Contains(ef, idx)) {
        continue;
      }
      if (Contains(base, idx)) {
        continue;
      }
      if (Contains(base_french, idx)) {
        ++extra;
      }
    }

    for (int idx : f) {
      if (Contains(ef, idx)) {
        continue;
      }
      if (Contains(base, idx)) {
        continue;
      }
      if (Contains(base_english, idx)) {
        ++extra;
      }
    }

    result = min(result, extra + (int) base.size());
  }

  cout << result;
}

int main() {
//  freopen("../Console/1.txt", "rb", stdin);
  freopen("../Console/C-small-attempt0.in", "rb", stdin);
//  freopen("../Console/C-small-attempt0.out", "wb", stdout);
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  int T;
  cin >> T;
  for (int tc = 0; tc < T; ++tc) {
    cout << "Case #" << tc + 1 << ": ";
    Solve();
    cout << endl;
  }

  return 0;
}
