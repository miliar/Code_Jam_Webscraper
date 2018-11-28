#include <bits/stdc++.h>
using namespace std;
int main()
{
    freopen("BL.in","r",stdin);
    freopen("output.in","w",stdout);
    int t,j,ctr=0,l,z=1,k; cin>>t; string s;
    for(int i=1;i<=t;i++)
    {
        cin >> s;
        reverse(s.begin(),s.end());
        for(k=0;k<s.length();k++)
        {
            if(s[k]=='-')
            {   ctr++;
                for(int j=k;j<s.length();j++)
                {
                    if(s[j]=='+') s[j]='-';
                    else s[j]='+';
                }
                }
            }
        cout<<"Case #"<<i<<": "<<ctr<<"\n";
        ctr=0;
    }
    return 0;
}
