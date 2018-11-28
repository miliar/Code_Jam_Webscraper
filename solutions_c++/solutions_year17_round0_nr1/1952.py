#include <iostream>
using namespace std;

int main()
{
    int tc;cin>>tc;
    int t;
    for(t=1;t<=tc;t++)
    {
    string s;int k;
    cin>>s>>k;

    int j;

    int count=0;
    int p=0;
    while(p!=s.length()-k+1)
    {
        if(s[p]=='-')
        {
            for(int i=p;i<p+k;i++)
            {
                if(s[i]=='-')
                {
                    s[i]='+';
                }
                else{
                    s[i]='-';
                }
            }
            count++;
            p++;
        }
        else{
            p++;
        }
    }
    for(j=s.length()-k;j<s.length();j++)
    {
        if(s[j]=='-')
        {
            break;
        }
    }
    if(j==s.length())
    {
        cout<<"Case #"<<t<<": "<<count<<endl;
    }
    else{
        cout<<"Case #"<<t<<": "<<"IMPOSSIBLE"<<endl;
    }
}
    return 0;
}
