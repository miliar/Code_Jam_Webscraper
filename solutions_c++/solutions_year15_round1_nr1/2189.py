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
    int main()
    {
        ll t,z,i,j,k,n,m,p,q,r,s,x,y;
        scanf("%lld",&t);
        for(z=1;z<=t;z++)
        {
            ll arr[1010];
            y=0;
            ll mx=0;
            ll ans=0;
           scanf("%lld",&n);
            for(i=0;i<n;i++)
                scanf("%lld",&arr[i]);
            for(i=1;i<n;i++)
            {
                if(arr[i]<=arr[i-1])
                {
                    y+=arr[i-1]-arr[i];
                }
              
                if(arr[i-1]>arr[i])
                    mx=max(mx,arr[i-1]-arr[i]);
            }
            //cout<<mx<<endl;
            for(i=1;i<n;i++)
            {
                    ans+=min(mx,arr[i-1]);
                    //cout<<ans<<endl;
            }
            printf("Case #%lld: %lld %lld\n",z,y,ans);
            
        }
        return 0;
    }