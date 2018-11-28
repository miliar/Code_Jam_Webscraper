#include <cstdio>
#include <iostream>

using namespace std;

int main() {

  freopen("in", "r", stdin);
  freopen("out", "w", stdout);

  int T;
  scanf("%d", &T);

  for (int t=1; t<=T; ++t) {
    printf("Case #%d: ", t);

    int smax;
    cin >> smax;

    char str[smax+2];
    cin >> str;
    int s[smax+1];
    for (int i=0; i<=smax; ++i) s[i] = str[i] - '0';

    int result = 0;
    int standing = 0;
    for (int i=0; i<=smax; ++i) {
      if (standing<i) {
      result += i-standing;
      standing += i-standing;
      }
      standing += s[i];
    }
    cout << result << endl;

  }
}
