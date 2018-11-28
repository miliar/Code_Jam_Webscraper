#include<bits/stdc++.h>              
//------------------------------------------------------------//
//  ___  ___ _____ ______                                     //
//  |  \/  |/  ___|| ___ \     This C++ Template Belongs to   //                   
//  | .  . |\ `--. | |_/ /        Manish Singh Bisht          //
//  | |\/| | `--. \| ___ \       http://fb.me/manish05        //    
//  | |  | |/\__/ /| |_/ /    Email: manish_05@ymail.com    //
//  \_|  |_/\____/ \____/                                     //    
//------------------------------------------------------------//
using namespace std;
#define DEBUG 1
#define debug(x) if(DEBUG){cout<<#x<<":"<<x<<endl;}
#define debug2(x,y) if(DEBUG){cout<<#x<<":"<<x<<" , "<<#y<<":"<<y<<endl;}
#define debugp(x) debug2(x.ft,x.sd)
#define debugv(v) if(DEBUG){cout<<#v<<endl;TR(v,it)cout<<*it<<" ";cout<<endl;}
#define debugar(ar,n) if(DEBUG){cout<<#ar<<endl;FOR(i,n)cout<<ar[i]<<" ";cout<<endl;}
#define debugmm(mp,n,m) if(DEBUG){cout<<#mp<<"("<<#n<<" x "<<#m<<")"<<endl;\
		FOR(i,m+1)cout<<(i<10?"0":"")<<i<<(i?"":"|")<<"\t";cout<<"\n``";FOR(i,m)cout<<"````";\
		FOR(i,n){cout<<endl<<(i<9?"0":"")<<i+1<<"|\t";FOR(j,m)cout<<mp[i][j]<<"\t";}cout<<endl;}
#define debugm(mp,n) debugmm(mp,n,n)
#define FOR(i,n) for(ll i=(0);i<(n);++i)
#define TR(v,it) for(typeof(v.begin()) it(v.begin());it!=v.end();++it)
#define SZ(v) ((ll)(v.size()))
#define CLEAR(a) memset((a),0,sizeof(a))
#define pb push_back
#define mp make_pair
#define VI vector<ll>
#define SI set<ll>
#define PII pair<ll,ll>
#define ft first
#define sd second
#define all(a) a.begin(),a.end()
#define lb lower_bound
#define ub upper_bound
#define inf INT_MAX
#define inff LLONG_MAX
#define PNL cout<<endl
#define md 1000000007
typedef int ll;
ll MAXN = 1000010;
ll modPow(ll a,ll b,ll m) {
    a %= m;
    ll r = 1;
    while (b > 0) {
        if (b & 1) r = (r * a) % m;
        a = (a * a) % m;
        b >>= 1;
    }
    return r;
}
string convertLL(ll number){stringstream ss;ss << number;return ss.str();}
ll convertString(string s){ll num;stringstream sstr(s);sstr>>num;return num;}
ll gcd(ll a,ll b){return b?gcd(b,a%b):a; }

int main()
{	ios_base::sync_with_stdio(false);cin.tie(0);
    ll t,T=1;
    cin>>t;
    while(t--)
    {
    	ll ans = 0;
    	ll n,ar[1001];
    	cin>>n;
    	FOR(i,n)cin>>ar[i];
    	sort(ar,ar+n);
    	ans = ar[n-1];
    	FOR(i,ar[n-1]){
    		ll tmp = i + 1;
    		FOR(j,n)
    		  tmp += (ar[j]-1)/(i+1);
    		ans = min(tmp,ans);
    	}
    	cout << "Case #" << T++ << ": "<<ans<<"\n";
    }
    return 0;
}