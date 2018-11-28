#include <bits/stdc++.h>
using namespace std;

int t, n, d[10];
string s;

int main(){
  cin >> t;
  int cnt=0;
  while (t--){
    cnt++;
    cin >> s;
    bool rev = 0;
    int ans=0;
    for (int i=s.size()-1; i>=0; i--){
      char c = s[i];
      if ((c=='+' && rev==1) || (c=='-' && rev==0)) ans++, rev^=1;

    }
    cout << "Case #" << cnt << ": " << ans << endl;
  }


}
