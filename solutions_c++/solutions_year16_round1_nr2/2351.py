#include <bits/stdc++.h>

using namespace std;
typedef long long ll;

vector<int>v;
map<int,int>mp;
int main()
{
    freopen("B-small-attempt0.in","r",stdin);
    freopen("B-small-attempt0.out","w",stdout);

    int t,n,x;
    cin>>t;
    int i=1;
    vector<int>tmp;

    while(i<=t)    {
        cin>>n;
        for(int j=1;j<2*n;j++)    {
            for(int k=0;k<n;k++)    {
                cin>>x;
                if(!mp[x])    {
                    v.push_back(x);
                }
                mp[x]++;
            }
        }
        for(int j=0;j<v.size();j++)    {
            if(mp[v[j]]%2)    tmp.push_back(v[j]);
        }
        sort(tmp.begin(),tmp.end());
        cout<<"Case #"<<i++<<": ";
        for(int j=0;j<n;j++)    {
            cout<<tmp[j]<<" ";
        }
        cout<<endl;
        tmp.clear();
        v.clear();
        mp.clear();
    }
    return 0;

}
