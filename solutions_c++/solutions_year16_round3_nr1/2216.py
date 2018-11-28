#include<bits/stdc++.h>
using namespace std;
bool qf=false;      //fast io enabled/disabled

#define input       freopen("in.txt","r",stdin);
#define output      freopen("out.txt","w",stdout);
#define fast        ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);qf=true;

#define sc          scanf
#define pr          printf
#define whi         while
#define ll          long long
#define ull         unsigned long long
#define lld         I64d
#define ff          first
#define ss          second
#define vc          vector
#define pb          push_back
#define ite         iterator
#define str         string
#define bl          bool
#define tr          true
#define fl          false
#define ct          continue;
#define endl        '\n'
#define ret         return
#define rsort       greater<int>()
#define nl          if(qf==tr) pr("\n");else cout<<"\n";
#define gcd(a,b)    __gcd(a,b)
#define mod         1000000007
#define tc          int t;if(qf==fl) scanf("%d",&t); else cin>>t;whi(t--)

#define all(c)      c.begin(),c.end()
#define sz(c)       c.size()
#define clr(c)      c.clear()
#define fd(c,a)     c.find(a)
#define bg(c)       c.begin()
#define ed(c)       c.end()
#define ins(c,a)    c.insert(a)
#define rem(c,a)    c.erase(a)



pair <int,char> a[30];

int main()
{
    input;
    output;
    int bzbz=1;
    tc
    {
        int n,i,x;
        sc("%d",&n);
        for(i=0;i<n;i++)
        {
            sc("%d",&x);
            a[i]={x,'A'+i};
        }
        pr("Case #%d: ",bzbz++);
        int sum,num1,num2;
        whi(1)
        {
            sort(a,a+n);
            if(a[n-1].ff==0) break;
            sum=0;
            for(i=n-1;i>=0 and a[i].ff!=0;i--)
            {
                sum+=a[i].ff;
            }
            if(a[n-2].ff==0)
            {
                if(a[n-1].ff==1)
                {
                    pr("%c",a[n-1].ss);
                    a[n-1].ff-=1;
                    break;
                }
                else
                {
                    pr("%c%c",a[n-1].ss);
                    a[n-1].ff-=2;
                }
            }
            else
            {
                num1=a[n-1].ff;
                num2=a[n-2].ff;
                if(num1<=((sum-2)/2.))
                {
                    pr("%c%c ",a[n-1].ss,a[n-2].ss);
                    a[n-1].ff--;
                    a[n-2].ff--;
                }
                else
                {
                    pr("%c ",a[n-1].ss);
                    a[n-1].ff--;
                }
            }
        }
        nl
    }
    ret 0;
}
