#include <stdlib.h>
#include <iostream>
#include <vector>

using namespace std;

vector<vector<bool> > square(int N)
{
  return vector<vector<bool> >(N, vector<bool>(N, false));
}

bool valid(int N, vector<vector<bool> > use)
{
  //for (int i = 0; i < N; i++) { // check that everyone can do something
  //  bool something = false;
  //  for (int j = 0; j < N; j++) {
  //    if (use[i][j]) {
  //      something = true;
  //      break;
  //    }
  //  }
  //  if (!something) {
  //    return false;
  //  }
  //}
  for (int i = 0; i < N; i++) { // check machine
    int index = -1;
    int count = 0;
    int count2 = 0;
    for (int j = 0; j < N; j++) { // find workers who can use this machine
      if (use[j][i]) {
        count++;
        if (index == -1) { // first worker
          index = j;
          for (int k = 0; k < N; k++) {
            count2 += use[j][k];
          }
        }
        else {
          for (int k = 0; k < N; k++) {
            if (use[j][k] != use[index][k]) {
              return false;
            }
          }
        }
      }
    }
    if (index == -1) { // no one can use this machine
      return false;
    }
    if (count != count2) {
      return false;
    }
  }
  return true;
}

int solve(int N, vector<vector<bool> > use)
{
  vector<pair<int, int> > cant;
  for (int i = 0; i < N; i++) {
    for (int j = 0; j < N; j++) {
      if (!use[i][j]) {
        cant.push_back(pair<int, int>(i, j));
      }
    }
  }

  int ans = cant.size();
  for (int i = 0; i < (1 << cant.size()); i++) {
    vector<vector<bool> > temp = use;
    int num = 0;
    for (int j = 0; j < cant.size(); j++) {
      if ((i & (1 << j)) != 0) {
        temp[cant[j].first][cant[j].second] = true;
        num++;
      }
    }
    if (valid(N, temp)) {
      ans = min(ans, num);
    }
  }
  return ans;
}

int main()
{
  int T;
  cin >> T;
  for (int t = 1; t <= T; t++) {
    int N;
    cin >> N;
    vector<vector<bool> > use = square(N);
    for (int i = 0; i < N; i++) {
      for (int j = 0; j < N; j++) {
        char c;
        cin >> c;
        use[i][j] = (c == '1');
      }
    }
    cout << "Case #" << t << ": " << solve(N, use) << "\n";
  }
  return 0;
}

