#include <iostream>
#include <unordered_map>
#include <queue>

using namespace std;

bool check(string s) {
  for (int i=0; i<s.size(); i++) {
    if (s[i] == '-') {
      return false;
    }
  }
  return true;
}

string flip(string s, int top) {
  for (int i=0; i<top/2; i++) {
    char tmp = s[i];
    s[i] = s[top-i-1];
    s[top-i-1] = tmp;
  }

  for (int i=0; i<top; i++) {
    if (s[i] == '-')
      s[i] = '+';
    else
      s[i] = '-';
  }

  return s;
}

int solve(string N) {
  if (check(N)) {
    return 0;
  }

  unordered_map<string, bool> seen;

  seen[N] = true;

  queue<pair<string, int> > q;
  q.push(make_pair(N, 0));

  while (!q.empty()) {
    auto entry = q.front();
    q.pop();

    string current = entry.first;
    int steps = entry.second;
    steps++;

    for (int i=1; i<=N.size(); i++) {
      // flip top i pancakes

      auto flipped = flip(current, i);

      if (seen[flipped]) {
        continue;
      }

      seen[flipped] = true;

      // all good ?
      if (check(flipped))
        return steps;

      q.push(make_pair(flipped, steps));
    }
  }

  return 0;
}

int main() {
  int T;
  cin >> T;

  string N;

  for (int i=0; i<T; i++) {
    cin >> N;

    int result = solve(N);

    cout << "Case #" << i+1 << ": " << result << endl;
  }

  return 0;
}
