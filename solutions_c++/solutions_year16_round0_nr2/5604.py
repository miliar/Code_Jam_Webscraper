#include <bits/stdc++.h>
using namespace std;

int main()
{
//freopen("cj2.in","r",stdin);
//freopen("out2.txt","w",stdout);
int t;
cin>>t;
for(int co=1;co<=t;co++)
{
    string s;
    cin>>s;
    int l=s.length(),cnt=0;
    for(int i=1;i<l;i++)
    {
        if(s[i]!=s[i-1])
            cnt++;
    }
    if(s[l-1]=='-')
        cout<<"Case #"<<co<<": "<<cnt+1<<endl;
    else
        cout<<"Case #"<<co<<": "<<cnt<<endl;

}
return 0;
}
