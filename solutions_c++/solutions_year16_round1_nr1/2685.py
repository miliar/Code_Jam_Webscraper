#include<bits/stdc++.h>

#define MOD 1000000007
#define MAX 100005
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

int main(){
	
	freopen("A-large.in","r",stdin);
	freopen("A2.out","w",stdout);
	
	int t;
	sd(t);
	for(int tt=1;tt<=t;tt++){
		string s;
		cin>>s;
		
		int l=s.length();
		
		string ans;
		
		ans+=s[0];
		
		for(int i=1;i<l;i++){
			if(s[i]>=ans[0]) ans=s[i]+ans;
			else ans+=s[i];
		}
		
		cout<<"Case #"<<tt<<": "<<ans<<endl;
	}
}
