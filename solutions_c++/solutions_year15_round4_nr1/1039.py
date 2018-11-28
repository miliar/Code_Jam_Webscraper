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

int main(){

	freopen("A-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	int t,r,c;
	cin>>t;
	int cnt=0;
	char a[111][111];
	while(t--){
		cnt++;
		cin>>r>>c;
		rep(i,r)
			rep(j,c)
				cin>>a[i][j];
		int ans=0;
		int u=0;
		int d=0;
		int lt=0;
		int rt=0;
		ans=0;
		bool pos=1;
		rep(i,r){
			rep(j,c){
				if(a[i][j]!='.'){
					u=d=lt=rt=0;
					for(int k=i-1;k>=0;k--){
						if(a[k][j]!='.') u=1;
					}
					for(int k=i+1;k<r;k++){
						if(a[k][j]!='.') d=1;
					}
					for(int k=j-1;k>=0;k--){
						if(a[i][k]!='.') lt=1;

					}
					for(int k=j+1;k<c;k++){
						if(a[i][k]!='.') rt=1;
					}
				//	cout<<u<<" ";
					if(a[i][j]=='^' and u==1) continue;
					if(a[i][j]=='v' and d==1) continue;
					if(a[i][j]=='<' and lt==1) continue;
					if(a[i][j]=='>' and rt==1) continue;
					ans++;
					if(u==0 and lt==0 and d==0 and rt==0){
						pos=0;
						break;
					}
				}
			}
			if(!pos) break;
		}
		if(pos)
			cout<<"Case #"<<cnt<<": "<<ans<<"\n";
		else
			cout<<"Case #"<<cnt<<": "<<"IMPOSSIBLE"<<"\n";
	}
}
