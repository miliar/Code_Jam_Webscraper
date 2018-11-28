#include <iostream>
#include <vector>
using namespace std;

void run() {
  string s;
  cin >> s;
  int flag = 0;
  if (s[0] == '-')
    flag = 1;
  int seg = 0;
  for (size_t i = 0; i < s.size(); ++i) {
    if (s[i] == '-' && (i == 0 || s[i - 1] != s[i]))
      seg++;
  }
  cout << seg * 2 - flag << endl;
}

int main() {
  int n;
  cin >> n;
  for (int i = 1; i <= n; ++i) {
    cout << "Case #" << i << ": ";
    run();
  }
}
