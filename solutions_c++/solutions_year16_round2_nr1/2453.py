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
ll powmod(ll a,ll b) {ll res=1;a%=mod;for(;b;b>>=1){if(b&1)res=res*a%mod;a=a*a%mod;}return res;}
int dr[8] = {1,1,0,-1,-1,-1, 0, 1};
int dc[8] = {0,1,1, 1, 0,-1,-1,-1};
int dh[4] = {0, 1, 0, -1};
int dv[4] = {-1, 0, 1, 0};
int v[26];
void solve(int yy)
{
    string s;cin>>s;MEM(v);//cout<<s<<endl;
    int i; vi  a;a.clear();
    rp(i,0,s.size())
    {
        int x=s[i]-'A';
        v[x]++;
    }
    if(v['z'-'a'])
    {
        rp(i,0,v['z'-'a']) {a.pb(0);v['e'-'a']--;v['r'-'a']--;v['o'-'a']--;}
        v['z'-'a']=0;
    }
    if(v['w'-'a'])
    {
        rp(i,0,v['w'-'a']) {a.pb(2);v['t'-'a']--;v['o'-'a']--;}
        v['w'-'a']=0;
    }
    if(v['x'-'a'])
    {
        rp(i,0,v['x'-'a']) {a.pb(6);v['s'-'a']--;v['i'-'a']--;}
        v['x'-'a']=0;
    }
    if(v['g'-'a'])
    {
        rp(i,0,v['g'-'a']) {a.pb(8);v['e'-'a']--;v['i'-'a']--;v['h'-'a']--;v['t'-'a']--;}
        v['g'-'a']=0;
    }
    if(v['u'-'a'])
    {
        rp(i,0,v['u'-'a']) {a.pb(4);v['f'-'a']--;v['o'-'a']--;v['r'-'a']--;}
        v['u'-'a']=0;
    }
    if(v['f'-'a']>0)
    {
        rp(i,0,v['f'-'a']) {a.pb(5);v['i'-'a']--;v['v'-'a']--;v['e'-'a']--;}
        v['f'-'a']=0;
    }
    if(v['r'-'a']>0)
    {
        rp(i,0,v['r'-'a']) {a.pb(3);v['t'-'a']--;v['h'-'a']--;v['e'-'a']--;v['e'-'a']--;}
        v['r'-'a']=0;
    }
    if(v['i'-'a']>0)
    {
        rp(i,0,v['i'-'a']) {a.pb(9);}
        v['i'-'a']=0;
    }
    if(v['o'-'a']>0)
    {
        rp(i,0,v['o'-'a']) {a.pb(1);}
        v['o'-'a']=0;
    }
        if(v['s'-'a']>0)
    {
        rp(i,0,v['s'-'a']) {a.pb(7);}
        v['v'-'a']=0;
    }
    sort(all(a));
    cout<<"Case #"<<yy<<": ";
    rp(i,0,a.size()) cout<<a[i];
    cout<<endl;
}
int main()
{
    freopen("in.in","r",stdin);
   freopen("out.txt","w",stdout);
    int t,y;cin>>t;
    rp(y,1,t+1) solve(y);
    return 0;
}
