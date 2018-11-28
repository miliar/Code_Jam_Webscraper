#include <iostream>
#include <string.h>
using namespace std;

int main() {
    int tc, count = 1;
    cin>>tc;
    while (tc--) {
        string s;
        cin>>s;
        int n = s.length();
        string ans="";
        ans = s[0];
        for (int i=1;i<n;i++) {
            if (s[i] >= ans[0]) {
                ans = s[i]+ans;
            } else {
                ans = ans+s[i];
            }
            //cout<<ans<<endl;
        }
        cout<<"Case #"<<count++<<": "<<ans<<endl;
    }
    return 0;
}