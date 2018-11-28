#include<bits/stdc++.h>
using namespace std;
int t,i,Z;
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    cin>>t;
    while(t--)
    {
        string s,p;
        cin>>s;
        for(i=0;s[i];i++)
        {
            if(i==0)
                p+=s[i];
            else if(s[i]>=p[0])
                p=s[i]+p;
            else
                p+=s[i];
        }
        cout<<"Case #"<<++Z<<": "<<p<<endl;
    }
}
