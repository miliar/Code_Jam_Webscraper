
#include<bits/stdc++.h>
using namespace std;

typedef long long  ll;
typedef unsigned long long  ull;

#define fast      ios_base::sync_with_stdio(false)
#define frmlty     int test_case;cin>>test_case;while(test_case--)

#define vi        vector<int>
#define vs        vector<string>
#define vll       vector<LL>
#define pii       pair<int,int>

#define msi       map<string,int>
#define msit      map<string,int>::iterator
#define pb        push_back
#define mp        make_pair



#define loop(i,a,b)      for(int i=a;i<b;i++)
#define rloop(i,a,b)     for(int i=b-1;i>=a;i--)

#define gcd(a,b)  __gcd(a,b)
#define mod       1000000007

int main()
{
    ll t;
    cin>>t;
    ll s,count1,n;
    string r;
    ll ans=0;
    for(ll j=1;j<=t;j++)
    {   ans=0;
        count1=0;
        n=0;
        cin>>s>>r;
        count1=r[0]-48;
        ll i;
        for( i=1;i<r.length();i++)
        {
            if(count1>=i)
            {
               count1=count1+(r[i]-48);
            }
            else {
                ans=ans+i-count1;
                count1=i+(r[i]-48);

            }

        }
        cout<<"Case #"<<j<<": "<<ans<<endl;
    }
}
