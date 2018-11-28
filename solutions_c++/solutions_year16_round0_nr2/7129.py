#include <iostream>
#include <string>
using namespace std;

// char flip_ch(char ch) {
//   if (ch == '-') return '+';
//   else return '-';
// }

// void flip(string &s, int k) {
//   for (int i = 0, j = k-1; i <= j; i++, j--) {
//     char t1 = s[i], t2 = s[j];
//     t1 = flip_ch(t1);
//     t2 = flip_ch(t2);
//     s[i] = t2;
//     s[j] = t1;
//   }
// }

int main() {
  int T;
  cin >> T;

  for (int casen = 1; casen <= T; casen++) {
    cout << "Case #" << casen << ": ";
    string st;
    cin >> st;

    int ans = 0;

    bool in_bad = 0;
    for (int i = 0; i < st.size(); i++) {
      if (st[i] == '-') {
        in_bad =  1;
      }
      else {
        ans += 2 * in_bad;
        in_bad = 0;
      }
    }
    ans += 2 * in_bad;

    cout << ans - (st[0]=='-') << endl;
  }

  return 0;
}
