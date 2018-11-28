#include <iostream>
#include "bits/stdc++.h"
#include "cmath"
using namespace std;

int main() {
	int t; cin>>t;
	int j;
	for(j = 1; j <= t; j++){
		printf("Case #%d: ", j);
		int n; cin>>n;
		vector<int> arr;
		arr.resize(n);
		long long ans1 = 0;
		int rate = 0;
		cin>>arr[0];
		int i;
		for(i = 1; i < n; i++){
			cin>>arr[i];
			int r = arr[i]-arr[i-1];
			if(r < 0){
				ans1 -= r;
				r *= -1;
				if(rate < r) rate = r;
			}
		}
		long long ans2 = 0;
		for(i = 0; i < n-1; i++){
			ans2 += min(rate, arr[i]);
		}
		cout<<ans1<<" "<<ans2<<endl;
	}
	return 0;
}
