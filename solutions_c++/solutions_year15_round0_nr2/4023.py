    #include<bits/stdc++.h>
    using namespace std;
    typedef long long ll;
    typedef vector<ll>vll;
    typedef pair<ll,ll> pll;
    #define xx first
    #define yy second
    #define maxx(a, b, c) ((a > b? (a > c? a : c) : (b > c? b : c)))
    #define rep(n) for(i=0;i<n;i++)
    void read(ll &n)
    {   scanf("%lld",&n);
    }
    ll val[][2]={{0,0},{0,1},{0,2},{0,3},{1,2},{1,3},{2,3},{2,3},{2,3},{2,3}};
    ll solve(priority_queue<ll> arr,ll &maxi)
    {
        if(arr.empty())
            return 0;
        ll cur=arr.top();
        arr.pop();
        if(cur<=maxi)return 0;
        if(cur<=3){maxi=cur; return 0;}
        ll maxx=maxi;
        ll mx=cur,ret=0,ans,v,v2;
        priority_queue<ll> temp;
        for(int i=2;i<=cur/2;i++)
        {
            maxi=maxx;
            temp=arr;
            temp.push(i);
            temp.push(cur-i);
            v=solve(temp,maxi)+1;
            //cout<<v<<" "<<maxi<<" "<<i<<endl;
            if(v+maxi<(mx+ret))
            {
                mx=maxi;
                ret=v;
            }
        }
        maxi=mx;
        return ret;

    }
    int main()
    {
        ll t,z,i,j,k,n,m,p,q,r,s,x,y;
        scanf("%lld",&t);
        for(z=1;z<=t;z++)
        {
           ll ans=0,mx;
           priority_queue<ll> arr;
           char str[1020];
           scanf("%lld ",&n);
           for(i=0;i<n;i++)
            {scanf("%lld",&x);
        arr.push(x);
    }
            mx=0;
        ans=solve(arr,mx);
        //cout<<ans<<"jk"<<mx<<endl;
            printf("Case #%lld: %lld\n",z,ans+mx);
            
        }
        return 0;
    }