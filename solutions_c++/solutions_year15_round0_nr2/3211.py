#include<iostream>
#include<map>
#include<vector>
#include<cmath>
using namespace std;
int main(){
	int T;
	cin>>T;
	int k=1;
	while(k<=T){
		int D;
		cin>>D;
		vector<int> all(D);
		map<int, int> plates;
		for(int i=0; i<D; i++){
			int t;
			cin>>t;
			plates[t]++;
			all[i]=t;
		}
		int biggest = plates.rbegin()->first;
		int ans = biggest;
		for(float i=1; i<=biggest; i++){
			int x = 0;
			for(int j = 0; j<D; j++)
				x+=max((int)ceil(all[j]/i)-1,0);	
			ans = min(ans, int(x+i));
			//cout<<x+i<<" "<<i<<endl;
		}
		cout<<"Case #"<<k<<": "<<ans<<endl;
		k++;
	}
	return 0;
}


