#include <algorithm>
#include <cassert>
#include <cstdio>
#include <cstdlib>
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
#define PROBLEM_ID "source"

#pragma comment(linker, "/STACK:36777216")

typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<vvi> vvvi;
typedef vector<bool> vb;
typedef long long ll;
typedef pair<int, int> pii;

enum class Num {I, J, K, One};

pair<Num, int> DivLeft(pair<Num, int> a, pair<Num, int> b) {
  if (b.first == Num::One) return pair<Num, int>(a.first, a.second * b.second);
  
  if (a.first == b.first) return pair<Num, int>(Num::One, a.second * b.second);
  if (a.first == Num::One) return pair<Num, int>(b.first, -1 * a.second * b.second);

  if (a.first == Num::I && b.first == Num::J) {
    return pair<Num, int>(Num::K, a.second * b.second);
  }
  if (a.first == Num::I && b.first == Num::K) {
    return pair<Num, int>(Num::J, -1 * a.second * b.second);
  }
  if (a.first == Num::J && b.first == Num::I) {
    return pair<Num, int>(Num::K, -1 * a.second * b.second);
  }
  if (a.first == Num::J && b.first == Num::K) {
    return pair<Num, int>(Num::I, a.second * b.second);
  }
  if (a.first == Num::K && b.first == Num::I) {
    return pair<Num, int>(Num::J, a.second * b.second);
  }
  if (a.first == Num::K && b.first == Num::J) {
    return pair<Num, int>(Num::I, -1 * a.second * b.second);
  }
  assert(false);
}


pair<Num, int> Mul(pair<Num, int> a, pair<Num, int> b) {
  if (a.first == Num::One) return pair<Num, int>(b.first, a.second * b.second);
  if (b.first == Num::One) return pair<Num, int>(a.first, a.second * b.second);

  if (a.first == b.first) return pair<Num, int>(Num::One, -1 * a.second * b.second);
  if (a.first == Num::I && b.first == Num::J) {
    return pair<Num, int>(Num::K, a.second * b.second);
  }
  if (a.first == Num::I && b.first == Num::K) {
    return pair<Num, int>(Num::J, -1 * a.second * b.second);
  }
  if (a.first == Num::J && b.first == Num::I) {
    return pair<Num, int>(Num::K, -1 * a.second * b.second);
  }
  if (a.first == Num::J && b.first == Num::K) {
    return pair<Num, int>(Num::I, a.second * b.second);
  }
  if (a.first == Num::K && b.first == Num::I) {
    return pair<Num, int>(Num::J, a.second * b.second);
  }
  if (a.first == Num::K && b.first == Num::J) {
    return pair<Num, int>(Num::I, -1 * a.second * b.second);
  }
  assert(false);
}

vector<pair<Num, int>> BuildNums(const string& line) {
  vector<pair<Num, int>> answer;
  for (int i = 0; i < line.size(); ++i) {
    Num num;
    if (line[i] == 'k')
      num = Num::K;
    else if (line[i] == 'i')
      num = Num::I;
    else if (line[i] == 'j')
      num = Num::J;
    else assert(false);

    answer.push_back(pair<Num, int>(num, 1));
  }
  return answer;
}

vector<pair<Num, int>> BuildRepeat(const string& line, int times) {
  vector<pair<Num, int>> result;

  auto nums = BuildNums(line);
  for (int i = 0; i < times; ++i) {
    for (auto num : nums) {
      result.push_back(num);
    }
  }
  return result;
}

pair<Num, int> Mul(vector<pair<Num, int>>::iterator begin, vector<pair<Num, int>>::iterator end) {
  pair<Num, int> result = pair<Num, int>(Num::One, 1);
  for (auto it = begin; it < end; ++it) {
    result = Mul(result, *it);
  }
  return result;
}

bool CanIjk(vector<pair<Num, int>>& nums) {
  if (nums.size() < 3)
    return false;

  pair<Num, int> left = nums[0];
  pair<Num, int> mid = nums[1];
  pair<Num, int> right = Mul(nums.begin() + 2, nums.end());

  pair<Num, int> all = Mul(nums.begin(), nums.end());
  
  auto x = Mul(left, mid);
  x = Mul(x, right);
  assert(x.first == all.first && x.second == all.second);

  for (int first_j = 1; first_j + 1 < nums.size(); ++first_j) {
    for (int first_k = first_j + 1; first_k < nums.size(); ++first_k) {
      if (left.first == Num::I && left.second == 1 &&
        mid.first == Num::J && mid.second == 1 &&
        right.first == Num::K && right.second == 1) {
        return true;
      }
      mid = Mul(mid, nums[first_k]);
      right = DivLeft(right, nums[first_k]);
    }

    left = Mul(left, nums[first_j]);
    mid = nums[first_j + 1];
    right = DivLeft(all, Mul(left, mid));
  }
  return false;
}

int main() {
  freopen(PROBLEM_ID".in", "r", stdin);
  freopen(PROBLEM_ID".out", "w", stdout);
  int tests; 
  cin >> tests;
  for (int test_index = 0; test_index < tests; ++test_index) {
    int L, X;
    cin >> L >> X;
    string line;
    getline(cin, line);
    getline(cin, line);

    assert(line.length() == L);
    vector<pair<Num, int>> nums = BuildRepeat(line, X);
    bool res = CanIjk(nums);

    cout << "Case #" << test_index + 1 << ": " << (res ? "YES" : "NO") << endl;
  }
  return 0;
}
