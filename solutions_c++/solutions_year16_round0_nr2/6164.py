#include<iostream>
#include<cstdio>
#include<string>
#include<vector>
using namespace std;
int t;
string s;
vector<int> realans;
int main()
{
    int sz,ans;
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cin>>t;
    for(int k=1;k<=t;++k)
    {
        cin>>s;
        sz=s.size();
        ans=0;
        for(int i=1;i<sz;++i)
        {
            if(s[i]!=s[0])
            {
                ++ans;
                for(int j=0;j<i;++j)
                {
                    if(s[j]=='-')s[j]='+';
                    else s[j]='-';
                }
            }
        }
        if(s[0]=='-')++ans;
        realans.push_back(ans);
    }
    for(int i=0;i<realans.size();++i)
    {
        cout<<"Case #"<<i+1<<": "<<realans[i]<<"\n";
    }
    return 0;
}
