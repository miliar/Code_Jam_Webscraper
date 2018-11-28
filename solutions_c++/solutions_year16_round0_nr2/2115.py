//mishraiiit
#include<bits/stdc++.h>
#define ll long long int
#define fastScan ios_base::sync_with_stdio(0); cin.tie(NULL);
using namespace std;
typedef pair <ll, ll> pll;

#ifdef TRACE
  #include "trace.h"
#else
  #define trace1(x)
  #define trace2(x, y)
  #define trace3(x, y, z)
  #define trace4(a, b, c, d)
  #define trace5(a, b, c, d, e)
  #define trace6(a, b, c, d, e, f)
#endif
string s;
char get(char c, bool r) {
  if(r == false) return c;
  else if(c == '+') return '-';
  return '+';
}


int solve(int top, int bottom, int rev) {
  if(top == bottom) return (get(s[top], rev) == '-');
  char t = get(s[top], rev);
  char b = get(s[bottom], rev);
  if(b == '+') {
    if(top < bottom) return solve(top, bottom - 1, rev);
    else return solve(top, bottom + 1, rev);
  } else if(t == '+' && b == '-') {
    if(top < bottom) {
      while(get(s[top], rev) == '+') top++;
      return 2 + solve(bottom, top, 1 - rev);
    } else {
      while(get(s[top], rev) == '+') top--;
      return 2 + solve(bottom, top, 1 - rev);
    }
  } else {
    if(top < bottom) return 1 + solve(bottom, top + 1, 1 - rev);
    else return 1 + solve(bottom, top - 1, 1 - rev);
  }
}

int main() {
    fastScan;
    int t;
    cin >> t;
    for(int i = 1; i <= t; i++) {
      cin >> s;
      int top = 0, bottom = s.size() - 1;
      int ans = 0;
      bool rev = false;
      cout << "Case #" << i << ": ";
      cout << solve(0, s.size() - 1, false) << endl;
    }
    return 0;
}
