#include<bits/stdc++.h>

using namespace std;

int main()
{
    freopen("000.in","r",stdin);
    freopen("0002.txt","w",stdout);

    int t,k,i,l,j;
    string s;
    cin>>t;

    for(l=1;l<=t;l++)
    {
        cin>>s>>k;
        int c=0;

        for(i=0;i<s.length();i++)
        {
            if(s[i]=='+')
                continue;

            if(i+k>s.length())
                break;

            for(j=0;j<k;j++)
                s[i+j]=(s[i+j]=='+'?'-':'+');
            c++;
            //cout<<s<<endl;
        }

        int flag=0;
        for(i=0;i<s.length();i++)
        {
            if(s[i]=='-')
                flag=1;
        }

        if(flag==1)
            cout<<"Case #"<<l<<": "<<"IMPOSSIBLE"<<endl;
        else
            cout<<"Case #"<<l<<": "<<c<<endl;
    }

    return 0;
}
