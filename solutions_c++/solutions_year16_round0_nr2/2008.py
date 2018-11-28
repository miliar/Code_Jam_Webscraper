#include<bits/stdc++.h>
using namespace std;
#define IO ios_base::sync_with_stdio(false);cin.tie(NULL);

#define endl '\n'
#define D(x) cout << #x << " = " << (x) << endl;

int f(const string &s, char c){
  int cnt = 0;
  for(int i = 0; i < s.size(); ++i){
    if(s[i] == c and (i == 0 or s[i - 1] != c)){
      if(i == 0) cnt += 1;
      else cnt += 2;
    }
  }
  return cnt;
}

int main(){ IO;
  int t;
  cin >> t;

  for(int ncase = 1; ncase <= t; ++ncase){
    cout << "Case #" << ncase << ": ";

    string s;
    cin >> s;

    int a = f(s, '-');
    int b = 1 + f(s, '+');

    cout << min(a, b) << endl;
  }

  return 0;
}
