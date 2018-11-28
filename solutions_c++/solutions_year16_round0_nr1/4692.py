#include "bits/stdc++.h"
using namespace std;

int main(void){
	int i, t; cin>>t;
	for(i = 1; i <= t; i++){
		cout<<"Case #"<<i<<": ";
		int n; cin>>n;
		vector<int> num;
		num.resize(10, 0);
		int j = 0, c = 0;
		bool f = true;
		for(j = 1; j < 100 && f; j++){
			c = n*j;
			while(c != 0){
				int r = c%10;
				num[r]++;
				c = c/10;
			}
			int k;
			f = false;
			for(k = 0; k < 10; k++){
				if(num[k] == 0){
					f = true;
					break;
				}
			}
		}
		if(j == 100) cout<<"INSOMNIA"<<endl;
		else cout<<n*(j-1)<<endl;
	}
}
