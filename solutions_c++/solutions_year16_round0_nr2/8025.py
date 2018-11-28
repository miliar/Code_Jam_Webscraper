#include <bits/stdc++.h>
#define ll long long int

using namespace std;

int main()
{
   freopen( "input.txt", "r", stdin );
   freopen( "output.txt", "w", stdout );
    ll t,j=1;
    cin>>t;
    while(t--)
    {
        int flag=0;
        string s,s1;
        cin>>s;
        s1=s1+s[0];
        for(int i=1;i<s.length();i++)
        {
            if(s[i]!=s[i-1])
                s1+=s[i],flag=1;
        }
        if(flag==0)
        {
            if(s[s.length()-1]=='+')
                cout<<"Case #"<<j++<<": "<<0<<endl;
            else
                cout<<"Case #"<<j++<<": "<<1<<endl;
            continue;
        }
        int p=0,n=0;
        for(int i=0;i<s1.length();i++)
        {
            if(s1[i]=='-')
                n++;
            else
                p++;
        }
        if(p==n)
        {
            if(s1[s1.length()-1]=='-')
                cout<<"Case #"<<j++<<": "<<p+n<<endl;
            else
                cout<<"Case #"<<j++<<": "<<p+n-1<<endl;
        }
        else if(p>n)
            cout<<"Case #"<<j++<<": "<<p+n-1<<endl;
        else
            cout<<"Case #"<<j++<<": "<<p+n<<endl;
    }
    return 0;
}
