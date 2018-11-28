#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("test.out","w",stdout);
    string s;
    int t,d=0;
    cin>>t;
    for(int j=1;j<=t;j++)
    {
        cin>>s;
        while(count(s.begin(),s.end(),'+')!=s.length())
        {
            int n=s.find('-');
            int k=s.find('+',n);
            if(k<0)
            {
                for(int i=0;i<s.length();i++)
            {
                if(s[i]=='+')
                s[i]='-';
                else
                s[i]='+';
            }
            d++;
            }
            if(count(s.begin(),s.end(),'+')!=s.length())
            {
             n=s.find('-');
             k=s.find('+',n);
            for(int i=0;i<k;i++)
            {
                if(s[i]=='+')
                s[i]='-';
                else
                s[i]='+';
            }
             d++;
            }
        }
        cout<<"Case #"<<j<<": "<<d<<"\n";
        d=0;
    }
    return 0;
}
