#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("B-large (2).in","r",stdin);
    freopen("opb.txt","w",stdout);
    int t,z;
    cin>>t;
    for(z=1;z<=t;z++)
    {
        string s;
        cin>>s;
        int oper=0,i;
        for(i=1;s[i];i++)
        {
            if(s[i]!=s[i-1])
                oper++;
        }
        if(s[s.length()-1]=='-')
            oper++;
        cout<<"Case #"<<z<<": "<<oper<<endl;
    }
    return 0;
}
