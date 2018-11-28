#include <iostream>
#include <cstdio>
#include <vector>
#include <cstring>
#include <algorithm>
#include <utility>

using namespace std;

int m[100][100];
int mm[100][100];
bool used[100][100];
int N, M;

bool cansend(pair<int, int> t, int rc) {
  if (rc == 0) {
    for (int i = 0; i < M; ++i) {
      if (mm[t.first][i] > m[t.first][t.second] &&
          used[t.first][i])
        return false;
    }
  } else {
    for (int i = 0; i < N; ++i) {
      if (m[i][t.second] > m[t.first][t.second] &&
          used[i][t.second])
        return false;
    }
  }
  return true;
}


void send(pair<int, int> t, int rc) {
  if (rc == 0) {
    for (int i = 0; i < M; ++i) {
      mm[t.first][i] = m[t.first][t.second];
    }
  } else {
    for (int i = 0; i < N; ++i) {
      mm[i][t.second] = m[t.first][t.second];
    }
  }
  used[t.first][t.second] = true;
}

bool solve(vector< pair<int, int> > t) {
    for (int i = 0; i < t.size(); ++i) {
      if (!used[t[i].first][t[i].second]) {
        if (cansend(t[i], 0)) {
          send(t[i], 0);
        } else if (cansend(t[i], 1)) {
          send(t[i], 1);
        } else {
          return false;
        }
      }
    }
    return true;
  }

  bool mycmp(pair<int, int> a, pair<int, int> b) {
    return m[a.first][a.second] > m[b.first][b.second];
  }
  
  void printM() {
    for (int i = 0; i < N; ++i) {
      for (int j = 0; j < M; ++j) {
        printf("%d", m[i][j]);
      }
      cout << endl;
    }
  }

  void printMM() {
    for (int i = 0; i < N; ++i) {
      for (int j = 0; j < M; ++j) {
        printf("%d", mm[i][j]);
      }
      cout << endl;
    }
  }

  
int main() {
  int T;
  cin >> T;
  for (int t = 1; t <= T; ++t) {
    cin >> N >> M;
    memset(m, 0, sizeof(m));
    for (int i = 0; i < N; ++i)
      for (int j = 0; j < M; ++j)
        mm[i][j]= 100;
    memset(used, false, sizeof(used));
    for (int i = 0; i < N; ++i) {
      for (int j = 0; j < M; ++j) {
        int e; cin >> e;
        m[i][j] = e;
      }
    }
    vector< pair<int, int> > ta;
    for (int i = 0; i < N; ++i) {
      for (int j = 0; j < M; ++j) {
        ta.push_back(make_pair(i,j));
      }
    }
    sort(ta.begin(), ta.end(), mycmp);
    if (solve(ta)) {
      //      printM();
      //      cout << endl;
      //      printMM();
      printf("Case #%d: YES\n", t);
    } else {
      //      printM();
      //      cout << endl;
      //      printMM();
      printf("Case #%d: NO\n", t);
    }
  }
  return 0;
}
