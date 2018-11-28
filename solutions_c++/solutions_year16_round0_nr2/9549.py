#include<bits/stdc++.h>
using namespace std;
int main(){
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    cin>>t;
    for(int T=1;T<=t;T++){
        string s;
        cin>>s;
        int i,ans=0;
        for(i=0;i<s.size()-1;i++){
            if(s[i]!=s[i+1])
                ans++;
        }
        if(s[s.size()-1]=='-')
            ans++;
        cout<<"Case #"<<T<<": "<<ans<<"\n";
    }
}
