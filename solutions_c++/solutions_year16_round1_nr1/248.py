#include <iostream>
#define REP(i,n) for(int i=0; i<(int)(n); i++)

#include <cstdio>
inline int getInt(){ int s; scanf("%d", &s); return s; }

#include <set>

using namespace std;

int main(){
  const int T = getInt();
  REP(i,T) {
    string s; cin >> s;

    string ans;
    ans += s[0];
    for(int i = 1; i < (int)s.size(); i++){
      if(ans[0] <= s[i]) ans = s[i] + ans;
      else ans = ans + s[i];
    }
    cout << "Case #" << i + 1 << ": " << ans << endl;
  }
  return 0;
}
