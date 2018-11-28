#include <bits/stdc++.h>
using namespace std;
int main() {
	freopen ("A-large.in","r",stdin);
	freopen ("A-large.out","w",stdout);
	int t, n;
	cin>>t;
	for(int tc = 1; tc <= t; tc++) {
		cin>>n;
		vector<int> v(n);
		int maxi = 0;
		for(int i = 0; i < n; i++){
			cin>>v[i];
			maxi += v[i];
		}
		cout<<"Case #"<<tc<<":";
		while(maxi > 0){
			int ind = -1;
			for(int i = 0;i < n; i++){
				if(ind != -1){
					if(v[i] > v[ind]){
						ind = i;
					}
				}else{
					ind = i;
				}
			}
			cout<<" "<<char(ind + 'A');
			v[ind]--; 
			maxi--; 
			ind = -1;
			for(int i = 0;i < n; i++){
				//cout<<v[i]<<":"<<(maxi / 2)<<endl;
				if(v[i] > maxi / 2){
					ind = i;
					break;
				}
			}
			if(ind >= 0){
				cout<<char(ind + 'A');
				v[ind]--; 
				maxi--; 
			}
		}
		cout<<endl;
	} 
	return 0;
}