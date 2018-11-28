#include<iostream>
#include<string>
#include<vector>

using namespace std;

bool notAll(vector<bool> v) {
  for (int i = 0; i < v.size(); i++) {
    if (!v[i]) {
      return true;
    }
  }
  return false;
}

bool lastTwo(vector<bool> v) {
  for (int i = 2; i < v.size(); i++) {
    if (!v[i]) {
      return false;
    }
  }
  if (v.size() > 1) {
    if (v[0] && !v[1]) {
      return true;
    }
  }
  return false;
}

int main() {
  int T;
  cin >> T;
  for (int t = 1; t <= T; t++) {
    string s;
    cin >> s;
    vector<bool> v;
    for (int i = 0; i < s.length(); i++) {
      if (s[i] == '+') {
        v.push_back(true);
      } else {
        v.push_back(false);
      }
    }
    int y = 0;
    while (notAll(v)) {
      if (v[0]) {
        int n = 0;
        while(v[++n]);
        for (int i = 0; i < n / 2; i++) {
          bool aux = v[i];
          v[i] = v[n - i - 1];
          v[n - i - 1] = aux;
        }
        for (int i = 0; i < n; i++) {
          v[i] = !v[i];
        }
      } else {
        int n = v.size();
        while(v[--n]);
        n++;
        for (int i = 0; i < n / 2; i++) {
          bool aux = v[i];
          v[i] = v[n - i - 1];
          v[n - i - 1] = aux;
        }
        for (int i = 0; i < n; i++) {
          v[i] = !v[i];
        }
      }
      y++;
    }
    cout << "Case #" << t << ": " << y << endl;
  }
  return 0;
}
