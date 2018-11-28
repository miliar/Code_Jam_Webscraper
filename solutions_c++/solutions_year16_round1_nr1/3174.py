#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>

using namespace std;

void solve(string &S)
{
  string ans = "";
  char first = '\0';
  int size = S.length();
  for (int i = 0; i < size; i++) {
    if (S[i] >= first) {
      // prepend
      ans = S[i] + ans;
      first = S[i];
    } else{
      ans += S[i];
    }
  }
  cout << ans;
}

int main(int argc, char *args[]) {
  if (argc == 2 && strcmp(args[1], "small") == 0) {
    freopen("small.in", "rt", stdin);
    freopen("small.out", "wt", stdout);
  }
  else if (argc == 2 && strcmp(args[1], "large") == 0) {
    freopen("large.in", "rt", stdin);
    freopen("large.out", "wt", stdout);
  }
  else {
    freopen(args[1], "rt", stdin);
    freopen("a.out", "wt", stdout);
  }
  int T;
  string S;
  cin >> T;
  for (int i = 1; i <= T; i++)
  {
    cin >> S;
    printf("Case #%d: ", i);
    // solve
    solve(S);
    cout << endl;
  }
}