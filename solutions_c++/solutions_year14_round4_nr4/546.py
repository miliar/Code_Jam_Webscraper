#include <limits.h>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <limits>
#include <cassert>
#include <string>
#include <vector>
#include <deque>
#include <fstream>
#include <algorithm>
#include <numeric>
#include <iostream>
#include <iomanip>
#include <sstream>
#include <queue>
#include <iterator>
#include <set>
#include <map>
static const int INF = std::numeric_limits<int>::max();

std::map<int, int> memo;

struct Node {
  std::map<char, int> next;
  char c;

  Node(char c) : c(c) {}
};

int trie(const std::vector<std::string>& v)
{
  std::vector<Node> nodes;
  nodes.push_back(Node(0));

  for(auto& s : v) {
    int i = 0;
    for(auto c : s) {
      assert(i < (int)nodes.size());
      auto& node = nodes[i];
      if(node.next.count(c)) {
        i = node.next[c];
        continue;
      }
      i = (int)nodes.size();
      node.next[c] = i;

      nodes.push_back(Node(c));
    }
  }

  return nodes.size();
}

int trie(const std::vector<std::string>& S, int N,
         const std::vector<int>& alloc)
{
  int res = 0;
  for(int i = 0; i < N; ++i) {
    std::vector<std::string> v;
    for(int j = 0; j < (int)alloc.size(); ++j) {
      if(alloc[j] == i) {
        v.push_back(S[j]);
      }
    }
    res += trie(v);
  }
  return res;
}

bool allocOk(const std::vector<int>& alloc, int N) {
  std::vector<int> used(N);
  for(int i = 0; i < (int)alloc.size(); ++i) {
    ++used[alloc[i]];
  }
  return std::find(std::begin(used), std::end(used), 0) == std::end(used);
}

void check(const std::vector<std::string>& S, int M, int N,
           std::vector<int> alloc)
{
  if(M == 0) {
    if(allocOk(alloc, N)) {
      auto x = trie(S, N, alloc);
      ++memo[x];
    }
    return;
  }

  for(int i = 0; i < N; ++i) {
    alloc[M - 1] = i;
    check(S, M - 1, N, alloc);
  }
}

void solve(const std::vector<std::string>& S, int M, int N)
{
  std::vector<int> alloc(M);

  check(S, M, N, alloc);
}

int main()
{
  int T;
  std::cin >> T;
  for(int test = 1; test <= T; ++test) {
    int M, N;
    std::cin >> M >> N;
    std::vector<std::string> S(M);
    for(int i = 0; i < M; ++i) {
      std::cin >> S[i];
    }

    memo.clear();
    solve(S, M, N);

    auto ans = (*memo.rbegin()).first;

    std::cout << "Case #" << test << ": " << ans << " " << memo[ans]
              << std::endl;
  }
}
