#include<bits/stdc++.h>
#define ll long long int
using namespace std;
int main(){
	freopen("B-large.in","r",stdin);
	freopen("new.txt","w",stdout);
	int t;
	int f=0;
	cin>>t;
	while(t--){
		ll ans=99999999;
		f++;
		int n; cin>>n;
		int a[n+1];
		int m=0;
		for(int i=0; i<n; i++){
			cin>>a[i];
			m=max(m,a[i]);	
		} 
		sort(a,a+n);
		for(int j=1; j<=m; j++){
			ll val=j;
			for(int i=0; i<n; i++){
				val= val+ (a[i]/j);
				if(a[i]%j==0) val--;
			}
			ans=min(ans,val);
		}
		cout<<"Case #"<<f<<": "<<ans<<endl;
	}
}
