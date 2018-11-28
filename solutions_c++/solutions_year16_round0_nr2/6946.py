#include <iostream>
#include <string>
using namespace std;

int main() {
  int N; string l;
  cin >> N; getline(cin, l);
  for (int num = 1; num <= N; ++num) {
    int ans = 1; getline(cin, l);
    for (int i = 1; i < l.length(); ++i)
      if (l[i] != l[i-1]) ++ans;
    if (l[l.length()-1] == '+') --ans;

    cout << "Case #" << num << ": " << ans << endl;
  }
  return 0;
}
