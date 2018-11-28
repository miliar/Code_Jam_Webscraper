#include <bits/stdc++.h>

using namespace std;

string solve(string s){
    string ans = "";
    for(int i = 0; i < s.size(); i++)
        ans = (s[i] < ans[0] ? ans + s[i] : s[i] + ans);
    return ans;
}

int main( ) {

  #ifdef LOCAL
    freopen( "A-large.in", "r", stdin );
    freopen( "A-large.out", "w", stdout );
  #endif

  ios_base::sync_with_stdio( 0 );
  cin.tie( 0 );

  int T;
  cin>>T;
  for(int t = 1; t<=T; t++){
    string s;
    cin>>s;
    cout<<"Case #"<<t<<": "<<solve(s)<<"\n";
  }
  return 0;
}
