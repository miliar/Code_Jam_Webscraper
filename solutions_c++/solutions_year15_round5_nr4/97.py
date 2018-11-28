#include <iostream>
#include <algorithm>
#include <vector>
#include <cstdio>
#include <cstring>
#include <map>

using namespace std;

vector<long long> sol;

void solve(map<long long, long long> freq) {
  if (freq.size() == 1) {
    while (freq[0] > 1) {
      sol.push_back(0);
      freq[0] /= 2;
    }
    return;
  }

  map<long long, long long> nfreq;
  long long mx = (--freq.end())->first;
  if (mx <= 0) {
    for (auto it : freq) {
      nfreq[-it.first] = it.second;
    }
    int pos = sol.size();
    solve(nfreq);
    for (int i = pos; i < sol.size(); i++) {
      sol[i] *= -1;
    }
    return;
  }

  long long v = 0;
  if (freq[mx] == 1) {
    v = mx - (----freq.end())->first;
    vector<long long> keys;
    for (auto it : freq) {
      keys.push_back(it.first);
    }
    for (auto it : keys) {
      freq[it + v] -= freq[it];
      if (freq[it]) {
        nfreq[it] = freq[it];
      }
    }
  } else {
    for (auto it : freq) {
      nfreq[it.first] = it.second / 2;
    }
  }
  sol.push_back(v);

  solve(nfreq);
}

int main() {
  int T; cin >> T;
  for (int t = 1; t <= T; t++) {
    cout << "Case #" << t << ":";
    long long P;
    cin >> P;

    vector<long long> A(P);
    for (int i = 0; i < P; i++) {
      cin >> A[i];
    }
    map<long long, long long> freq;
    for (int i = 0; i < P; i++) {
      long long f;
      cin >> f;
      freq[A[i]] = f;
    }

    sol.clear();
    solve(freq);
    sort(sol.begin(), sol.end());
    for (int i = 0; i < sol.size(); i++) {
      cout << " " << sol[i];
    }
    cout << endl;
  }
  return 0;
}
