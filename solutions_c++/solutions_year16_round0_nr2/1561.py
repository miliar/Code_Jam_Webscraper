#include <bits/stdc++.h>
using namespace std;
int main()
{
    int t;
    cin>>t;
    for(int test = 1; test <= t; test++){
        int ans = 0;
        string s;
        cin>>s;
        while(1){
            int np = 0, posm = s.size();
            for(int i = 0; i < s.size(); i++){
                if(s[i] == '-')
                    break;
                np++;
            }
            for(int i = s.size() - 1; i >= 0; i--){
                if(s[i] == '-'){
                    posm = i;
                    break;
                }
            }
            // cout<<np<<" "<<posm<<endl;
            if(np == s.size())
                break;
            if(np != 0){
                for(int i = 0; i < np; i++)
                    s[i] = '-';
            }
            else{
                for(int i = 0; i <= posm/2; i++){
                    char temp = s[posm-i];
                    if(s[i] == '+')
                        s[posm-i] = '-';
                    else
                        s[posm-i] = '+';
                    if(temp == '+')
                        s[i] = '-';
                    else
                        s[i] = '+';
                }
            }
            // cout<<s<<endl;
            ans++;
        }
        cout<<"Case #"<<test<<": "<<ans<<endl;
    }
}