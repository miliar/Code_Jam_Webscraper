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

int CountPeople(vector<int> p) {
  sort(p.begin(), p.end());
  int count = 0;
  int additional = 0;
  for (const auto& v : p) {
    if (v > count) {
      additional += (v - count);
      count += (v - count);
    }
    count++;
  }
  return additional;
}

vector<int> ReadVec() {
  int smax;
  cin >> smax;
  
  char digit = getchar();
  while (digit < '0' || digit > '9') digit = getchar();

  vector<int> result;

  for (int i = 0; i < smax + 1; i++) {
    int count = digit - '0';
    for (int j = 0; j < count; ++j) {
      result.push_back(i);
    }
    digit = getchar();
  }
  return result;
}

int main() {
  freopen(PROBLEM_ID".in", "r", stdin);
  freopen(PROBLEM_ID".out", "w", stdout);
  int tests;
  cin >> tests;
  for (int test_index = 0; test_index < tests; ++test_index) {
    vector<int> p = ReadVec();
    cout << "Case #" << test_index + 1 << ": " << CountPeople(p) << endl;
  }
  return 0;
}
