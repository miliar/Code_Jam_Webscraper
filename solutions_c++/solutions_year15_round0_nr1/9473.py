#include <iostream>
#include <vector>
#include <string>


using namespace std;
int to_number(char s) {
  return s - '0';
}
int main() {
  int T, S;
  string a;
  cin >> T;
  for (int t = 0; t < T; ++t) {
    cin >> S;
    getline(cin, a);
    int m = 0;
    int total = 0;
    int i = 0;
    while (a[i] == ' ') ++i;
    if (i < a.size()) {
      total = to_number(a[i]);
      ++i;
    }
    for (int j = 1; j <= S; ++j, ++i) {
      if (to_number(a[i]) > 0 && j > total) {
        m += j - total;
        total = j;
      }
      total += to_number(a[i]);
    }
    cout << "Case #" << t+1 << ": " << m << endl;
  }
}
