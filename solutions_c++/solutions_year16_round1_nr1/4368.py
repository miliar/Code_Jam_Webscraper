#include <bits/stdc++.h>

using namespace std;

int main()
{
    freopen("A-large (1).in","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    cin>>t;
    for(int i=1;i<=t;i++)
    {
        string s,k,temp;
        cin>>s;
        k=k+s[0];
        for(int i=1;i<s.length();i++)
        {
            if(k[0]<=s[i])
            {
                temp=s[i];
                temp+=k;
                k=temp;
            }
            else
                k=k+s[i];
        }
        cout<<"Case #"<<i<<": "<<k<<endl;
    }
    return 0;
}
