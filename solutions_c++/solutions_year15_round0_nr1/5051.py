#include<bits/stdc++.h>
using namespace std;

int T;

int main(){
  cin >> T;
  for(int ttt=0;ttt<T;ttt++){
    int S;
    cin >> S;
    string s;
    cin >> s;
    int cnt = 0;
    int res = 0;
    for(int i=0;i<S+1;i++){
      if( i > cnt ) {
	res += i - cnt;
	cnt = i;
      }
      cnt += (s[i]-'0');	
    }
    cout << "Case #" << ttt+1 << ": " << res << endl;
  }
}
