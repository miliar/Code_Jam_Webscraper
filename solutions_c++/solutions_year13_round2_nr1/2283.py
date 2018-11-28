#include<iostream>
#include<sstream>
#include<string>
#include<vector>
#include<set>
#include<map>
#include<algorithm>
#include<cmath>

using namespace std;

int add(int& a, int m){
	int count=0;
	while(a <= m){
		a = 2*a -1;
		++count;
	}
	a += m;
	return count;
}

int solve(int a, vector<int> data){
	if(a == 1) return data.size();
	int ans=0;
	while(!data.empty()){
		if(a <= data[0]) break;
		a += data[0];
		data.erase(data.begin());
	}
	if(!data.empty()){
		int a_ = a;
		int ans_ = add(a_, data[0]);
		int size = data.size();
		data.erase(data.begin());
		ans += min(ans_ + solve(a_, data), size);
	}
	return ans;
}

int main(){
	int t, a, n;
	cin >> t;
	for(int i=0; i<t; ++i){
		cin >> a >> n;
		vector<int> data(n, 0);
		for(int j=0; j<n; ++j) cin >> data[j];
		sort(data.begin(), data.end());
		cout << "Case #" << i+1 << ": " << solve(a, data) << endl;
	}
	return 0;
}
