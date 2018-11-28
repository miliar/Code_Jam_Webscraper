#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector< vector<int> > GetTable() {
  int n, m;
  scanf("%d %d", &n, &m);
  vector< vector<int> > result (n, vector<int>(m));
  for (size_t row = 0; row < n; ++row) {
    for (size_t column = 0; column < m; ++column) {
      int value;
      scanf("%d", &value);
      result[row][column] = value;
    }
  }
  return result;
}

int GetMaxRow(const vector< vector<int> >& table, size_t row) {
  int max_value = -1;
  for (size_t column = 0; column < table[row].size(); ++column) {
    max_value = max(max_value, table[row][column]);
  }

  return max_value;
}

int GetMaxColumn(const vector< vector<int> >& table, size_t column) {
  int max_value = -1;
  for (size_t row = 0; row < table.size(); ++row) {
    max_value = max(max_value, table[row][column]);
  }
  return max_value;
}

vector< vector<int> > Cut(const vector< vector<int> >& table) {
  vector< vector<int> > result(table.size(), vector<int>(table[0].size(), 100));

  for (size_t row = 0; row < table.size(); ++row) {
    int max_value = GetMaxRow(table, row);
    for (size_t column = 0; column < table[row].size(); ++column) {
      result[row][column] = min(result[row][column], max_value);
    }
  }

  for (size_t column = 0; column < table[0].size(); ++column) {
    int max_value = GetMaxColumn(table, column);
    for (size_t row = 0; row < table.size(); ++row) {
      result[row][column] = min(result[row][column], max_value);
    }
  }

  return result;
}

void Solve() {
  int T;
  scanf("%d\n", &T);
  for (int test_number = 1; test_number <= T; ++test_number) {
    vector< vector<int> > table = GetTable();
    bool possible = (Cut(table) == table);
    printf("Case #%d: %s\n", test_number, possible ? "YES" : "NO");
  }
}

int main() {
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
  Solve();
  return 0;
}