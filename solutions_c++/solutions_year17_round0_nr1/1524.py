#include <iostream>
#include <string>

using namespace std;

int main() {
    int T; cin>>T;
    for (int tt = 1; tt <= T; tt++) {
      string s;cin>>s;
      int K; cin>>K;
      int c = 0;
      for (int i = 0; i <= s.size() - K; i++) {
        if (s[i]=='-') {
          for (int j = 0; j < K; j++) {
            s[i+j] = (s[i+j] == '-') ? '+' : '-';
          }
          c++;
        }
      }
      bool rs = true; 
      for (int j = 1; j <= K; j++) {
        if (s[s.size()-j] == '-') {
          rs = false;
          break;
        }
      }
      if (rs) {
        cout << "Case #"<<tt<<": "<<c<<"\n";
      } else {
        cout << "Case #"<<tt<<": IMPOSSIBLE\n";
      }
    }
}
