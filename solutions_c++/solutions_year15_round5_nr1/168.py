#include <iostream>
#include<algorithm>
#include<cstring>
#include<fstream>
#include<vector>
#include<string>
#define X first
#define Y second

using namespace std;

const int MAXN=1100000;
typedef pair<int,int> pii;
bool mark[MAXN];
long long As,Cs,Rs,Am,Cm,Rm,M0,s[MAXN];
int n,a[MAXN],ind,h[MAXN],fi[MAXN],e[MAXN],t[MAXN*4],flag[4*MAXN],MIN[MAXN*4],d,ans;
vector<int>G[MAXN];
vector<pii>vec;

void dfs(int v)
{
    mark[v]=true;
    a[ind]=h[v];
    fi[v]=ind++;
    for(int i=0;i<G[v].size();i++)
    {
        int u=G[v][i];
        if(!mark[u])
        {
            h[u]=h[v]+1;
            dfs(u);
        }
    }
    e[v]=ind;
}

void update(int x)
{
    t[x]=0;
    MIN[x]=min(MIN[2*x],MIN[2*x+1]);
    if(MIN[2*x]==MIN[x])
        t[x]+=t[2*x];
    if(MIN[2*x+1]==MIN[x])
        t[x]+=t[2*x+1];
}

void make(int node,int l,int r)
{
    if(l+1>=r)
    {
        MIN[node]=a[l];
        t[node]=1;
        return;
    }
    int mid=(l+r)/2;
    make(2*node,l,mid);
    make(2*node+1,mid,r);
    update(node);
}

void shift(int x)
{
    flag[2*x]+=flag[x];
    flag[2*x+1]+=flag[x];
    MIN[2*x]+=flag[x];
    MIN[2*x+1]+=flag[x];
    flag[x]=0;
}

void add(int node,int l,int r,int beg,int en,int val)
{
    if(beg<=l && r<=en)
    {
        flag[node]+=val;
        MIN[node]+=val;
        return;
    }
    shift(node);
    int mid=(l+r)/2;
    if(beg<mid) add(2*node,l,mid,beg,en,val);
    if(mid<en)  add(2*node+1,mid,r,beg,en,val);
    update(node);
}

int main()
{
    ifstream cin("A-small-attempt0.in");
    ofstream cout("A-small-attempt0.out");
    int qw;
    cin>>qw;
    for(int q=1;q<=qw;q++)
    {
        ind=0;
        vec.clear();
        memset(flag,0,sizeof flag);
        cin>>n>>d>>s[0]>>As>>Cs>>Rs>>M0>>Am>>Cm>>Rm;
        for(int i=0;i<n;i++)
            G[i].clear();
        vec.push_back(pii(s[0],0));
        for(int i=1;i<n;i++)
        {
            s[i]=(s[i-1]*As+Cs)%Rs;
            M0=(M0*Am+Cm)%Rm;
            G[M0%i].push_back(i);
           // cout<<M0%i<<"->"<<i<<endl;
            vec.push_back(pii(s[i],i));
        }
        sort(vec.begin(),vec.end());
        h[0]=1;
        memset(mark,false,sizeof mark);
        dfs(0);
   //     for(int i=0;i<n;i++)
     //       cout<<s[i]<<" "<<fi[i]<<" "<<e[i]<<endl;
        make(1,0,n);
        int p=0;
       // for(int i=0;i<vec.size();i++)
       //     cout<<a[i]<<" ";
      // cout<<endl;
        while(p<n && vec[p].X-vec[0].X<=d)
        {
         //   cout<<"+"<<p<<endl;
            add(1,0,n,fi[vec[p].Y],e[vec[p].Y],-1);
            p++;
        }
        ans=0;
        if(MIN[1]==0)
            ans=t[1];
        for(int i=1;i<n;i++)
        {
          //  cout<<"-"<<i<<endl;
            add(1,0,n,fi[vec[i-1].Y],e[vec[i-1].Y],1);
            while(p<n && vec[p].X-vec[i].X<=d)
            {
           //     cout<<"+"<<p<<endl;
                add(1,0,n,fi[vec[p].Y],e[vec[p].Y],-1);
                p++;
            }
            if(MIN[1]==0)
                ans=max(ans,t[1]);
        }
        cout<<"Case #"<<q<<": ";
        cout<<ans<<endl;
    }
}
