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
            bool flag=false;
           scanf("%lld %lld%lld",&n,&p,&q);
           if(n<7&&(p*q)%n==0&&max(p,q)>=n&&min(p,q)>=(n-1))
           {
            flag=true;
           }
            printf("Case #%lld: %s\n",z,(flag==true)?"GABRIEL":"RICHARD");
            
        }
        return 0;
    }