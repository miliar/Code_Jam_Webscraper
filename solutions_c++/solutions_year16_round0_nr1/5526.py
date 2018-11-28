#include<bits/stdc++.h>

#define MOD 1000000007
#define MAX 10000005
#define ll long long
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

bool d[10];

bool go(int n){
	ll k=1;
	while(n/k!=0){
		d[(n/k)%10]=1;
		k*=10;
	}
	for(int i=0;i<10;i++) if(!d[i]) return 0;
	return 1;
}

int main(){
	
	freopen("A-large.in","r",stdin);
	freopen("A-out-large.out","w",stdout);
	
	int t;
	sd(t);
	for(int tt=1;tt<=t;tt++){
		int n;
		sd(n);
		
		if(!n) cout<<"Case #"<<tt<<": INSOMNIA\n";
		else{
			for(int i=0;i<10;i++) d[i]=0;
			
			int ans=-1;
			bool ok=go(n);
			
			for(int i=2;i<=100;i++){
				ok=go(i*n);
				if(ok){
					ans=i*n;
					break;
				}
			}
			
			if(ans!=-1) cout<<"Case #"<<tt<<": "<<ans<<"\n";
			else cout<<"Case #"<<tt<<": INSOMNIA\n";
		}
	}
}
