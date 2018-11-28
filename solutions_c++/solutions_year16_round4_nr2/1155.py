#include <bits/stdc++.h>

using namespace std;
long double calc(vector<long double> &t){
	long double ans=0;
	for(int i=0;i<(1<<(t.size()));i++){
		int ones=__builtin_popcount(i);
		long double now=1;
		if(ones==(t.size()/2)){
			for(int j=0;j<t.size();j++){
				if(i&(1<<j)){
					now*=t[j];
				}else{
					now*=(1-t[j]);
				}
			}
		}else{
			continue;
		}
		ans+=now;
	}
	return ans;
}
int main(){
	int tc,casen=1;
	cin>>tc;
	while(tc-->0){
		int n,k;
		cin>>n>>k;
		vector<long double>prob,ch;
		for(int i=0;i<n;i++){
			long double t;
			cin>>t;
			prob.push_back(t);;
		}
		long double ans=0;
		for(int i=0;i<(1<<n);i++){
			if(__builtin_popcount(i)!=k)continue;
			vector<long double>toc;
			for(int j=0;j<n;j++){
				if(i&(1<<j)){
					toc.push_back(prob[j]);
				}
			}
			ans=max(ans,calc(toc));
		}
		cout<<"Case #"<<casen++<<": "<<fixed<<setprecision(15)<<ans<<endl;
	}
	return 0;
}
