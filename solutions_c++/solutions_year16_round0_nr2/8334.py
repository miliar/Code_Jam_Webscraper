#include <bits/stdc++.h>

using namespace std;

int t,szaml;
string s;

int main()
{
    freopen("B-large.in","r",stdin);
    //freopen("B-large.txt","w",stdout);
    cin>>t;
    for(int i=1;i<=t;i++) {
        szaml=0;
        cin>>s;
        for(int j=1;j<s.size();j++){
            if(s[j]!=s[j-1]) szaml++;
        }
        if(s.back()=='-') szaml++;
        cout<<"Case #"<<i<<": "<<szaml<<endl;
    }
    return 0;
}
