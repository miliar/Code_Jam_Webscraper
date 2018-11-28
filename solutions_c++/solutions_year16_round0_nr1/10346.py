#include<bits/stdc++.h>
#include <iostream>
#include <numeric>
#define ll long long
#define ull unsigned long long  
#define mpa make_pair
#define pb push_back
#define ff first
#define ss second
#define boost ios_base::sync_with_stdio(0)
#define ss second
#define forp(i,a,b) for(ll i=a;i<=b;i++)
#define rep(i,n)    for(ll i=0;i<n;++i)
#define ren(i,n)    for(ll i=n-1;i>=0;i--)
#define forn(i,a,b) for(ll i=a;i>=b;i--)
#define fre     freopen("input.in","r",stdin),freopen("output.txt","w",stdout)
#define all(c) (c).begin(),(c).end()
#define tr(c,i) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define scan(x) scanf("%lld",&x)
#define clr(x,val) memset(x,val,sizeof(x))
using namespace std;
template<class T> inline void umax(T &a,T b){if(a<b) a = b ; }
template<class T> inline void umin(T &a,T b){if(a>b) a = b ; }
template<class T> inline T abs(T a){return a>0 ? a : -a;}
template<class T> inline T gcd(T a,T b){return __gcd(a, b);}
template<class T> inline T lcm(T a,T b){return a/gcd(a,b)*b;}
ll modpow(ll a,ll n,ll temp){ll res=1,y=a;while(n>0){if(n&1)res=(res*y)%temp;y=(y*y)%temp;n/=2;}return res%temp;} 
//ll a[100005],n,dp[1000005]={0},b[1000005],c[100005],dp1[1000005],bit[100005];
//ll vis[100005];
//vector<ll> adj[100005];
#define pi 3.1415926536
#define sz(x) x.size()
ll ison(ll mask,ll pos){
	return (mask&(1<<pos));
}
typedef vector<ll> vi;
typedef vector<vi> vvi;
typedef pair<ll, ll> pii;
ll cbit(ll n){ll k=0;while(n) n&=(n-1),k++;return k;}
ll nbit(ll n){ll k=0;while(n) n/=2,k++;return k;}
//ll b1[1001][1001],b2[1001][1001],g1[1001][1001],g2[1001][1001],w[1001][1001];
//bool a1[101][101],a2[102][101],a3[103][101];
ll mod=1e9+7;
int sgn(ll x) {
  return x < 0 ? -1 : !!x;
}
//pair<ll,ll> a[1000005];
/*void upd(ll ind,ll val){
    if(ind==0) return;
    while(ind<=n){
        bit[ind]+=val;
        ind+=(ind&-ind);
    }
}
ll qu(ll ind){
  ll k=0; while(ind>0){
    k+=bit[ind];
    ind-=(ind&-ind);
  }
    return k;
}*/


//ll tree[500005];

//vector<ll,pair<ll,ll> > b;
//vector<ll> adj[100005];

/*Tarjan incomplette
void dfs(ll s){
	vis[s]=1;
	for(ll i=0;i<adj[s].size();i++) if(!vis[adj[s][i]]) dfs(adj[s][i]);
    ofvs.pb(s);
}
void dfs2(ll s){
	vis[s]=1;
	if(wt[s]<optc){optn=0,optc=wt[s];}
	if(optc==wt[s]) optn++;
	for(ll i=0;i<rdj[s].size();i++) if(!vis[rdj[s][i]]) dfs2(rdj[s][i]);
}
*/
typedef pair<ll,pair<ll,ll> >ver;
//string s;
/*ll tree[200005];
ll a[100005];
void build(ll node,ll ss,ll se)
{
	if(ss==se) tree[node]=a[ss];
	else
	{
		ll mid=(ss+se)/2;
		build(2*node,ss,mid);
		build(2*node+1,mid+1,se);
        tree[node]=tree[2*node]&tree[2*node+1];
	}
}*/
/*void upd(ll node,ll ss,ll se,ll idx,ll val)
{
	if(ss==se)
	a[idx]=val,tree[node]=a[idx];
	else
	{
		ll mid=(ss+se)/2;
		if(ss<=idx && idx<=mid)
		upd(2*node,ss,mid,idx,val);
		else
		upd(2*node+1,mid+1,se,idx,val);
	    tree[node]=tree[node*2]+tree[node*2+1];
	}
}*/
/*ll query(ll node,ll ss,ll se,ll l,ll r)
{
	if(r<ss || se<l)
	return 0;
	if(l<=ss && se<=r)
	return tree[node];
	ll mid=(ss+se)/2;
	ll q1=query(node*2,ss,mid,l,r);
	ll q2=query(node*2+1,mid+1,se,l,r);
	return q1&q2;
}*/
/*ll pow(ll n){
	ll t=1,i=1;
	while(i<=n) t*=10;
	return t;
}*/
//stack<ll> help;
//ll dp[1ll<<11];

