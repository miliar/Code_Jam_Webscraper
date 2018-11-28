#include<bits/stdc++.h>
using namespace std;
#define ll long long

string s;
int main()
{
        freopen("inp.in","r",stdin);
    freopen("opt.out","w",stdout);

    ll t,p,i,len;
    char first;
    cin>>t;
    for(p = 1;p<=t;p++)
    {
        cin>>s;
        len = s.length();
        first = s[0];
        string st;
        st += s[0];
        for(i=1;i< len ; i++)
        {
            if(first > s[i])
            {
                st = st + s[i];
            }
            else
            {
                st = s[i]+st;
                first = s[i];
            }
        }
        cout<<"Case #"<<p<<": "<<st;
        cout<<endl;
    }
    return 0;
}
