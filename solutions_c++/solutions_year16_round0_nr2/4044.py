#include <bits/stdc++.h>
using namespace std;
int main(){
    long long n,i,cas,j,sum;
    string s;
    cin>>cas;
    for (j=0;j<cas;j++){
        cin>>s;
        sum=0;
        for (i=1;i<s.length();i++){
            if(s[i]!=s[i-1])sum++;
        }
        if(s[s.length()-1]=='-')sum++;
        cout<<"Case #"<<j+1<<": ";
        cout<<sum<<endl;
    }
}
