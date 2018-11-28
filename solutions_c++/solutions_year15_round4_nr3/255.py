#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cassert>

#include <iostream>
#include <iomanip>
#include <fstream>
#include <algorithm>
#include <vector>
#include <string>
#include <stack>
#include <queue>
#include <unordered_map>
#include <unordered_set>
#include <map>
#include <set>
#include <sstream>

using namespace std;

typedef long long int64;

inline int GetBit(const int mask, const int bit) {
  return (mask >> bit) & 1;
}

int main() {
  ifstream cin("input.txt");
  ofstream cout("output.txt");
  int testCount;
  cin >> testCount;
  for (int t = 1; t <= testCount; ++t) {
    int n;
    cin >> n;
    string line;
    getline(cin, line);
    unordered_map<string, int> hash;
    vector< set<int> > sentences(n, set<int>());
    int wordCount = 0;
    for (int i = 0; i < n; ++i) {
      getline(cin, line);
      istringstream lineParser(line);
      do {
        string word;
        lineParser >> word;
        if (word.empty())
          continue;
        if (hash.count(word) == 0)
          hash[word] = wordCount++;
        sentences[i].insert(hash[word]);
      } while (lineParser);
    }
    vector<int> languages = vector<int>(wordCount, 0);
    for (const auto &w: sentences[0])
      languages[w] |= 1;
    for (const auto &w: sentences[1])
      languages[w] |= 2;
    int addCost = 0;
    for (int w = 0; w < wordCount; ++w)
      if (languages[w] == 3)
        ++addCost;
    int minCost = wordCount;
    for (int mask = 0; mask < (1 << n); ++mask) {
      if (GetBit(mask, 0) != 0 || GetBit(mask, 1) != 1)
        continue;
      vector< pair<int, int> > changed;
      int cost = 0;
      for (int s = 2; s < n; ++s) {
        for (const auto &w: sentences[s]) {
          int newLanguages = languages[w] |(1 << GetBit(mask, s));
          if (languages[w] != newLanguages) {
            changed.push_back(make_pair(w, languages[w]));
            languages[w] = newLanguages;
            if (newLanguages == 3)
              ++cost;
          }
        }
      }
      reverse(changed.begin(), changed.end());
      for (const auto &c: changed)
        languages[c.first] = c.second;
      minCost = min(minCost, cost + addCost);
    }
    cout << "Case #" << t << ": " << minCost << "\n";
  }
  cin.close();
  cout.close();
  return 0;
}
