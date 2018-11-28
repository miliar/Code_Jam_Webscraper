#include <bits/stdc++.h>
using namespace std;

int main() {
    int tc, aa, bb;
    string s1,s2;
    cin>>tc;
    int cnt = 1;
    while(tc--) {
        cin>>s1;
        if(s1.size() == 1) {
            if(s1[0] == '+')
                cout<<"Case #"<<cnt++<<": 0\n";
            else {
                cout<<"Case #"<<cnt++<<": 1\n";
            }
                continue;
        }
        else {
            reverse(s1.begin(), s1.end());
            int aa = 0, flag1 = 0, flag2 = 0;
            int ans = 0;
            for(int i = 1; i < s1.size(); i++) {
                if(s1[i] == s1[i-1])
                    continue;
                else if(s1[i] == '-' and s1[i-1] == '+') {
                    flag2 = 1;
                    ans++;
                }
                else if(s1[i] == '+' and s1[i-1] == '-') {
                    ans++;
                    if(flag1 == 0 and flag2 == 0) {
                        ans += 1;
                        flag1 = 1;
                    }
                }
            }
            if(flag1 != 0 or flag2 != 0) {
                cout<<"Case #"<<cnt++<<": "<<ans<<"\n";
            }
        }
    int allone = 0, allzero = 0;
    for(int i = 0; i < s1.size(); i++) {
        if(s1[i] == '+') {
            allone++;
        }
        else if(s1[i] == '-') {
            allzero++;
        }
    }
    if(allzero == 0)
        cout<<"Case #"<<cnt++<<": 0\n";
    if(allone == 0)
        cout<<"Case #"<<cnt++<<": 1\n";
}
return 0;
}
