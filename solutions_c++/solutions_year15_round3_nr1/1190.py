#include<iostream>
#include<vector>
#include<utility>
#include<algorithm>
#include<unordered_map>
#define ll long long int
#define umap unordered_map
using namespace std;

int main(){
	ios_base::sync_with_stdio(false);
	int T; cin>>T;
	for (int t = 0; t < T; t++){
		ll r,w,c;
		cin>>r>>c>>w;
		ll ans;
		ans = ceil(float(c)/float(w));
		ans += w-1;
		ans += (r-1) * (c/w);
		cout<<"Case #"<<t+1<<": "<< ans <<endl;
	}
	return 0;
}
