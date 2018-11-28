#include<bits/stdc++.h>
using namespace std;

int state[110];

void solve(string s){
  //cout << endl;
  int res = 0;
  for(int i = (int)s.size() - 1;
      i >= 0;--i){
    //cout << s << endl;
    if(s[i] == '-'){
      ++res;
      for(int j = 0;j <= i;++j){
	if(s[j] == '+')s[j] = '-';
	else s[j] = '+';
      }
    }
  }
  //cout << s << endl;
  cout << res << endl;
  return;
}

int main(void){
  int n;
  cin >> n;
  for(int i = 0;i < n;++i){
    string s;
    cin >> s;
    cout << "Case #" << i+1 << ": ";
    solve(s);
  }
  return 0;
}
