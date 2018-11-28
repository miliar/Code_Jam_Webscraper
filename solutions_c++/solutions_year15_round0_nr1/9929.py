#include <bits/stdc++.h>

using namespace std;


int main() {
  int t,s;
  string x;
  int cnt=1;
  cin >> t;
  while(t--) {
    cin >> s >> x;
    int c = 0;
    int ans = 0;
    vector <int> V(s+1);
    for(int i = 0; i <= s; i++) {
      V[i]=(x[i]-'0');
    }
    for(int i = 0; i <= s; i++) {
      if(V[i]==0)continue;
      if(c < i) {
        int lol = i-c;
        //cout<< "lol -> " << lol << endl;
        for(int j = 0; j < i; j++) {
          if(V[j]+lol <= s) {
            ans+=lol;
            V[j]+=lol;
            lol = 0;
          }else {
            lol-=(s-V[j]);
            ans+=(s-V[j]);
            V[j]=s;
          }
          c+=V[j];
          if(lol == 0)break;
        }
      }
      c+=V[i];
    }
    cout << "Case #"<< cnt++ << ": " << ans <<"\n";
  }
  return 0;
}
