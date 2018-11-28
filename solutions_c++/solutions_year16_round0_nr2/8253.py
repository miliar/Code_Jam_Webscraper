#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("B-large.in","r+",stdin);
    freopen("B-large.out","w+",stdout);
    int t,T;
    cin>>t;
    T=t;
    while(t--)
    {
        int  c=0;
        string s;
        cin>>s;
        char a;
        a='+';
        for(int i=s.length()-1;i>=0;i--)
        {
            if(s[i]!=a)
            {
                c++;
                if(a=='+')
                {
                    a='-';
                }
                else
                {
                    a='+';
                }
            }
        }
        cout<<"Case #"<<(T-t)<<": "<<c<<"\n";
    }
    return 0;
}
