#include <bits/stdc++.h>
using namespace std;

int ar[30];

string al[] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
string nums = "0123456789";

stack<char> st;

void add(int* ar, int i, int v) {
  for (int j = 0; j < al[i].length(); ++j)
    ar[al[i][j] - 'A'] += v;
}

bool can(int* ar, int i) {
  add(ar, i, -1);
  for (int j = 0; j < al[i].length(); ++j) 
    if (ar[al[i][j] - 'A'] < 0) {
      add(ar, i, 1);
      return false;
    }
  add(ar, i, 1);
  return true;
}

bool find(int* ar, int p = 0) {
  int c = 0;
  for (int i = 0; i < 26; ++i)
    c += ar[i] != 0;
  if (c == 0) return true;
  for (int i = p; i < nums.length(); ++i) {
    if (can(ar, i)) {
      st.push(nums[i]);
      add(ar, i, -1);
      if (find(ar, i)) return true;
      st.pop();
      add(ar, i, 1);
    }
  }
  return false;
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int t; cin >> t;
  int tc = 1;
  while (t--) {
    for (int i = 0; i < 30; ++i)
      ar[i] = 0;
    string s; cin >> s;
    for (int i = 0; i < s.length(); ++i)
      ar[s[i] - 'A']++;
    find(ar);
    string ans = "";
    while (!st.empty()) {
      ans += st.top();
      st.pop();
    }
    sort(ans.begin(), ans.end());
    cout << "Case #" << tc++ << ": " << ans << "\n";
  }

  return 0;
}