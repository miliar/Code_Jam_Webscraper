#include<bits/stdc++.h>
using namespace std;
int main(){
    int t;
    cin>>t;
    for(int tt=1;tt<=t;tt++){
        cout<<"Case #"<<tt<<": ";
        string s;
        cin>>s;
        int n=s.size();
        int ans=0;
        for(int i=1;i<n;i++){
            if(s[i]=='-' and s[i-1]=='+'){
                ans++;
            }
        }
        ans*=2;
        if(s[0]=='-')
            ans++;
        cout<<ans<<endl;
    }
}
