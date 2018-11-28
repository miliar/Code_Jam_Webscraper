#include<bits/stdc++.h>
using namespace std;

int main(){
    freopen("input.in", "r", stdin);
    freopen("output.out", "w", stdout);
    int tt;
    cin>>tt;
    for(int qq=1;qq<=tt;qq++){
        string s;
        cin>>s;
        cout<<"Case #"<<qq<<": ";
        int count=0;
        for(int i=0;i<s.length()-1;i++){
            if(s[i]!=s[i+1]) count++;
        }
        if(s[s.length()-1]=='-') count++;
        cout<<count<<endl;
    }
    return 0;
}
