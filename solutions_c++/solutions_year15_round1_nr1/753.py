#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main(){
	int T;
	cin >> T;
	for(int test = 1; test <= T; ++test){
		int n;
		cin >> n;
		vector<int> arr(n);
		int sum = 0, max_jump = 0, ans = 0;
		for(int i = 0; i < n; ++i){
			cin >> arr[i];
			if(i>0){
				max_jump=max(max_jump,arr[i-1]-arr[i]);
				sum+=max(0,arr[i-1]-arr[i]);
			}
		}
		for(int i = 0; i < n-1; ++i)
			ans+=min(max_jump,arr[i]);
		cout << "Case #" << test << ": " << sum << ' ' << ans << '\n';
	}
}

