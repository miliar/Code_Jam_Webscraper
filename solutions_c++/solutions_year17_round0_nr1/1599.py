#include <bits/stdc++.h>

using namespace std;

string s;

bool flip(int i,int k)
{
    if(i+k>s.size())
        return 0;
    for(int f=i;f<i+k;f++)
    {
        if(s[f]=='-')
            s[f]='+';
        else
            s[f]='-';
    }
    return 1;
}

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    cin>>t;
    for(int tc=1;tc<=t;tc++)
    {
        cin>>s;
        int k;
        cin>>k;
        bool flag=1;
        int ans=0;
        for(int f=0;f<s.size();f++)
        {
            if(s[f]=='-')
            {
                ans++;
                if(!flip(f,k))
                    flag=0;
            }
        }
        cout<<"Case #"<<tc<<": ";
        if(flag)
            cout<<ans<<endl;
        else cout<<"IMPOSSIBLE\n";
    }
}
