#include <bits/stdc++.h>
using namespace std;
#define ll long long int
#define pb push_back
#define f first
#define s second
#define mod 1000000007
#define inf 1e8

#define pi pair<ll,ll>
#define pii pair<pi,ll>
#define f first
#define mp make_pair
#define s second
#define rep(i,n) for(ll i=0;i<n;i++)
#define forup(i,a,b) for(ll i=a;i<=b;i++)
vector<string>split(string s){
	vector<string>v;
	string ans="";
	for(int i=0;i<s.length();i++){
		if(s[i]==' '){
			v.pb(ans);
			ans="";
		}
		else{
			ans+=s[i];
		}
	}
	v.pb(ans);
	return v;
}
int main(){

	freopen("C-small-attempt0.in","r",stdin);
	freopen("output.txt","w",stdout);
	int t,n;
	int cnt=0;
	cin>>t;
	while(t--){
		cnt++;
		cin>>n;
		cin.ignore();
		string a,b;
		getline(cin,a);
		getline(cin,b);
		vector<string>v(n-2);
		rep(i,n-2)
			getline(cin,v[i]);
		vector<vector<string>>d;
		rep(i,n-2){
			d.pb(split(v[i]));
		}

		d.pb(split(a));
		d.pb(split(b));

		ll sz=(1<<(n-2));
		int r=n-2;
		int ans=1e9;
		int temp=0;
		map<string,bool>f,e;
		for(int mask=0;mask<sz;mask++){

			rep(i,r){
				if(mask&(1<<i)){
					for(auto x:d[i]){
						f[x]=1;
					}
				}
				else{
					for(auto x:d[i]){
						e[x]=1;
					}
				}
			}
			for(auto x:d[n-2]){
				e[x]=1;
			}
			for(auto x:d[n-1]){
				f[x]=1;
			}
			temp=0;
			for(auto x:f){
				if(e[x.f]==1) temp++;
			}
			ans=min(ans,temp);
			e.clear();
			f.clear();
		}
		printf("Case #%d: %d\n",cnt,ans);
	}
}
