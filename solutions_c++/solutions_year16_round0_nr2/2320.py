#include <iostream>
#include <set>

using namespace std;

void solve(string str) {
  int res = 0;
  for (int i = 1; i < str.length(); i++) {
    if (str[i] != str[i-1]) res++;
  }
  if (str[str.length()-1] == '-') res++;
  cout << res << endl;
}

int main() {
  int N;
  cin >> N;
  for (int i = 0; i < N; i++) {
    string str;
    cin >> str;
    cout << "Case #" << (i+1) << ": ";
    solve(str);
  }

  return 0;
}
