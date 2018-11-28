#include <bits/stdc++.h>

using namespace std;

int main(){
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

  string s;
  int t,n;
  cin >> t;

  for(int i=0;i<t;i++){
    cin >> s;
    n = 1;
    for(int j=1;j<s.length();j++){
      if(s[j] != s[j-1])
        n++;
    }
    if(s[s.length() - 1] == '+')
      n--;
    cout << "Case #" << i+1 << ": " << n << '\n';
  }

  return 0;
}
