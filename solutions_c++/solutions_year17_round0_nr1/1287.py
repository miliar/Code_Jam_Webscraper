#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("alarge.in","r",stdin);
    freopen("alarge.out","w",stdout);
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    int tt,k;
    cin>>tt;
    string s;
    for(int t=1; t<=tt; t++)
    {
        cin>>s;
        cin>>k;
        int c=0;
        int n=s.length()-k;
        for(int i=0; i<=n; i++)
        {
            if(s[i]=='-')
            {
                c++;
                for(int j=i; j<i+k; j++)
                {
                    if(s[j]=='-')
                        s[j]='+';
                    else
                        s[j]='-';
                }
            }
        }
        bool poss=true;
        for(int i=n; i<s.length(); i++)
        {
            if(s[i]=='-')
            {
                poss=false;
                break;
            }
        }
        if(poss)
            cout<<"Case #"<<t<<": "<<c<<endl;
        else
            cout<<"Case #"<<t<<": IMPOSSIBLE"<<endl;
        cerr<<"Test Case "<<t<<" Solved"<<endl;
    }
    return 0;
}
