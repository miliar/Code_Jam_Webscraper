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
ll sleep[1000001];
int main()
{
    read;
    write;
    ll n,i,j,counter;
    for(n=1;n<=1000000;n++)
    {
        ll a[12]={},here;
        bl ans;
        counter=1;
        whi(1)
        {
            ans=tr;
            i=n*counter;
            whi(i)
            {
                a[i%10]++;
                i/=10;
            }
            for(i=0;i<10;i++) if(a[i]==0) ans=fl;
            here=n*counter;
            if(ans==tr) break;
            counter++;
        }
        sleep[n]=here;
    }
    int mcd=1;
    tc
    {
        ll n;
        sc("%lld",&n);
        if(n==0) pr("Case #%d: INSOMNIA\n",mcd);
        else pr("Case #%d: %lld\n",mcd,sleep[n]);
        mcd++;
    }
    ret 0;
}
