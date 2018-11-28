#include<bits/stdc++.h>
using namespace std;
#define ll long long
vector <pair<ll,char> > v;
#define pb push_back
#define mp make_pair
vector <string> res;
int main()
{
freopen("input.in","r",stdin);
freopen("output.txt","w",stdout);
ll n,l,t,minm,k,x,i,j,a[30];
char c;
cin>>t;


for(k=1;k<=t;k++)
{
    v.clear();
res.clear();
    string temp;
cin>>n;
minm=INT_MAX;
for(c='A';c<='A'+n-1;c++)
{
    cin>>x;
    minm=min(minm,x);
    v.pb(mp(x,c));
}
//for(i=0;i<v.size();i++)
   // cout<<v[i].first<<" "<<v[i].second<<"\n";
//make all equal
sort(v.rbegin(),v.rend());
i=0;
while(1)
{
    if(i==0&&v[0].first==minm)
    break;


        if(v[i].first>minm)
        {
            v[i].first--;
            temp=v[i].second;
            res.pb(temp);

        }

    if(i==v.size()-1)
        i=0;
    else
        i++;
}


    for(i=2;i<v.size();i++)
    {
        while(v[i].first)
        {
            temp=v[i].second;
            res.pb(temp);
            v[i].first--;
        }
    }
    while(v[0].first)
    {
        temp=v[0].second;
        temp+=v[1].second;
        res.pb(temp);
        v[0].first--;
        }


    cout<<"Case #"<<k<<": ";
    for(i=0;i<res.size();i++)
        cout<<res[i]<<" ";
    cout<<"\n";
}
return 0;
}
