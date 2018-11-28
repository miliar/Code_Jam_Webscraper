#include<bits/stdc++.h>

#define gcd __gcd
#define bitcount __builtin_popcountll
#define getcx getchar
#define rep(i,j,n) for(i=j;i<n;i++)
#define tr(it,c) for(auto it=(c).begin();it!=(c).end();it++)
#define pb push_back
#define mp make_pair
#define hell 1000000007
#define uset unordered_set
#define umap unordered_map
#define ll long long

using namespace std;

const int MAXN = 1e3+10;

vector<int>v;

int solve(int N)
{
    int res = N+1,ans;
    for(int i = 1;i<=N;i++)
    {
        ans=i;
        tr(it,v)
        {
            if((*it)>i)
            {
                ans+=((*it)/i);
                if((*it)%i==0)
                    ans--;
            }
        }
        res=min(ans,res);
    }
    return res;
}

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("out2.txt","w",stdout);

   int T,x,i,D,k;
   cin>>T;
   for(int tt=1;tt<=T;tt++)
   {
       cin>>D;
       k=-1;
       rep(i,0,D)
       {
            cin>>x;
            k=max(k,x);
            v.pb(x);
       }
       cout<<"Case #"<<tt<<": "<<solve(k)<<endl;
       v.clear();
   }
}

