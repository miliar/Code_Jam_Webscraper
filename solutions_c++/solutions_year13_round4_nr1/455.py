#include<iostream>
#include<sstream>
#include<cstdio>
#include<cctype>
#include<string>
#include<cmath>
#include<map>
#include<set>
#include<queue>
#include<vector>
#include<cstring>
#include<algorithm>

#define ll long long
#define inf 1000000009
#define mod 1000000007

using namespace std;

typedef pair<int,int> II;
struct node{
    int x,p,c;
    node(){}
    node(int x,int p,int c):x(x),p(p),c(c){}
};
bool cmp(const node &a,const node &b)
{
    if(a.x!=b.x) return a.x<b.x;
    return a.p<b.p;
}
ll cal(int l,int r,int n)
{
    int d=r-l;
    return (2ll*n-d+1)*d/2;
}
void go(int cas)
{
    ll res=0;
    int n,m;
    vector<node> v;
    map<int,ll> h;
    map<int,ll>::iterator it;
    cin>>n>>m;
    for(int i=1;i<=m;i++)
    {
        node tmp;
        int l,r,c;
        scanf("%d%d%d",&l,&r,&c);
        res+=c*cal(l,r,n);
        v.push_back(node(l,0,c));
        v.push_back(node(r,1,c));
    }
    sort(v.begin(),v.end(),cmp);
    
    for(int i=0;i<v.size();i++)
    {
        if(v[i].p==0)
        {
            h[v[i].x]+=v[i].c;
        }
        else
        {
            ll tmp=v[i].c;
            int x=v[i].x;
            while(tmp)
            {
                it=h.end();
                it--;
                int t=min(it->second,tmp);
                it->second-=t;
                tmp-=t;
                res-=cal(it->first,x,n)*t;
                if(it->second==0) h.erase(it);
            }
        }
    }
    cout<<"Case #"<<cas<<": "<<res<<endl;
}

int main()
{
    //freopen("in","r",stdin);
    //freopen("out","w",stdout);
    int T;
    cin>>T;
    for(int run=1;run<=T;run++) go(run);
    //fclose(stdout);
}
