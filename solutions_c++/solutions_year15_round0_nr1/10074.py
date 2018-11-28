#include <iostream>
#include <cstdio>
#include <string>
using namespace std;

int main()
{
    int t,k;
    cin >> t;
    for (k = 1; k <= t; k++) {
        int sm, i;
        string s;
        cin >> sm;
        cin >> s;
        int cnt = s[0]-'0';
        int ans = 0;
        for (i = 1; i <= sm; i++) {
            if ((s[i]-'0') > 0) {
               if (cnt < i) {
                  ans += i-cnt;
                  cnt += i-cnt;
                  cnt += s[i]-'0';        
               } else {
                  cnt += s[i]-'0';       
               }        
            }    
        }        
        cout << "Case #" << k << ": " << ans << endl; 
    }
   // system("pause");
    return 0;
}
