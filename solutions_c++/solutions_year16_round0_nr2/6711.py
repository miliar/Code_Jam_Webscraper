#include <bits/stdc++.h>

using namespace std;

int main()
{
    freopen ("input.txt","r",stdin);
    freopen ("output.txt","w",stdout);
    int t;
    cin>>t;
    for(int i = 1;i <= t;i++){
        string s;
        cin>>s;
        int ans = 0;
        for(int j = s.size() - 1;j >= 0;j--){
            if(s[j] == '+'){
                if(ans%2 == 1){
                    ans++;
                }
            }else{
                if(ans%2 == 0){
                    ans++;
                }
            }
        }
        cout<<"Case #"<<i<<": "<<ans<<endl;
    }
    return 0;
}
