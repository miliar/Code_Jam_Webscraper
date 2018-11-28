#include <bits/stdc++.h>
using namespace std;

int N;

int main() {
    int TC = 1;
    cin>>TC;
    for(int tc=1;tc<=TC;tc++) {
        string s;
        cin>>s;
        int ans = 0;
        for(int i=s.size()-1;i>=0;i--) if (s[i] == '-') {
            int j=0;
            if (s[j] == '+') {
                ans++;
                while(j<i && s[j] == '+') s[j++] = '-';
            }
            for(int j=0;j<(i+1)/2;j++) {
                char tmp = s[j];
                s[j] = s[i-j];
                s[i-j] = tmp;
            }
            for(int j=0;j<=i;j++) s[j] = (s[j] == '+'? '-' : '+');
            ans++;
        }
        cout<<"Case #"<<tc<<": "<<ans<<endl;
    }
    return 0;
}
