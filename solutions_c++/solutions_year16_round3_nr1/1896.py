#include<bits/stdc++.h>
using namespace std;
vector<pair<int,char> > v;
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    scanf("%d",&t);
    for(int test=1;test<=t;test++)
    {
        v.clear();
        int n,x;
        scanf("%d",&n);
        for(int i=0;i<n;i++)
        {
            scanf("%d",&x);
            v.push_back(make_pair(x,'A'+i));
        }
        sort(v.begin(),v.end());
        cout<<"Case #"<<test<<": ";
        while(v[n-2].first!=v[n-1].first)
        {
            if(v[n-1].first==v[n-2].first+1)
            {
                v[n-1].first--;
                cout<<v[n-1].second<<" ";
            }
            else
            {
                v[n-1].first-=2;
                cout<<v[n-1].second<<v[n-1].second<<" ";
            }
        }
        for(int i=0;i<n-2;i++)
        {
            while(v[i].first!=0)
            {
            v[i].first--;
            cout<<v[i].second<<" ";
        }
        }
while(v[n-1].first!=0)
{
    cout<<v[n-2].second<<v[n-1].second<<" ";
    v[n-2].first--;
    v[n-1].first--;
}
cout<<endl;
    }
    return 0;
}
