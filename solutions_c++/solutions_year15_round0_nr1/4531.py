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
           ll ans=0;
           x=0;
           char str[1020];
           scanf("%lld %s",&n,str);
           for(i=0;i<=n;i++)
           {
                if(i<=x)
                {
                    x+=str[i]-'0';
                }
                else{
                    ans+=i-x;
                    x+=i-x+str[i]-'0';
                }
           }
            printf("Case #%lld: %lld\n",z,ans);
            
        }
        return 0;
    }