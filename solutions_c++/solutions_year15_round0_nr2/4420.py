#include<bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int,int> pii;
typedef vector<int> vi;
typedef vector<long long> vll;
typedef vector<vector<int> > vvi;
typedef vector<string> vs;
typedef vector<pair<int,int> > vpii;

#define pb push_back
#define mp make_pair
#define PI acos(-1)
#define all(a) (a).begin(),(a).end()
#define len(a) ((int)(a).size())
#define mem(a,n) memset(a,n,sizeof(a))
#define eps 1e-9
#define rep(i,n) for(int i=0;i<(n);i++)
#define repi(i,a,n) for(int i=(a);i<(n);i++)
#define repr(i,a,n) for(int i=(n);i>=(a);i--)


int ans=0,mxd;

void bt(vi v,int t){
	if(t>mxd || t>ans)return;
	sort(all(v));
	ans = min(ans,t+v.back());
	if(v.back()<=3) return;
	
	repi(i,1,v.back()/2+1){
		vi tv = v;
		tv[len(tv)-1] = i;
		tv.pb(v.back()-i);
		bt(tv,t+1);
	}
	

	
}


int main(void){
	ios_base::sync_with_stdio(0);
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	
	int tst;
	cin>>tst;
	repi(ks,1,tst+1){
		int n;
		cin>>n;
		vi v(n);
		mxd = -1;
		rep(i,n){
			cin>>v[i];
			mxd = max(mxd,v[i]);
		}
		ans = 999999999;
		bt(v,0);
		cout<<"Case #"<<ks<<": "<<ans<<endl;
	}
	
	//~ cout<<1.0*clock()/CLOCKS_PER_SEC<<endl;
	
	return 0;
}
