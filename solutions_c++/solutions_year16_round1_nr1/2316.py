#include<bits/stdc++.h>

using namespace std;

#define ll long long int

int main()
{
    string s;
    ll t;
    cin>>t;
    char st[5000];
    ll first=1000,i;
    ll last=1000;
    for(i=0;i<5000;i++)
        st[i]='0';
    while(t--)
    {
        cin>>s;
        for(i=0;i<s.size();i++)
        {
            if(i==0)
                st[first]=s[i];
            else
            {
                if(s[i]>=st[first])
                {
                    st[--first]=s[i];
                }
                else
                {
                    st[++last]=s[i];
                }
            }

        cout<<"Case #"<<count<<": ";
        for(i=0;i<5000;i++)
        {
            if(st[i]!='0')
            {
                cout<<st[i];
                st[i]='0';
            }
        }
        cout<<"\n";
    }
    return 0;
}
