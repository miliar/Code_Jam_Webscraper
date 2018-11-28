#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
long long cnt(vector<int> arr, long long t){
	long long ans = 0;
	for(int i = 0; i < arr.size(); ++i)
		ans+=t/arr[i]+1;
	return ans;
}
int solve(vector<int> arr, long long n){
	if(cnt(arr,0)>=n){
		return n;
	}
	long long lo = 0, hi = 1e16, mid;
	while(lo<hi){
		mid = (lo+hi+1)/2;
		if(cnt(arr,mid)<n)
			lo=mid;
		else
			hi=mid-1;
	}
	n-=cnt(arr,lo);
	long long t = lo+1;
	for(int i = 0; i < arr.size(); ++i){
		if(t%arr[i]==0)
			n--;
		if(n==0)
			return i+1;
	}
	return -1;
}
int main(){
	int T;
	cin >> T;
	for(int test = 1; test <= T; ++test){
		int b,n;
		cin >> b >> n;
		vector<int> arr(b);
		for(int i = 0; i < b; ++i)
			cin >> arr[i];
		cout << "Case #" << test << ": " << solve(arr,n) << '\n';
	}
}

