#include <bits/stdc++.h>

using namespace std;
bool ok(string s)
{
    //cout<<s<<endl;
    if(s.length()==1)return true;
    string ret="";
    for(int i=1; i<s.length(); i+=2)
    {
        if(s[i]==s[i-1])return false;
        bool p=false,r=false,ss=false;
        if(s[i]=='P')p=true;
        if(s[i]=='R')r=true;
        if(s[i]=='S')ss=true;
        if(s[i-1]=='P')p=true;
        if(s[i-1]=='R')r=true;
        if(s[i-1]=='S')ss=true;
        if(p&&r)ret+="P";
        if(p&&ss)ret+="S";
        if(r&&ss)ret+="R";
    }
    return ok(ret);
}
int main()
{
    int t;
    freopen("input.in","r",stdin);
    freopen("out.out","w",stdout);
    scanf("%d",&t);
    int caseno=1;
    while(t--)
    {
        int n,p,r,s;
        scanf("%d%d%d%d",&n,&r,&p,&s);
        string c="";
        for(int i=0; i<p; i++)c+="P";
        for(int i=0; i<r; i++)c+="R";
        for(int i=0; i<s; i++)c+="S";
        sort(c.begin(),c.end());
        bool found=false;
        do
        {
            if(ok(c))
            {
                found=true;
                cout<<"Case #"<<caseno++<<": "<<c<<endl;
                break;
            }
        }
        while(next_permutation(c.begin(),c.end()));
        if(!found)
        {
            cout<<"Case #"<<caseno++<<": IMPOSSIBLE"<<endl;
        }
    }
    return 0;
}