//ll csum[100005],b[100005],help[100005];
//vector<ll> adj[1005];
//vector<ll> ans;
/*ll kmp[1000005];
ll zee[1000005];
void kmpm(string p){
	ll i,j,k=0,l;
	kmp[0]=0;
	j=0;
	for(i=1;i<p.size();i++){
		while(k && p[i]!=p[k]) k=kmp[k-1];
		if(p[i]==p[k]) k++;
		kmp[i]=k;
	}
}
ll isp(ll n){
	ll f=1,i;
	for(i=2;i<=sqrt(n);i++) if(!(n%i)) return 0;
	return 1;
}*/
/*vector<ll> zFunction(vector<ll> &s) {
    int n = (ll) s.size();
    vector<ll> z (n);
    for (int i=1, l=0, r=0; i<n; ++i) {
        if (i <= r)
            z[i] = min (r-i+1, z[i-l]);
        while (i+z[i] < n && s[z[i]] == s[i+z[i]])
            ++z[i];
        if (i+z[i]-1 > r)
            l = i,  r = i+z[i]-1;
    }
    return z;
}*/
//map<ll,ll> help;
/*ll chk(ll val,ll n,ll m){
	ll t=0,i;
	val--;
	for(i=1;i<=n;i++) t+=min(m,val/i);
	return t;
}*/

/*ll size[100005];
void init(ll n)
{for(int i=1;i<=n;i++) a[i]=i;}
ll root(ll x)
{
	while(a[x]!=x)
	{
		a[x]=a[a[x]];
		x=a[x];
	}
	return x;
}
ll u1(ll x,ll y)
{
	int p=root(x);
	int q=root(y);
	a[p]=a[q];
}
*/
/*ll tree[100005];
void update(ll idx, ll val){
	while(idx < 100005){
		tree[idx] = max(tree[idx], val);
		idx += (idx & (-idx));
	}
}
ll query(ll idx){
	ll ret = 0;
	while(idx > 0){
		ret = max(ret, tree[idx]);
		idx -= (idx & (-idx));
	}
	return ret;
}*/
//pair<char ,pair<ll,ll> >p[5005];[10004]
/*
//(topsort)
vector<ll> adj[100005];
vector<ll> fino;
ll vis[100005];
void dfs(ll v){
vis[v]=1;
for(ll i=0;i<adj[v].size();i++) if(!vis[adj[v][i]])dfs(adj[v][i]);
fino.pb(v);
}
*/

ll xo(ll i)
{
	if ((i&3)==0) return i;
	if ((i&3)==1) return 1;
	if ((i&3)==2) return i+1;
	return 0;
}
//pair<ll,ll> p[10005];
ll a[100005];

int main(){
   ll n,t,i,j;
   fre;
   scan(t);
   ll tt=t;
   while(t--){
   	ll n;
   	scan(n);
   	if(n==0) printf("Case #%lld: %s\n",tt-t,"INSOMNIA");
   	else{
   		set<ll> x;
   		x.clear();
   		ll j=n;
   		ll k=1;
   		while(x.size()<10){
   			i=j*k;
   			while(i) x.insert(i%10),i/=10;
   			if(x.size()==10) break;
   			k++;
   		}
   		printf("Case #%lld: %lld\n",tt-t,j*k);
	}
   }
}


   
   
   

    
    
    
    

	 
   
   
    
   
   











 	
 	
 	
 	
 	
 
 
 









 	
 	
 	
 





  
  
  
  
  	

  
  
  
   
   
   



	














 
 
 
 
 
 
 
 
 
 
 
 
 

 
 
 
 
 
 
  
  
  




	
	
	









  
   	
   	

   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   	
   	
   	
   	
   	
  		
   		
	

	
	





	









    	
    	
    	
    	
    	
    	
	
    
		
		
		




	
	
	 
	 
	 
	 
	 
	 
	 
	 
	 
 	
  	
  
  
 
 
 

	 
	 

	  
	  
	  
	  
	  
    
    
    
    
    
    
    
    
    
   
