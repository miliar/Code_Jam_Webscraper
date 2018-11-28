#define ll long long
#define vi vector <int>
#define pii pair <int,int>
#define FOR(i, a, b) for (i = (a); i <= (b); i++)
#define REP(i, a) for (i = 0; i < (a); i++)
#define ALL(v) (v).begin(), (v).end()
#define SET(a, x) memset((a), (x), sizeof(a))
#define SZ(a) ((int)(a).size())
#define CL(a) ((a).clear())
#define SORT(x) sort(ALL(x))
#define mp make_pair
#define pb push_back
#define MAX(a,b) ((a)>(b)?(a):(b))
#define MIN(a,b) ((a)<(b)?(a):(b))

#define filer() freopen("in.txt","r",stdin)
#define filew() freopen("out.txt","w",stdout)

#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <queue>
#include <cassert>


using namespace std;

template<class X>void debug(vector<X>&v){for(int i=0;i<v.size();i++)cout<<v[i]<<" ";cout<<endl;}


vi va,vb,vk;
int n;

void tobin(vi &v,ll n)
{
    CL(v);
    while( n ){v.pb(n%2);n/=2;}
}

ll dp[70][2][2][2];


bool can(int p,int &f,int bit,vi &v)
{
    if( !f )
    {
        if(bit>v[p])return false;
        if(bit<v[p])f=1;
    }

    return true;
}

ll go(int p,int fa,int fb,int fk)
{
  //  cout<<p<<" "<<fa<<" "<<fb<<" "<<fk<<endl;

    ll &ret=dp[p][fa][fb][fk];
    if(ret!=-1)return ret;


    if(p==n)
    {
        return ret=(fa&&fb&&fk);
    }
    ret=0;

    for(int a=0;a<=1;a++)
    {
        for(int b=0;b<=1;b++)
        {
            int nfa=fa,nfb=fb,nfk=fk;

            if(!can( p,nfa,a,va ))continue;
            if(!can( p,nfb,b,vb ))continue;
            int k=a&b;
            if(!can(p,nfk,k,vk))continue;



            ret+=go(p+1,nfa,nfb,nfk);

        }
    }



    return ret;
}

int main()
{

    freopen("B-large.in","r",stdin);
  //  freopen("b2.out","w",stdout);

    int ks=0;

    int t;
    cin>>t;
   // cout<<t<<endl;
    while(t--)
    {


        ll a,b,k,ans=0;
        cin>>a>>b>>k;

        SET(dp,-1);

        printf("Case #%d: ",++ks);
     /*   int ans1=0;
        for(int i=0;i<a;i++)
        {
            for(int j=0;j<b;j++)
            {
                if( (i&j)<k )ans1++;
            }
        }*/


        if( k>=a && k>=b )
        {
            cout<<a*b<<endl;
            continue;
        }


        if(a<b)swap(a,b); /// a is large


        tobin(va,a);
        tobin(vb,b);
        tobin(vk,k);

        n=max(va.size(),vb.size());



        va.resize(n);
        vb.resize(n);
        vk.resize(n);

        reverse(ALL(va));
        reverse(ALL(vb));
        reverse(ALL(vk));


       // debug(va);
       // debug(vb);
       // debug(vk);


       ans=go( 0,0,0,0 );

      //  assert(ans1==ans);


        cout<<ans<<endl;
    }
    return 0;
}
