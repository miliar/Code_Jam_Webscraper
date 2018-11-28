#include<bits/stdc++.h>
using namespace std;
#define pb push_back
#define gcd(a,b) __gcd(a,b)
#define mp make_pair
#define fast cin.sync_with_stdio(0);cin.tie(0);
#define prr(n) cout<<n<<"\n";
#define ff first
#define setbits(x) __builtin_popcount(x)
#define ss second
#define forr(n) for(int i=0;i<n;i++)
typedef pair<int,int> pii;
typedef long long int ll;
const int si=1e5+7;
const int mod=1e9+7;
ll fexpo(ll a,ll b)
{
    if(b==1)
        return a;
    if(b==2)
       return a*a;
        if(b%2==0)
        return fexpo(fexpo(a,b/2),2);
    else
        return a*fexpo(fexpo(a,(b-1)/2),2);

}
int main()
{
freopen("haha.in","r",stdin);
    freopen("RRJJ.txt","w",stdout);
  //  ll h=2;
    int t;
    cin>>t;
    set<int> ms;
    for(int i=1;i<=t;i++)
    {
        ms.clear();
        ll h=2;
        ll n;
        cin>>n;
        ll kk=n;
        ll r;
        int hhh=1;
        if(n==0)

        {
            cout<<"Case #"<<i<<":"<<" INSOMNIA\n";
          //  hhh+=1;
            continue;
        }

        while(ms.size()!=10)
        {
            //
            //cout<<n<<endl;
             r=n;
            while(r!=0)
            {
                int hh=r%10;
                ms.insert(hh);
                r=r/10;
            }
            n=kk*h;
            h++;
        }
      cout<<"Case #"<<i<<":"<<" "<<n-kk<<endl;
     // hhh+=1;
    }
    return 0;
}
