#include <bits/stdc++.h>

using namespace std;

#define REP(i,n) for(int (i)=0;(i)<(int)(n);(i)++)

void main2() {
  int N;
  string s;

  cin >> N >> s;

  int res = 0, tmp = 0;
  REP(i,s.length()) {
    if (tmp < i && s[i] != '0') {
      res += i - tmp;
      tmp += res;
    }
    tmp += s[i] - '0';
  }

  cout << res << endl;
}

int main() {
  int T;

  scanf("%d\n", &T);
  REP(t,T) {
    printf("Case #%d: ", t + 1);
    main2();
  }

  return 0;
}
