#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;

int solve(char s[]) {
  int len = strlen(s);

  int res = 0;
  for ( int i = len - 1 ; i >= 0 ; i-- ) {
    if ( s[i] == '-' ) {
      for ( int j = 0 ; j <= i ; j++ ) {
        if ( s[j] == '-' ) s[j] = '+';
        else if ( s[j] == '+' ) s[j] = '-';
      }
      res++;
    }
  }
  return res;
}

int main() {
  //freopen("input2.txt", "r", stdin);
  //freopen("output2.txt", "w", stdout);
  int T, kase = 1;
  cin >> T;
  while ( T-- ) {
    char s[105];
    cin >> s;
    cout << "Case #" << kase++ << ": " << solve(s) << endl;
  }

  return 0;
}
