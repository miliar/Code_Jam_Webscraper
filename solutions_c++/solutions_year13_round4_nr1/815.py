#include <string>
#include <vector>
#include <algorithm>
#include <numeric>
#include <set>
#include <map>
#include <queue>
#include <iostream>
#include <sstream>
#include <cstdio>
#include <cmath>
#include <ctime>
#include <cstring>
#include <cctype>
#include <utility>
#include <cstdlib>
#include <cassert>

#define rep(i,n) for(int (i)=0;(i)<(int)(n);++(i))
#define foreach(c,itr) for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();itr++)
#define rer(i,l,u) for(int (i)=(int)(l);(i)<=(int)(u);++(i))
#define reu(i,l,u) for(int (i)=(int)(l);(i)<(int)(u);++(i))
#define all(o) (o).begin(), (o).end()
#define pb(x) push_back(x)
#define mp(x,y) make_pair((x),(y))
#define mset(m,v) memset(m,v,sizeof(m))
#define EPS 1e-9
#define gi(a) int a; cin>>a
#define gi2(a,b) int a,b; cin>>a>>b
#define read(_type,name) _type name; cin>>name
#define read2(_type,name1,name2) _type name1,name2; cin>>name1>>name2
#define pi 3.141592653589793238

using namespace std;

typedef vector<int> vi; typedef pair<int,int> pii; typedef vector<pair<int,int> > vpii;
typedef long long ll; typedef pair<double,double> pdd; typedef unsigned int ui;

const ll mod=1000002013;

ll cal(ll n, ll k)
{
    if(k%2==0)return (2*n-k+1)%mod*k/2%mod;
    else return (2*n-k+1)/2%mod*k%mod;
}

main()
{
    //std::ios::sync_with_stdio(false);
    freopen("A-large.in","r",stdin);
    freopen("A.out","w",stdout);
    gi(T);
    rep(tt,T)
    {
        gi2(n,m);
        vpii a;
        ll ans=0;
        rep(i,m)
        {
            int o,e;
            ll p;
            cin>>o>>e>>p;
            ans+=p*cal(n,e-o)%mod;
            ans%=mod;
            a.pb(mp(o,-p));
            a.pb(mp(e,p));
        }
        sort(all(a));
        //cout<<ans<<endl;
        
        /*rep(i,a.size())
            cout<<a[i].first<<' '<<a[i].second<<endl;*/
        
        vpii s;
        int res=0;
        rep(i,a.size())
        {
            /*rep(i,s.size())cout<<s[i].first<<' '<<s[i].second<<endl;
            cout<<"-----------"<<res<<endl;*/
            if(a[i].second<0)
            {
                s.pb(a[i]);
            } else {
                assert(s.size()>0);
                while(s.size()&&a[i].second+s[s.size()-1].second>=0)
                {
                    a[i].second+=s[s.size()-1].second;
                    //int t;
                    /*
                    cout<<s[s.size()-1].second<<endl;
                    
                    cout<<(t=cal(n,a[i].first-s[s.size()-1].first)*(-s[s.size()-1].second))<<endl;
                    */
                    res+=cal(n,a[i].first-s[s.size()-1].first)%mod*(ll)(-s[s.size()-1].second)%mod;
                    res%=mod;
                    s.pop_back();
                }
                assert(a[i].second>=0);
                if(a[i].second)
                {
                    res+=cal(n,a[i].first-s[s.size()-1].first)%mod*(ll)a[i].second%mod;
                    res%=mod;
                    s[s.size()-1].second+=a[i].second;
                    if(s[s.size()-1].second==0)s.pop_back();
                }
            }
        }
        //cout<<res<<endl;
        ll tmp=ans-res;
        while(tmp<0)tmp+=mod;
        tmp%=mod;
        printf("Case #%d: %d\n",tt+1,tmp);
    }
}

