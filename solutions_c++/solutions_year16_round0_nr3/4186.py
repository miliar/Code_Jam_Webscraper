#include<bits/stdc++.h>
using namespace std;
int yt=1;           //test variable
bool qf=false;      //fast io enabled/disabled

#define read        freopen("in.txt","r",stdin)
#define write       freopen("out.txt","w",stdout)
#define fast        ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);qf=true;

#define sc          scanf
#define pr          printf
#define whi         while
#define ll          long long
#define ull         unsigned long long
#define lld         I64d
#define mp          make_pair
#define ff          first
#define ss          second
#define vc          vector
#define pb          push_back
#define ite         iterator
#define str         string
#define bl          bool
#define tr          true
#define fl          false

#define endl        '\n'
#define ret         return
#define rsort       greater<int>()
#define nl          if(qf==tr) pr("\n");else cout<<"\n";
#define test        if(qf==tr) pr("TEST %d\n",yt++);else cout<<"TEST "<<yt++<<"\n";
#define gcd(a,b)    __gcd(a,b)
#define mod         1000000007

#define all(c)      c.begin(),c.end()
#define sz(c)       c.size()
#define clr(c)      c.clear()
#define fd(c,a)     c.find(a)
#define bg(c)       c.begin()
#define ed(c)       c.end()
#define ins(c,a)    c.insert(a)
#define rem(c,a)    c.erase(a)

#define si(n)       if(qf==fl) sc("%d",&n); else cin>>n;
#define sll(n)      if(qf==fl) sc("%lld",&n); else cin>>n;
#define pi(n)       if(qf==fl) pr("%d ",n); else cout<<n<<" ";
#define pll(n)      if(qf==fl) pr("%lld ",n); else cout<<n<<" ";

#define tc          int t;if(qf==fl) si(t) else cin>>t;whi(t--)
#define ct          continue
#define debug       system("PAUSE");
ll i,j;
vc <bl> prime(100000001,tr);
ll power(ll a)
{
    ll i,p=1;
    for(i=1;i<=a;i++) p*=2;
    ret p;
}
vc <ll> xyz;
int main()
{
    write;
    for(i=4;i<=100000000;i+=2) prime[i]=fl;
    for(i=3;i<=10000;i+=2)
    {
        if(prime[i]==tr)
        {
            for(j=i*i;j<=100000000;j+=i) prime[j]=fl;
        }
        if(i%6==1) i+=2;
    }
    xyz.pb(2);
    for(i=3;i<=100000000;i+=2)
    {
        if(prime[i]==tr) xyz.pb(i);
        if(i%6==1) i+=2;
    }
    sc("%lld",&i);
    ll n,z;
    sc("%lld%lld",&n,&z);
    pr("Case #1:\n");
    ll till=power(n)-1,a[50],top,base,val,p,r,fokat=0;
    for(i=0;fokat<z and i<=till;i++)
    {
        j=i;
        top=0;
        whi(top<n)
        {
            a[top++]=j%2;
            j/=2;
        }
        if(a[0]!=a[top-1] or a[0]==0) ct;
        bl jamcoin;
        for(base=2;base<=10;base++)
        {
            jamcoin=fl;
            val=0;
            p=1;
            for(j=n-1;j>=0;j--)
            {
                val=val+p*a[j];
                p*=base;
            }
            r=sqrtl(val);
            for(j=2;j<=r;j++)
            {
                if(val%j==0)
                {
                    jamcoin=tr;
                    break;
                }
            }
            if(jamcoin==fl) break;
        }
        if(jamcoin==tr)
        {
            for(j=0;j<n;j++) pr("%lld",a[j]);
            pr(" ");
            for(base=2;base<=10;base++)
            {
                jamcoin=fl;
                val=0;
                p=1;
                for(j=n-1;j>=0;j--)
                {
                    val=val+p*a[j];
                    p*=base;
                }
                r=sqrtl(val);
                for(j=2;j<=r;j++)
                {
                    if(val%j==0)
                    {
                        pr("%lld ",j);
                        break;
                    }
                }
            }
            pr("\n");
            fokat++;
        }
    }
    ret 0;
}
