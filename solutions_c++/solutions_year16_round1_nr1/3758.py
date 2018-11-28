#include <bits/stdc++.h>
using namespace std;
int main()
{
    int t;cin>>t;
    for(int z=1;z<=t;++z)
    {
        string s,y="";cin>>s;
        int i,j,n=s.length();y=s[0];
        for(i=1;i<n;++i)
        {
            if(s[i]>=y[0])y=s[i]+y;
            else y=y+s[i];
        }
        cout<<"Case #"<<z<<": "<<y<<"\n";
    }
    return 0;
}
