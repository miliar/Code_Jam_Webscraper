#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

void flip(string &s, int l) {
  string aux(s);
  for(int i = 0; i < l; i++) {
    s[i] = aux[l-i-1] == '+' ? '-' : '+';
  }
}

int continuous(string & s, int l) {
  int i = 0;
  while(s[i] == '+') {
    i++;
  }
  int ans = i;
  while(s[i] == '-' && i < l) {
    i++;
  }
  if(i == l) {
    return ans;
  }
  else {
    return -1;
  }
}

int solve(string& s, int b, int l) {
  char a = s[0];
  int ans = 0;
  for(int i = 0; i < l; i++) {
    if(a != s[i]) {
      a = s[i];
      ans++;
    }
  }
  if(s[l-1] == '-') {
    ans++;
  }
  return ans;
}

//int solve(string &s, int l) {
//  int i = l-1;
//  if(l == 1) {
//    return s[i] == '+' ? 0 : 1;
//  }
//  // ends with +
//  if(s[i] == '+') {
//    return solve(s, l-1);
//  }
//  // ends with -
//  // starts with -
//  if(s[0] == '-') {
//    flip(s, l);
//    return 1 + solve(s , l);
//    //ends with - starts with +
//  } else {
//    int f = continuous(s, l);
//    if(f != -1) {
//      flip(s, f);
//
//    } else {
//      flip(s, 1);
//    }
//    return 1 + solve(s, l);
//  }
//}
int main() {
  //freopen("B-small-attempt1.in", "r" , stdin);
  freopen("B-large.in", "r" , stdin);
  //freopen("in", "r" , stdin);
  freopen("Blarge.out", "w" , stdout);
  int T;
  cin >> T;
  for(int t = 1; t <= T; t++) {
    string S;
    cin >> S;
    int l = S.size();

    int ans = solve(S, 0, l);

    cout << "Case #" << t << ": " << ans << "\n";
  }
}
