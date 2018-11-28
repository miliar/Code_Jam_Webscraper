#include <bits/stdc++.h>
#include <boost/range/irange.hpp>
#include <boost/range.hpp>
#include <boost/container/small_vector.hpp>
#include "../../prettyprint.hpp"
using namespace std;
using boost::irange;
using boost::make_iterator_range;

// #ifdef NDEBUG
// #include <boost/iostreams/stream.hpp>
// #include <boost/iostreams/device/null.hpp>
// boost::iostreams::stream<boost::iostreams::null_sink> //logs((boost::iostreams::null_sink()));
// #else
// auto& logs = cerr;
// #endif

// using real_int = int;
// #define int int64_t

int solve() {
  int n; cin >> n;
  unordered_map<string, int> word_ids;
  vector<vector<int> > sentences;
  cin.ignore(numeric_limits<streamsize>::max(), '\n');
  for (auto _ : irange<int>(0, n)) {
    (void)_;
    sentences.emplace_back();
    string line; getline(cin, line);
    istringstream is(line);
    for (string s; is >> s;) {
      if (!word_ids.count(s)) {
        int idx = (int)word_ids.size();
        word_ids[s] = idx;
      }
      sentences.back().push_back(word_ids[s]);
    }
  }
  //logs << '\n' << word_ids << '\n';
  //logs << sentences << '\n';
  //int best=word_ids.size();
  array<vector<int>, 2> langcnt;
  langcnt[0].resize(word_ids.size());
  langcnt[1].resize(word_ids.size());

  vector<boost::container::small_vector<int, 20> > short_sentences(sentences.size()-2);
  for (int i : irange<int>(2, sentences.size())) {
    for (int x : sentences[i])
      short_sentences[i-2].push_back(x);
  }

  // fill(langs.begin(), langs.end(), 0);
  for (int w : sentences[0])
    langcnt[0][w]++;
  for (int w : sentences[1])
    langcnt[1][w]++;
  for (int i : irange<int>(2, sentences.size()))
    for (int w : short_sentences[i-2])
      langcnt[0][w]++;
  int last=0;
  int bothlangcnt=0;

  for (int i : irange<int>(0, word_ids.size()))
    if (langcnt[0][i] && langcnt[1][i])
      ++bothlangcnt;

  int best=bothlangcnt;
  
  for (int bitmask : irange<int>(1, (int(1)<<(sentences.size()-2)))) {
    int diff = bitmask ^ last;
    ////logs << "mask: " << bitmask << '\n';
    for (int i : irange<int>(2, sentences.size())) {
      auto mask = ((bitmask>>(i-2))&1);
      auto lastmask = ((last>>(i-2))&1);
      if (lastmask != mask)
        for (int w : short_sentences[i-2]) {
          int last_cnt=(langcnt[0][w] && langcnt[1][w]);
          langcnt[lastmask][w]--;
          langcnt[mask][w]++;
          int new_cnt=(langcnt[0][w] && langcnt[1][w]);
          bothlangcnt -= last_cnt;
          bothlangcnt += new_cnt;
        }
    }
    // int count=0;
    // for (auto& mask : langs)
    //   if (mask == 3)
    //     ++count;
    //logs << "count " << count << ": " << langs << '\n';
    best = min(bothlangcnt, best);
    last = bitmask;
  }
  return best;
}

int main() {
  int testcases; cin >> testcases;
  for (auto i : irange<int>(1, testcases+1)) {;
    cout << "Case #" << i << ": ";
    cout << solve();
    cout << '\n';
  }
}

/*
 * Local variables:
 * compile-command:"g++ -D_GLIBCXX_DEBUG -g3 -ggdb3 -O0 -Wall -Wextra -std=c++14 bilingual.cc -o bilingual && for f in *.in; do echo \"--- $f -------------\"; ./bilingual <$f; done"
 * end:
 */

