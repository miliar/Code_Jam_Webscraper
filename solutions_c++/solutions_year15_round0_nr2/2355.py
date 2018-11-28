#include <bits/stdc++.h>
using namespace std;
int cases,n;
int v[1010];
int maxi;
int solve(){
	int mini=maxi;
	for(int x=1;x<=maxi;x++){
		int c=0;
		for(int i=0;i<n;i++){
			if(v[i]>x){
				double num=double(v[i])/double(x);
				num=ceil(num);
				c+=num-1;
			}				
		}
			mini=min(x+c,mini);
	}
	return mini;
}
int main(){
	ios::sync_with_stdio(false);
	cin.tie(0);
	cin>>cases;
	int tc=1;
	while(cases--){
		cin>>n;
		maxi=0;
		for(int i=0;i<n;i++){
			cin>>v[i];
			maxi=max(maxi,v[i]);
		}
		cout<<"Case #"<<tc++<<": "<<solve()<<"\n";	
	}
	return 0;
}
