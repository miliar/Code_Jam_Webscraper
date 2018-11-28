#include<bits/stdc++.h>

#define MOD 1000000007
#define MAX 200000005
#define slld(t) scanf("%lld",&t)
#define sd(t) scanf("%d",&t)
#define pd(t) printf("%d\n",t)
#define plld(t) printf("%lld\n",t)
#define pcc pair<char,char>
#define pii pair<int,int>
#define pll pair<ll,ll>
#define tr(container,it) for(typeof(container.begin()) it=container.begin();it!=container.end();it++)
#define mp(a,b) make_pair(a,b)
#define FF first
#define SS second
#define pb(x) push_back(x)
#define vi vector<int>

using namespace std;

// Miller Rabin

typedef long long ll;
 
int T;
ll mod;
int b[]={2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97};
ll a[]={1996011519951206ll,1995120619960115ll,1995100319960115ll,195100319951206ll,1996011519951003ll};
 
 
ll multi(ll x,ll y)
{
	ll w=x*y-mod*(ll(double(x)*y/mod+1e-3));
	while(w<0)
		w+=mod;
	while(w>=mod)
		w-=mod;
	return w;
}
 
ll pow(ll x,ll y)
{
	ll t=1;
	while(y)
	{
		if(y&1)
			t=multi(t,x);
		x=multi(x,x);
		y>>=1;
	}
	return t;
}
 
bool judge(ll n)
{
	if(n==2) return true;
	if(n<2||!(n&1)) return false;
	for(int i=0;i<25;i++)
		if(n%b[i]==0&&n!=b[i])
			return false;
	mod=n;
	int t=0;
	ll u=n-1;
	while(!(u&1)) t++,u>>=1;
	for(int i=0;i<5;i++)
	{
		ll x=a[i]%(n-1)+1;
		x=pow(x,u);
		ll y=x;
		for(int j=1;j<=t;j++)
		{
			x=multi(x,x);
			if(x==1&&y!=1&&y!=n-1)
				return false;
			y=x;
		}
		if(x!=1) return false;
	}
	return true;
}

// -------

ll fact(ll ans){
	for(ll d=2;d*d<=ans;d++){
		if(ans%d==0) return d;
	}
}

vi ok;
int ans[12];

ll prime(int p){
	ll ans=0;
	ll pp=1;
	for(int i=ok.size()-1;i>=0;i--){
		ans+=ok[i]*pp;
		pp*=p;
	}
	if(judge(ans)) return 0;
	return fact(ans);
}

bool go(){
	for(int p=2;p<=10;p++){
		ans[p]=prime(p);
		if(!ans[p]) return 0;
	}
	return 1;
}

int main(){
	
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C.out","w",stdout);
	
	int t;
	sd(t);
	for(int tt=1;tt<=t;tt++){
		cout<<"Case #"<<tt<<":\n";
		
		int n,j;
		sd(n);sd(j);
		
		int cnt=0;
		
		int lim=1<<(n-2);
		
		for(int i=0;i<lim;i++){
			if(cnt==j) break;
			
			ok.clear();
			ok.pb(1);
			for(int j=0;j<n-2;j++){
				if(i&(1<<j)){
					ok.pb(1);
				}
				else ok.pb(0);
			}
			ok.pb(1);
			reverse(ok.begin(),ok.end());
			
			if(go()){
				for(int j=0;j<ok.size();j++) cout<<ok[j];
				cout<<" ";
				for(int p=2;p<=10;p++) cout<<ans[p]<<" ";
				cout<<endl;
				cnt++;
			}
		}
		
	}
}
