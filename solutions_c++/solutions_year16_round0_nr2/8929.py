#include <bits/stdc++.h>

using namespace std;

string flip(string s) {
  std::reverse(s.begin(), s.end());
  for(char &c : s) {
    c = c == '+' ? '-' : '+';
  }
  return s;
}

int solve(string s) {
    if(s.find('-') == string::npos) return 0;
    if(s.find('+') == string::npos) return 1;
    for(int i = s.length() - 1; i >= 0; --i) {
      if(s[i] != '+'){
        if(i == s.length() - 1) break;
        return solve(s.substr(0, i + 1));
      }
    }
    if(s[0] == '-') {
      return 1 +  solve(flip(s));
    }

    int i = 0;
    while(s[i] == '+') {
      s[i++] = '-';
    }
    return 1 + solve(s);
}

void instance(int T) {
    string s; cin >> s;
    int n = solve(s);
    cout << "Case #" << T << ": " << n << endl;
}

int main()  {
    int T;
    cin >> T;
    for(int t = 0; t < T; t++) {
        instance(t + 1);
    }
}
