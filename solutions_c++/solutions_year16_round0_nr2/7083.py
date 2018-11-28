#include<bits/stdc++.h>
using namespace std;
int main(){
    int t, p=1;
    cin>>t;
    while(t--){
        string s;
        cin>>s;
        s=s+'+';
        char state=s[0];
        int l=s.size();
        long long int ans=0;
        for(int i=1; i<l; i++){
            if(s[i]!=state){
                ans++;
                state=s[i];
            }
        }
        cout<<"Case #"<<p<<": "<<ans<<"\n";
        p++;
    }
}

