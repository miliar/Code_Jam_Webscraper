#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <set>

using namespace std;

int main()
{
    int T;
    cin >> T;
    for(int t = 1; t <= T; t++) {
        string s;
        cin >> s;
        long ans = 0;
        while(1) {
          bool flag = false;
          for(int i = s.length()-1; i >= 0; i--) {
              if(s[i] == '-') {
                  flag = true;
                  for(int j = i; j >= 0; j--) {
                      s[j] = (s[j] == '+') ? '-' : '+';
                  }
                  break;
              }
          }
          if(!flag) break;
          ans++;
        }
        cout << "Case #" << t << ": " << ans << "\n";
    }
    return 0;
}
