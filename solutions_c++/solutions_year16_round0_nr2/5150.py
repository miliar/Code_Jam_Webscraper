#include <bits/stdc++.h>

using namespace std;

int main(){
    int t;
    cin >> t;
    int index=1;
    while(t--){
        string s;
        cin >> s;
        int ans=0;
        if(s.size()==1){
            if(s[0]=='-'){
                ans=1;
            }
            cout << "Case #" << index++ << ": " << ans << endl;
            continue;
        }
        int flag=0;
        for(int i=1;i<s.size();++i){
            if(s[i-1]=='+' && s[i]=='-'){
                ans+=2;
                flag=1;
            }
            if(s[i-1]=='-' && s[i]=='+'){
                if(flag==0){
                    ++ans;
                }
                flag=1;
            }

        }
        if(flag==0 && s[0]=='-')
        ++ans;

       cout << "Case #" << index++ << ": " << ans << endl;

    }
    return 0;
}
