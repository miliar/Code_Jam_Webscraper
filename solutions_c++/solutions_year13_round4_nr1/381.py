#include<iostream>
#include<cstdio>
#include<algorithm>
#include<vector>
using namespace std;
typedef long long ll;
int n,m;
int a[1024],b[1024],p[1024];

const ll mod=  1000002013;
ll before,after;

int main(){
	int ts=1,Ts;
	for(cin >>Ts;Ts--;++ts){
		cin >> n >> m;
		before=after = 0;
		vector<int> e;
		for(int i=0;i<m;++i){
			cin >> a[i] >> b[i] >> p[i];
			before = (before+(b[i]-a[i])*(ll)(b[i]-a[i]-1)/2%mod*p[i])%mod;
			e.push_back(a[i]);
			e.push_back(b[i]);
		}
		sort(e.begin(),e.end());
		e.resize(unique(e.begin(),e.end())-e.begin());
		int k = e.size()-1;
		vector<long long> s(k,0);
		for(int i=0;i<m;++i){
			int u = lower_bound(e.begin(),e.end(),a[i])-e.begin();
			for(;u<k && e[u+1]<=b[i] ;++u)
				s[u]+=p[i];
		}
		//cout << s.size() << endl;
		for(bool conti = true;conti;){
			conti = false;
			for(int i=0,j;i<s.size();){
				if(s[i]==0){++i;continue;}
				conti = true;
				ll f = 1234567890ll<<28;
				for(j=i;j<s.size()&&s[j]>0;++j)
					f= min(f,s[j]);
				for(int t=i;t<j;++t)
					s[t]-=f;
				after = (after+(e[j]-e[i])*(ll)(e[j]-e[i]-1)/2%mod*(ll)f)%mod;
				i=j;
			}
		}
		int ans = (after-before+mod)%mod;
		cout << "Case #"<<ts << ": " <<
		ans << endl;
	}
}
