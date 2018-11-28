#include <iostream>
#include <string>

using namespace std;

void Reverse(string& s, int size) {
  for (int i = 0; i < size / 2; ++i) {
    swap(s[i], s[size - 1 - i]);
  }

  for (int i = 0; i < size; ++i) {
    if (s[i] == '-') s[i] = '+';
    else s[i] = '-';
  }
}

void Flip(string& s, int size, int cnt, int* ans) {
  if (size <= 0) {
    if (*ans == -1) *ans = cnt;
    else *ans = min(cnt, *ans);
  }

  if (*ans != -1 && cnt >= *ans) return;

  if (s[size - 1] == '+') Flip(s, size - 1, cnt, ans);
  else {
    if (s[0] == '-') {
      Reverse(s, size);
      Flip(s, size - 1, cnt + 1, ans);
    } else {
      string original = s;
      for (int i = 0; i < size - 1; ++i) {
        s = original;
        if (s[i] == '+') {
          Reverse(s, i + 1);
          Reverse(s, size);
          Flip(s, size - 1, cnt + 2, ans);
        }
      }
    }
  }
}

int main() {
  int t;
  cin >> t;
  for (int ci = 1; ci <= t; ++ci) {
    string s;
    cin >> s;

    int ans = -1;
    Flip(s, s.size(), 0, &ans);
    cout << "Case #" << ci << ": " << ans << endl;
  }

  return 0;
}
