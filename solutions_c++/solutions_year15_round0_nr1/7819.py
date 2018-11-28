#include <bits/stdc++.h>
using namespace std;
string s;
int a[1012],b[1012],q;
int main()
{
    cin>>q;
    for(int j=1;j<=q;j++)
    {
        int n,clp=0,sol=0;
        cin>>n;
        cin>>s;
        for(int i=0;i<=n;i++)
        if(s[i]!='0')
        {
            if(clp>=i)clp+=(s[i]-'0');
            else{
                sol+=(i-clp);
                clp+=(i-clp);
                clp+=(s[i]-'0');
            }
        }
        cout<<"Case #"<<j<<": "<<sol<<'\n';
    }
    return 0;
}
