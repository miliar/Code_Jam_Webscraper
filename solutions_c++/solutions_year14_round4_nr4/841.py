#include<bits/stdc++.h>
using namespace std;


int sol(){
	int n,m;
	cin >> n >> m;
	string a[8];
	int all=1;
	for(int i=0;i<n;++i){
		cin >> a[i];
		all*=m;
	}
	int ans=-1,cnt=0;
	for(int k=0;k<all;++k){
		set<string> u[4];
		for(int t=k,i=0;i<n;++i,t/=m) {
			set<string>& y=u[t%m];
			for(int j=0;j<=a[i].length();++j)
				y.insert(a[i].substr(0,j));
		}
		int tmp=0;
		for(int i=0;i<m;++i)tmp+=u[i].size();
		if(tmp>ans){ans=tmp;cnt=0;}
		if(tmp==ans)++cnt;
	}
	cout << ans << " " << cnt << endl;
	
}
int main(){
	int T;
	cin >> T;
	for(int i=1;i<=T;++i){
		cout << "Case #"<<i <<": ";
		sol();
	}
}
