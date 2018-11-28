#include <bits/stdc++.h>

using namespace std;

int main() {
  int t;
  cin >> t;
  for (int tc = 1; tc <= t; tc++) {
    char s[105];
    cin >> s;
    int len = strlen(s);   
    int k = (s[len - 1] == '-');
    int sum = 0;
    for (int j = 0; j < len - 1; j++)
      if (s[j] != s[j + 1])
        sum++;             
    sum += k;
    cout << "Case #" << tc << ": " << sum << endl;
  }
  return 0;
}
