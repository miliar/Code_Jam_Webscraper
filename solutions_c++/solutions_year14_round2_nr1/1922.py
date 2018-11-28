#include <bits/stdc++.h>

using namespace std;

const int MAX_N = 110;

int N;
vector<string> S;

void Input() {
  cin >> N;
  S.resize(N, string(""));
  for (int i = 0; i < N; i++) {
    cin >> S[i];
  }
}

string Minimize(const string& a) {
  string b = "";
  b += a[0];
  for (char c : a) {
    if (b[b.size() - 1] != c) {
      b += c;
    }
  }
  return b;
}

int Count(const string& s, int index, int to) {
  char last = s[0];
  int currentIndex = 0;
  int i = 0;
  while (i < s.size()) {
    if (s[i] != last) {
      currentIndex++;
      last = s[i];
    }
    if (currentIndex == index) {
      break;
    }
    i++;
  }

  int count = 0;
  for (; i < s.size(); i++) {
    if (s[i] != last) {
      break;
    }
    count++;
  }
  return abs(to - count);
}

void Solve() {
  string m = Minimize(S[0]);
  for (int i = 1; i < N; i++) {
    string p = Minimize(S[i]);
    if (p != m) {
      printf("Fegla Won");
      return;
    }
  }

  vector<pair<int, int> > V(m.size(), make_pair(110, -1));
  for (int i = 0; i < N; i++) {
    string s = S[i];
    char last = s[0];
    int count = 1;
    int index = 0;
    for (int j = 1; j < s.size(); j++) {
      if (s[j] == last) {
        count++;
      } else {
        V[index].first = min(V[index].first, count);
        V[index].second = max(V[index].second, count);
        index++;
        last = s[j];
        count = 1;
      }
    }
    V[index].first = min(V[index].first, count);
    V[index].second = max(V[index].second, count);
  }

  int res = 0;
  for (int i = 0; i < V.size(); i++) {
    int minTotal = 110;
    for (int j = V[i].first; j <= V[i].second; j++) {
      int total = 0;
      for (string s : S) {
        total += Count(s, i, j);
      }
      minTotal = min(minTotal, total);
    }
    res += minTotal;
  }
  printf("%d", res);
}

int main(int argc, char **argv) {
  int T;
  scanf("%d", &T);

  for (int test_case = 1; test_case <= T; ++test_case) {
    Input();
    printf("Case #%d: ", test_case);
    Solve();
    printf("\n");
  }
  return 0;
}
