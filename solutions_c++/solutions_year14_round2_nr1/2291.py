#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
using namespace std;
int t,k,n,i,l,j,ok,sol,L,maxi,mini;
char s[110],ch,CH;
vector<pair<int,char> >v[110];
int main()
{
    freopen("a.in","r",stdin);
    cin>>t;
    freopen("a.out","w",stdout);
    for(k=1;k<=t;k++)
    {
        cin>>n;
        cout<<"Case #"<<k<<": ";
        for(i=1;i<=n;i++)
        {
            cin>>s;
            v[i].clear();
            ch=s[0];
            l=1;
            for(j=1;j<=strlen(s);j++)
            {
                if(s[j]==ch)
                    l++;
                else
                {
                    v[i].push_back(make_pair(l,ch));
                    ch=s[j];
                    l=1;
                }
            }
        }
        ok=1;
        sol=0;
        for(i=0;i<v[1].size();i++)
        {
            CH=v[1][i].second;
            L=v[1][i].first;
            maxi=0;
            mini=110;
            for(j=1;j<=n;j++)
            {
                if(v[j][i].second!=CH||v[j].size()!=v[1].size())
                {
                    ok=0;
                    i=110;
                    cout<<"Fegla Won\n";
                    break;
                }
                maxi=max(maxi,v[j][i].first);
                mini=min(mini,v[j][i].first);
            }
            sol+=maxi-mini;
        }
        if(ok)
            cout<<sol<<'\n';
    }
    return 0;
}
