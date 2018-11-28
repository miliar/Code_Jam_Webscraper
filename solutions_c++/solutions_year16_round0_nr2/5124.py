#include<bits/stdc++.h>

using namespace std;

#define ll long long int

int main()
{
    string s;
    ll count=0,c=0,t,i,j;
    cin>>t;
    while(t--)
    {
        count=0;
        c++;
        cin>>s;
        for(i=1;i<s.size();i++)
        {
            if(s[i]!=s[i-1])
            {
                for(j=0;j<i;j++)
                {
                    if(s[i]=='-')
                        s[j]='+';
                    else
                        s[j]='-';
                }
                count++;
            }
        }
        if(s[i-1]=='-')
            count++;
        cout<<"Case #"<<c<<": "<<count<<"\n";
    }
    return 0;
}
