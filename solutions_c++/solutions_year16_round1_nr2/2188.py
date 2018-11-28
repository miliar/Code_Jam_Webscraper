#include<bits/stdc++.h>
using namespace std;
vector<int> ans;
map<int,int> mape;
int main(){
	freopen("B-large.in","r",stdin);
	freopen("outB.txt","w",stdout);
	int t,n,data;
	cin>>t;
	for(int k=1;k<=t;k++){
		cin>>n;
		mape.clear();
		ans.clear();
		for(int i=0;i<2*n-1;i++){
			for(int j=0;j<n;j++){
				cin>>data;
				mape[data]++;
			}
		}
		cout<<"Case #"<<k<<":";
		for(auto it:mape){
			if(it.second>0&&(it.second%2))
				ans.push_back(it.first);
		}
		for(auto it:ans)
			cout<<" "<<it;
		cout<<endl;
	}
}
