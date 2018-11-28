#include <algorithm>
#include <cstdio>
#include <cstring>
#include <unordered_map>
#include <utility>
#include <vector>
#include <queue>
#include <iterator>
#include <iostream>

using namespace std;

vector<bool> rev_flip(vector<bool> bv, size_t r) {
  reverse(bv.begin(), bv.begin() + r);
  for(size_t i = 0; i < r; ++i) bv[i] = !bv[i];
  return bv;
}

unsigned char shortest_path(const vector<bool> & bv) {
  vector<bool> target(bv.size(), true);

  unordered_map<vector<bool>, unsigned char> dist;
  queue<pair<unsigned char, vector<bool>>> explore;

  explore.push(make_pair(0, bv));

  while(dist.find(target) == dist.end()) {
    auto && node = explore.front();
    auto iter = dist.find(node.second);
    if(iter == dist.end()) {
      dist[node.second] = node.first;
      for(size_t r = 1; r <= bv.size(); ++r)
        explore.push(make_pair(node.first+1, rev_flip(node.second, r)));
    }

    explore.pop();
  }

  return dist[target];
}

int main() {
  unsigned T;
  scanf("%u", &T);

  for(unsigned i = 1; i <= T; ++i) {
    char bvs[1000];
    scanf("%s", bvs);

    vector<bool> bv;
    for(unsigned j = 0; j  < strlen(bvs); ++j)
      bv.push_back(bvs[j] == '+');

    printf("Case #%u: %u\n", i, shortest_path(bv));
  }
}
