#include <bits/stdc++.h>

using namespace std;

template <typename T>
void answer(int test, T answer) {
  cout << "Case #" << test << ": " << answer << endl;
}

template<typename T>
inline void normalize(pair<T, T>& p) {
  if (p.first > p.second) {
    swap(p.first, p.second);
  }
}

template <typename T>
ostream& operator<<(ostream& out, vector<T> v) {
  out << "{";
  for (T t: v) {
    out << t + 1 << ",";
  }
  out << "}";
  return out;
}

int n;
int bff[1000];

int ans;

int sinks[5000];

void processChain(int i) {
  vector<int> chain { i };
  unordered_set<int> chain_s; chain_s.insert(i);

  for (;;) {
    int next = bff[chain.back()];

    if (chain_s.find(next) == chain_s.end()) {
      chain.push_back(next);
      chain_s.insert(next);

    } else if (chain.size() >= 2 && next == chain[chain.size() - 2]) {
      chain.pop_back();

      int sink = chain.back();

      sinks[sink] = max(sinks[sink], (int) chain.size());

      //cout << "chain: " << chain << endl;

      return;

    } else if (next == chain.front()) {
      //cout << "loop: " << (int) chain.size() << ": " << chain << endl;

      ans = max(ans, (int) chain.size());
      return;
    } else {
      return;
    }
  }
}

void solve(int test) {
  cin >> n;

  for (int i = 0; i < n; i++) {
    cin >> bff[i];
    bff[i]--;
  }

  fill(sinks, sinks + 5000, 0);

  ans = 1;

  for (int i = 0; i < n; i++) {
    processChain(i);
  }

  int possibleAns = 0;

  for (int i = 0; i < n; i++) {
    possibleAns += sinks[i];
  }

  ans = max(ans, possibleAns);

  answer(test, ans);
}

int main() {
  int t;
  cin >> t;

  for (int i = 0; i < t; i++) {
    solve(i + 1);
  }
}
