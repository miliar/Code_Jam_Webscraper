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

int a[1001];

bool p(int x, int N)
{
    int i;
    rep(i,0,N-1)
        if((max(a[i]-x,0))>a[i+1])
            return false;
    return true;
}
int bin_search(int low, int high, int N)
{
    int mid;
    while(low<high)
    {
        mid = low + (high-low)/2;
        if(p(mid,N))
            high=mid;
        else
            low=mid+1;
    }
    if(!p(low,N))
        return -1;
    return low;
}

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out_large.txt","w",stdout);

   int T,i,res;
   cin>>T;
   for(int tt=1;tt<=T;tt++)
   {
       int N,m=-1;
       cout<<"Case #"<<tt<<": ";
       cin>>N;
       rep(i,0,N)
       {
           cin>>a[i];
           m=max(a[i],m);
       }
       res=0;
       rep(i,0,N-1)
            if(a[i+1]<a[i])
                res+=(-a[i+1]+a[i]);
        cout<<res<<" ";
        res=0;
        int x = bin_search(0,m+1,N);
        rep(i,0,N-1)
            if(a[i]-x>=0)
                res+=x;
            else
                res+=a[i];
        cout<<res<<endl;
   }
}
