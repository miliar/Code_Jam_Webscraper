#include <bits/stdc++.h>
using namespace std;

int main(){

    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);

    int t, s;
    string ns;
    cin>>t;

    for(int tc=1; tc<=t; tc++){
        cin>>s>>ns;
        int sm=0, ans=0;
        for(int i=0; i<=s; i++){
            if(sm<i) ans+=i-sm, sm+=i-sm;
            sm+=ns[i]-'0';
        }
        cout<<"Case #"<<tc<<": "<<ans<<endl;
    }

    return 0;
}
