#include<bits/stdc++.h>
using namespace std;

int main()
{
    int tt,t,n,i,st,c,nop,r;
    string s;
    cin>>t;
    for(tt=1;tt<=t;tt++)
    {
        st=0;
        c=0;
        cin>>n;
        cin>>s;
        for(i=0;i<=s.length();i++)
        {
            nop=s[i]-48;
            if(i<=st)
            {
                st+=nop;
            }
            else
            {
                r=(i-st);
                c+=r;
                st+=(r+nop);
            }
        }
        cout<<"Case #"<<tt<<": "<<c<<"\n";
    }
    return 0;
}
