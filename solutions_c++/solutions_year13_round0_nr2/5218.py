#include<iostream>
#include<string>
#include<vector>

using namespace std;

bool check(vector< vector<int> > lawn, int m, int n);

int main(int argv, char **argc) {
  int t;

  cin >> t;

  for (int i = 0; i < t; ++i) {
    int m, n;
    cin >> n; 
    cin >> m;
    vector< vector<int> > lawn;
    for (int a = 0; a < n; ++a) {
      vector<int> row;
      for (int b = 0; b < m; ++b) {
        int x;
        cin >> x;
        row.push_back(x);
      }
      lawn.push_back(row);
    } 
    
    cout << "Case #" << i+1 << ": ";
    if (check(lawn, m, n)) {
      cout << "YES" << endl;
    } else {
      cout << "NO" << endl;
    }
  }

  return 0;
}

bool check(vector< vector<int> > lawn, int m, int n) {
  // For each number on the lawn, it must be the highest
  // either in a row or a column;
  vector<int> row_highests;
  vector<int> col_highests;
  for (int i = 0; i < n; ++i) {
    vector<int> row = lawn[i];
    int highest = -1;
    for (int j = 0; j < m; ++j) {
      if(row[j] > highest) {
        highest = row[j];
      }
    }

    row_highests.push_back(highest);
  }
  for (int i = 0; i < m; ++i) {
    int highest = -1;
    for (int j = 0; j < n; ++j) {
      if(lawn[j][i] > highest) {
        highest = lawn[j][i];
      }
    }

    col_highests.push_back(highest);
  }


  for (int i = 0; i < n; ++i) {
    for (int j = 0; j < m; ++j) {
      int block = lawn[i][j];
      if (block != row_highests[i] && block != col_highests[j]) {
        return false;
      }
    }
  }

  return true;
}

