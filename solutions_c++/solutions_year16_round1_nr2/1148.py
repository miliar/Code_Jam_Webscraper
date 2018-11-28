#include <bits/stdc++.h>
using namespace std;
typedef long double ld;
typedef long long ll;
string solve(){
	int n;
	cin >> n;
	vector<int> cnt(2501);
	for(int i = 0; i < n*(2*n-1); ++i){
		int a;
		cin >> a;
		cnt[a]^=1;
//		cout << a << '\n';
	}
	vector<int> arr;
	for(int i = 0; i <= 2500; ++i)
		if(cnt[i])
			arr.push_back(i);
	string ans;
	for(int i = 0; i < arr.size(); ++i){
		if(i)
			ans += " ";
		ans += to_string(arr[i]);
	}
	return ans;
}
int main(){
	int T;
	cin >> T;
	for(int tc = 1; tc <= T; ++tc){
		cout << "Case #" << tc << ": " << solve() << '\n';
	}
}

