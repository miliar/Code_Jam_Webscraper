#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main(){
	int T;
	cin >> T;
	for(int test = 1; test <= T; ++test){
		int m;
		string s;
		cin >> m;
		cin >> s;
		vector<int> arr;
		for(int i = 0; i < s.size(); ++i)
			arr.push_back(s[i]-'0');
		int n = s.size();
		for(int i = 0; i < n-1; ++i)
			if(arr[i]>1)
				arr[i+1]+=arr[i]-1;
		int ans = 0;
		for(int i = 0; i < n; ++i)
			if(arr[i]==0)
				ans++;
		cout << "Case #" << test << ": " << ans << '\n';
	}
}

