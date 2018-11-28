#include "cassert"
#include "vector"
#include "iostream"
#include "set"
#include "functional"

int global_ans, global_cnt;

int cost(std::vector<std::string> &bucket) {
  if (bucket.empty()) {
    return 0;
  }
  int ans = 1;
  // std::vector<std::set<char>> nodes;
  std::set<std::string> nodes;
  for (auto &s : bucket) {
    std::string x = "";
    for (int i = 0; i < s.size(); ++i) {
      /*
      if (nodes.size() <= i) {
	nodes.push_back(std::set<char>());
      }
      if (nodes[i].count(s[i]) == 0) {
	++ ans;
	nodes[i].insert(s[i]);
	} */
      x += s[i];
      nodes.insert(x);
    }
  }
  return nodes.size() + 1;
}

void dfs(std::vector<std::string> &vs, 
	 std::vector<std::vector<std::string>> &buckets,
	 int i) {
  if (i == vs.size()) {
    for (auto bucket : buckets) {
      if (bucket.empty()) {
	return;
      }
    }
    int ans = 0;
    for (auto bucket : buckets) {
      ans += cost(bucket);
    }
    if (ans > global_ans) {
      global_ans = ans;
      global_cnt = 1;
    } else if (ans == global_ans) {
      global_cnt += 1;
    }
    return;
  }
  for (int j = 0; j < buckets.size(); ++j) {
    buckets[j].push_back(vs[i]);
    dfs(vs, buckets, i + 1);
    buckets[j].pop_back();
  }
}


int main() {
  int T, t = 1, N, M;
  for (std::cin >> T; t <= T; ++t) {
    std::cout << "Case #" << t << ": ";
    std::cin >> M >> N;
    std::vector<std::string> vs(M);
    for (int i = 0; i < M; ++i) {
      std::cin >> vs[i];
    }
    global_ans = 0, global_cnt = 0;
    std::vector<std::vector<std::string>> buckets(N);
    dfs(vs, buckets, 0);
    std::cout << global_ans << " " << global_cnt << std::endl;
  }
  return 0;
}
