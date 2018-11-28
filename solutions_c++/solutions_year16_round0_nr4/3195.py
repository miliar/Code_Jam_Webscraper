#include <bits/stdc++.h>
using namespace std;
#define MEM(a) memset(a,0,sizeof(a))
#define rp(i,a,n) for ( i=a;i<n;i++)
#define pr(i,a,n) for ( i=n-1;i>=a;i--)
#define pb push_back
#define mp make_pair
#define all(x) (x).begin(),(x).end()
#define sz(x) ((int)(x).size())
#define F first
#define S second
#define IT(c,itr) for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();itr++)
#define MAX 105000
typedef vector<int> vi;
typedef long long ll;
typedef pair<int,int> pii;
typedef vector<pii> vii;
typedef vector<ll> vll;
const ll mod=1000000007;
int dr[8] = {1,1,0,-1,-1,-1, 0, 1};
int dc[8] = {0,1,1, 1, 0,-1,-1,-1};
int dh[4] = {0, 1, 0, -1};
int dv[4] = {-1, 0, 1, 0};
ll powmod(ll a,ll b) {ll res=1;a%=mod;for(;b;b>>=1){if(b&1)res=res*a%mod;a=a*a%mod;}return res;}
void solve(int pp)
{
    int n,i,j;
    ll k,c,s;
    cin>>k>>c>>s;
    vector<ll> v(k,0),t(k,1);

    cout<<"Case #"<<pp<<": ";
    if(c==1)
    {
        if(k==s) rp(i,1,k+1) cout<<i<<' ';
        else cout<<"IMPOSSIBLE";
        cout<<endl;
    }
    else
    {
        if(c*s<k) { cout<<"IMPOSSIBLE"<<endl; }
        else {rp(i,0,k) cout<<i+1<<' ';
        cout<<endl;}

    }
}
int main()
{
    freopen("in.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t;cin>>t;
    int qq; rp(qq,1,t+1)
    {
        solve(qq);
    }
    return 0;
}
