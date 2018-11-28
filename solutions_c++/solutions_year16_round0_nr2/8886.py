#include <bits/stdc++.h>
using namespace std;

int main() {
int t,n,c;
cin>>t;
string s;
for(int k =1;k<=t;k++)
{
    c=1;
    cin>>s;
    n=s.size();
    cout<<"Case #"<<k<<": ";
    for(int i=1;i<n;i++)
        if(s[i]!=s[i-1]) c++;
    if(s[n-1]=='+') c--;
    cout<<c<<endl;
}
return 0;
}