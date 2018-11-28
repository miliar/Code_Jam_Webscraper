#include<bits/stdc++.h>
using namespace std;
int main()
{
freopen("B-large.in","r",stdin);
freopen("output.txt","w",stdout);
int t;
cin>>t;
for(int i=1;i<=t;i++)
{
    string s;
    cin>>s;
    long long c=1;
    if(s.length()>1){
    for(int i=0;i<s.length()-1;i++)
    {
     if(s.at(i)==s.at(i+1))
            continue;
     else
        c++;
    }
    }
    else
    {
        if(s.at(0)=='+')
            c--;
    }
    if(c!=0&&s.at(s.length()-1)=='+')
        c--;
    cout<<"Case #"<<i<<": "<<c<<"\n";
}
}
