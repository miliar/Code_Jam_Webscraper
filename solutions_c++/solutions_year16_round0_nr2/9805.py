#include <iostream>

using namespace std;

int main() {
  int n;
  cin >> n;
  for (int i = 0; i < n; i++) {
    string in;
    cin >> in;
    int ans = 0;
    while(in.find('-') != string::npos) {
      bool minus = in[0] == '-' ? true : false;
      int flip = 0;
      for (int j = 1; j < in.size(); j++) {
        if ((minus && in[j] == '-') || (!minus && in[j] == '+')) {
          flip++;
        } else {
          break;
        }
      }
      if (minus) {
        in.replace(in.begin(), in.begin()+flip+1, flip+1, '+');
      } else {
        in.replace(in.begin(), in.begin()+flip+1, flip+1, '-');
      }

      ans++;
    }
    cout << "Case #" << i+1 << ": " << ans << endl;
  }
  return 0;
}
