#include <bits/stdc++.h>
#define _ ios_base::sync_with_stdio(false);cin.tie(0);
using namespace std;
#define pb push_back
#define pob pop_back
#define pf push_front
#define pof pop_front
#define mp make_pair
#define all(a) a.begin(),a.end()
#define bitcnt(x) __builtin_popcountll(x)
#define MOD 1000000007
#define BASE1 31
#define BASE2 255
#define MOD1 1000003
typedef unsigned long long int uint64;
typedef long long int int64;
 
map<string,vector<int> >m1,m2;

int main(){
	int t,i,j,n,k;
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	string s1[20],s2[20];
	cin>>t;
	for(int cas=1;cas<=t;cas++){
		printf("Case #%d: ",cas);
		cin>>n;
		m1.clear();
		m2.clear();
		
		for(i=0;i<n;i++){
			cin>>s1[i]>>s2[i];
			m1[s1[i]].pb(i);
			m2[s2[i]].pb(i);
		}
		int ans=1e9;
		for(i=1;i<(1<<n);i++){
			bool pres=true;
		
			vector<int>v;
			for(j=0;j<n;j++){
				if(i&(1<<j))
				v.pb(j);
			}
			
			for(j=0;j<n;j++){
				if(binary_search(all(v),j))
				continue;
				vector<int>req=m1[s1[j]];
				for(k=0;k<req.size();k++){
					int idx=req[k];
					if(binary_search(all(v),idx))
					break;
				}
				if(k==req.size()){
					pres=false;
					break;
				}
				
				req=m2[s2[j]];
				for(k=0;k<req.size();k++){
					int idx=req[k];
					if(binary_search(all(v),idx))
					break;
				}
				if(k==req.size()){
					pres=false;
					break;
				}
			}
		//	cout<<i<<" "<<j<<" "<<v.size()<<endl;
			if(j==n){
				ans=min(ans,(int)v.size());
			}
			
		}
		cout<<n-ans<<endl;
	}
	fclose(stdout);
	return 0;
}
