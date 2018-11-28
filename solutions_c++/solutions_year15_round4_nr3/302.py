#include <bits/stdc++.h>
#define rep(i,n) for(int i=0;i<(int)(n);i++)
#define rep1(i,n) for(int i=1;i<=(int)(n);i++)
#define all(c) c.begin(),c.end()
#define pb push_back
#define fs first
#define sc second
#define show(x) cout << #x << " = " << x << endl
#define chmin(x,y) x=min(x,y)
#define chmax(x,y) x=max(x,y)
using namespace std;
vector<string> ash;
vector<string> ww[20];
vector<int> w[20];
bool isA[3000],isB[3000];
void solve(){
	rep(j,3000) isA[j]=isB[j]=0;
	ash.clear();
	rep(j,20) ww[j].clear(),w[j].clear();
	int N;
	scanf("%d\n",&N);
	rep(i,N){
		string s;
		getline(cin,s);
//		show(s);
		istringstream is(s);
		string t;
//		show(i);
		while(is>>t){
//			show(t);
			ash.pb(t);
			ww[i].pb(t);
		}
	}
	rep(i,N){
		sort(all(ww[i]));
		ww[i].erase(unique(all(ww[i])),ww[i].end());
	}
	sort(all(ash));
	ash.erase(unique(all(ash)),ash.end());
	rep(i,N){
		for(string s:ww[i]){
			w[i].pb(lower_bound(all(ash),s)-ash.begin());
		}
	}
	int MX=ash.size();
	int ans=3000;
	rep(i,1<<(N-2)){
		rep(j,MX) isA[j]=isB[j]=0;
		for(int k:w[0]) isA[k]=1;
		for(int k:w[1]) isB[k]=1;
		rep(j,N-2){
			bool x=(i>>j)&1;
			for(int k:w[j+2]){
				if(x) isA[k]=1;
				else isB[k]=1;
			}
		}
		int tmp=0;
		rep(j,MX) if(isA[j]&&isB[j]) tmp++;
		chmin(ans,tmp);
	}
	cout<<ans<<endl;
}
int main(){
	int T;
	cin>>T;
	rep1(tt,T){
		printf("Case #%d: ",tt);
		solve();
	}
}
