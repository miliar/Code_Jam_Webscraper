#include <iostream>

using namespace std;
int main() {
    int tc, count=1;
    cin>>tc;
    while (tc--) {
        string s;
        int ans=0;
        cin>>s;
        cout<<"Case #"<<count++<<": ";
        for (int i=s.length()-1;i>=0;i--) {
            if (s[i] == '-') {
                if (s[0] == '+') {
                    for (int j=0;j<=i;j++) {
                        if (s[j] == '-') break;
                        else s[j] = '-';
                    }
                    ans++;
                }
                string temp = s;
                for (int j=0;j<=i;j++) {
                    s[j] = temp[i-j] == '+' ? '-' : '+';
                }
                ans++;
            }
        }
        
        cout<<ans<<endl;
    }
    return 0;
}