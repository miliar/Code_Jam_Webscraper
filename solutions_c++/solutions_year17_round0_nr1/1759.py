#include <bits/stdc++.h>

using namespace std;

const int maxn = 1010;

string s;
int n,k;

int main(){
  ios::sync_with_stdio(false);
  int t; cin >> t;
  for(int cass = 1; cass <= t; ++cass){
    cin >> s >> k;
    n = s.size();
    int cont = 0;
    for(int i = 0; i < n; ++i){
      if(s[i] == '-'){
        if(i+k > n){
          cont = -1;
          break;
        }
        for(int j = i; j < i+k; ++j){
          if(s[j] == '+') s[j] = '-';
          else s[j] = '+';
        }
        ++cont;
      }
    }
    if(cont == -1) cout << "Case #" << cass << ": IMPOSSIBLE\n";
    else cout << "Case #" << cass << ": " << cont << '\n';
  }
}