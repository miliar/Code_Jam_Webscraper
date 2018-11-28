#include<bits/stdc++.h>
using namespace std;


string s[3]={"R","P","S"};
string dfs(int f,int d)
{
    if(d==0)return s[f];
    string z1,z2;
    if(f==0)
    {
        z1=dfs(0,d-1);
        z2=dfs(2,d-1);
    }
    else if(f==1)
    {
        z1=dfs(0,d-1);
        z2=dfs(1,d-1);
    }
    else
    {
        z1=dfs(1,d-1);
        z2=dfs(2,d-1);
    }
    if(z1>z2)return z2+z1;
    else return z1+z2;
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("2.txt","w",stdout);
    int t,ti=1;cin>>t;
    while(t--)
    {
        int n,r,p,s,f=0;
        cin>>n>>r>>p>>s;
        cout<<"Case #"<<ti++<<": ";
        for(int i=0;i<3;i++)
        {
            string a=dfs(i,n);
            int R=0,P=0,S=0;
            for(int j=0;j<a.length();j++)
                if(a[j]=='R')R++;
                else if(a[j]=='P')P++;
                else S++;
            if(R==r&&P==p&&S==s)
            {
                cout<<a<<endl;
                f=1;
                break;
            }
        }
        if(f==0)
            cout<<"IMPOSSIBLE"<<endl;
    }
    return 0;
}
