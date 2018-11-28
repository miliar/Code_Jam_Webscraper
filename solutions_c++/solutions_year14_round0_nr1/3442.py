#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
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
#define PROBLEM_ID "A"

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<vvi> vvvi;
typedef vector<bool> vb;
typedef long double ld;
typedef pair<int, int> pii;
typedef long long ll;
typedef vector<ll> vl;
typedef vector<vl> vvl;
typedef vector<vvl> vvvl;
typedef pair<ll, ll> pll;

void ReadAnswer(vvi& field, int& row) {
  cin >> row;
  --row;
  field.assign(4,vi(4));
  for (int i = 0; i < 4; ++i) {
    for (int j = 0; j < 4; ++j) {
      cin >> field[i][j];
    }
  }
}

int main() {
  freopen(PROBLEM_ID".in", "r", stdin);
  freopen(PROBLEM_ID".out", "w", stdout);
  int tests;
  cin >> tests;
  for (int test_index = 0; test_index < tests; ++test_index) {
    vvi first_field, second_field;
    int first_row, second_row;
    ReadAnswer(first_field, first_row);
    ReadAnswer(second_field, second_row);
    set<int> answers;
    for (int col = 0; col < 4; ++col) {
      int card = first_field[first_row][col];
      bool good = false;
      for (int col2 = 0; col2 < 4; ++col2) {
        if (second_field[second_row][col2] == card) {
          good = true;
          answers.insert(card);
          break;
        }
      }
    }
    cout << "Case #" << (test_index + 1) << ": ";
    if (answers.empty()) {
      cout << "Volunteer cheated!" << endl;
    } else if (answers.size() == 1) {
      cout << *answers.begin() << endl;
    } else {
      cout << "Bad magician!" << endl;
    }
  }
  return 0;
}
