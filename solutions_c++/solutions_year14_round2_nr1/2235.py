#include <string>
#include <vector>
#include <iostream>
#include <utility>
#include <algorithm>
#include <cmath>
#include <set>


using namespace std;


pair<string, vector<int>> make_distinct(string str) {
  string filtered;
  auto duplicates = vector<int>(str.size(), 0);
  for (auto ch: str) {
    if (filtered.size() == 0 || filtered.back() != ch) {
      filtered += ch;
    } else {
      ++duplicates[filtered.size() - 1];
    }
  }
  duplicates.erase(duplicates.begin() + filtered.size(), duplicates.end());
  return make_pair(filtered, duplicates);
}


int cost_diff(vector<int> dups) {
  int maxv = dups[0], minv = dups[0];
  for (auto x: dups){
    maxv = max(maxv, x);
    minv = min(minv, x);
  }
  auto cost = maxv;
  for (auto middle = minv; middle <= maxv; ++middle) {

    auto this_cost = 0;
    for (auto x: dups) {
      this_cost += abs(x - middle);
    }
    cost = min(cost, this_cost);
  }
  return cost;
}




int main() {
  ios_base::sync_with_stdio(false);
  
  int T;
  cin >> T;

  for (int t=1; t<=T; ++t) {
    int N;
    cin >> N;
    auto dup  = vector<vector<int>>(N);
    auto distinct = set<string>();
    for (int i=0; i<N; ++i) {
      string str;
      cin >> str;
      auto p = make_distinct(str);
      distinct.insert(p.first);
      dup[i] = p.second;
    }

    /*
    cout << "dup:\n";
    for (int i=0; i<dup.size(); ++i) {
      for (int j=0; j<dup[i].size(); ++j){
	cout << dup[i][j] << " ";
      }
      cout << '\n';
      } */


    cout << "Case #" << t << ": ";
    if (distinct.size() > 1) {
      cout << "Fegla Won\n";
    } else {
      int costs = 0;
      for (int i=0; i<dup[0].size(); ++i) {
	auto this_loc = vector<int>(dup.size());
	for (int j=0; j<dup.size(); ++j){
	  this_loc[j] = dup[j][i];
	}
	costs += cost_diff(this_loc);
      }
      cout << costs << '\n';
    }
  }
  
  return 0;
}
