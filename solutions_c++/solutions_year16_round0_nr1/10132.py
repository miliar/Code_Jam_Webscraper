#include <bits/stdc++.h>

using namespace std;

long solve(long num) {
  set<int> ans;
  int i = 0;
  while (ans.size() < 10) {
    int aux = num * ++i;
    while (aux) {
        ans.insert(aux%10);
        aux /= 10;
      }
    }
  return (num * i);
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  long num, tc;
  cin >> tc;
  for (int i = 1; i <= tc; i++) {
    cin >> num;
    cout << "Case #" << i << ": ";
    if (num != 0)
      cout << solve(num) << endl;
    else
      cout << "INSOMNIA" << endl;
  }

  return 0;
}
