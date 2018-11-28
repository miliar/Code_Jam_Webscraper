#include<bits/stdc++.h>

using namespace std;

int main(){

    freopen("B-large.in","r",stdin);
    freopen("out2_large.txt","w",stdout);
    int t;
    cin>>t;
    for(int i=0;i<t;i++){
        string s;
        cin>>s;
        cout<<"Case #"<<(i+1)<<": ";
        int cnt=0;
        for(int i=1;i<s.size();i++){
            if(s[i]!=s[i-1]) cnt++;
        }
        if(s[s.size()-1]=='-') cnt++;
        if(s[0]=='+' && cnt==0) cnt=0;
        cout<<cnt<<endl;
    }

}

