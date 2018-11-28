#include<iostream>
#include<string>
#include<cstdio>
#include<cstring>
using namespace std;
string n;
int t,r,ans;
int main()
{
    freopen("B.in","r",stdin);
    freopen("B.out","w",stdout);
    cin>>t;
    for(int o=1;o<=t;o++)
    {
        cin>>n;
        r=ans=0;
        while(n[r]=='-')
        {
            ans=1;
            n[r++]='+';
        }
        while(r<n.length())
        {
            if(n[r]=='-'&&n[r-1]=='+')
                ans+=2;
            r++;
        }
        cout<<"Case #"<<o<<": "<<ans<<endl;
    }
    return 0;
}
