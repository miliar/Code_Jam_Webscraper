#include <iostream>
#include <vector>
#include <utility>
#include <string>

using namespace std;


bool evacuated(const vector<int>& p) {
  for (int i = 0; i < p.size(); ++i) {
    if (p[i] > 0) return false;
  }
  return true;
}

bool majority(const vector<int>& p) {
  int count = 0;
  for (int i = 0; i < p.size(); ++i) {
    count += p[i];
  }

  for (int i = 0; i < p.size(); ++i) {
    if (p[i] > count / 2) return true;
  }
  return false;
}

pair<int, int> next_pair(vector<int>& p) {
  for (int i= 0; i < p.size(); ++i) {
    if (p[i] > 0) {
      for (int j = 0; j < p.size(); ++j) {
        if (p[j] > 0) {
          p[i]--;
          p[j]--;
          if (!majority(p)) { 
            return {i, j};
          } else {
             p[i]++;
             p[j]++;
          }
        }
      }
    }
  }
  return {-1, -1};
}

int next_p(vector<int>& p) {
  for (int i= 0; i < p.size(); ++i) {
    if (p[i] > 0) {
      p[i]--;
      if (!majority(p)) { 
        return i;
      } else {
        p[i]++;
      }
    }
  }
  return -1;
}

int main() {
  int T;
  cin >> T;
  for (int t = 1; t <= T; ++t) {
    int N;
    cin >> N;
    vector<int> P(N, 0);
    for (int k = 0; k < N; ++k) {
      cin >> P[k];
    }
    string res;
    while (!evacuated(P)) {
      res.push_back(' ');
      pair<int, int> pp = next_pair(P);
      if (pp.first >= 0) {
        res.push_back(pp.first + 'A');
        res.push_back(pp.second + 'A');
      } else {
        int m = next_p(P);
         res.push_back(m + 'A');
      }
    }
    cout << "Case #" << t << ":" << res << endl;  
  }
  return 0;
}
