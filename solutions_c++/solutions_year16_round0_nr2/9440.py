#include<bits/stdc++.h>
using namespace std;

#define l long long

ifstream fin("input.txt");
ofstream fout("output.txt");
int main(){
    int t;cin>>t;
    for(int j=1;j<=t;j++){
        string s;cin>>s;

        int ans=0,i=0;

        if(s[i]=='-')ans++;

        while(i<s.length()&&s[i]=='-')i++;
        for(;i<s.length();i++){
            if(s[i]=='-'){
                ans+=2;
                while(i<s.length()&&s[i]=='-')i++;
            }
        }
        cout<<"Case #"<<j<<": ";
        cout<<ans<<endl;

    }
}
