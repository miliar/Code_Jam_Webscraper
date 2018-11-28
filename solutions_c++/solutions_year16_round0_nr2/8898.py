#include <bits/stdc++.h>
using namespace std;
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("outp.txt","w",stdout);
    string s;int j,t,ans,i,l,p,f;
    cin>>t;
    for(j=1;j<=t;j++)
    {
        ans=0;
        cin>>s;
        l=s.length();
        if(s.at(0)=='-')
        {
            p=s.find_last_of('-');
            //cout<<p;
            reverse(s.begin(),s.begin()+p+1);
            //cout<<s;
            for(i=0;i<=p;i++)
            {
                if(s.at(i)=='+')
                    s.at(i)='-';
                else
                    s.at(i)='+';
            }
            //cout<<s;
            ans++;
        }
        p=s.find_first_of('-');
        //cout<<p;
        f=1;
        while(p<l && p>=0)
        {
            if(f)
            {
                reverse(s.begin(),s.begin()+p);
                for(i=0;i<p;i++)
                {
                    if(s.at(i)=='+')
                        s.at(i)='-';
                    else
                        s.at(i)='+';
                }
                p=s.find_last_of('-');
            }
            else
            {
                reverse(s.begin(),s.begin()+p+1);
                for(i=0;i<=p;i++)
                {
                    if(s.at(i)=='+')
                        s.at(i)='-';
                    else
                        s.at(i)='+';
                }
                p=s.find_first_of('-');
            }
            f=1-f;
            ans++;
        }
        cout<<"Case #"<<j<<": "<<ans<<endl;
    }
    return 0;
}
