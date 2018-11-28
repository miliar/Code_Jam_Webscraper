#include <algorithm>
#include <functional>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <deque>
#include <iostream>
#include <limits>
#include <map>
#include <queue>
#include <set>
#include <list>
#include <vector>
#include <sstream>
#include <numeric>
using std::cin;
using std::cout;

int M, N;
std::vector<std::string> S;
std::vector<int> assignment;

int answer_count = 0;
int max_anwser = 0;

int CountTrieSize(const std::vector<std::string>& str) {
  std::vector<std::string> prefixes;
  prefixes.push_back("");

  for (const std::string& s : str) {
    for (size_t pos = 0; pos <= s.size(); ++pos) {
      prefixes.push_back(s.substr(0, pos));
    }
  }

  std::sort(prefixes.begin(), prefixes.end());
  prefixes.erase(std::unique(prefixes.begin(), prefixes.end()), prefixes.end());

  return static_cast<int>(prefixes.size());
}

void go(int index) {
  if (index == M) {
    std::vector<int> types = assignment;
    std::sort(types.begin(), types.end());
    types.erase(std::unique(types.begin(), types.end()), types.end());

    if (types.size() < N) {
      return;
    }

    std::vector<std::vector<std::string>> str(N);
    for (int i = 0; i < M; ++i) {
      str[assignment[i]].push_back(S[i]);
    }

    int count = 0;
    for (const auto& line : str) {
      count += CountTrieSize(line);
    }

    if (count > max_anwser) {
      max_anwser = count;
      answer_count = 1;
    } else if (count == max_anwser) {
      ++answer_count;
    }

    return;
  }

  for (int i = 0; i < N; ++i) {
    assignment[index] = i;
    go(index + 1);
  }
}

int main() {
  std::ios_base::sync_with_stdio(false);
//  std::freopen("/Users/kuznetsovs/Hobby/Console/Console/1.txt", "rb", stdin);
  std::freopen("/Users/kuznetsovs/Hobby/Console/Console/D-small-attempt0.in", "rb", stdin);
  std::freopen("/Users/kuznetsovs/Hobby/Console/Console/D-small-attempt0.out", "wb", stdout);

  int T;
  cin >> T;
  for (int tc = 0; tc < T; ++tc) {

    cin >> M >> N;
    S = std::vector<std::string>(M);
    assignment = std::vector<int>(M);
    for (auto& str : S) {
      cin >> str;
    }

    answer_count = 0;
    max_anwser = 0;
    go(0);

    cout << "Case #" << tc + 1 << ": " << max_anwser << ' ' << answer_count << '\n';
  }
  return 0;
}
